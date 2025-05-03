import requests
import json
import logging
from typing import Optional

logger = logging.getLogger(__name__)

DEFAULT_WIALON_URL = "https://hst-api.wialon.com/wialon/ajax.html"

class WialonAuthError(Exception):
    """Raised when Wialon authentication fails."""
    pass

class WialonAPIError(Exception):
    """Raised when Wialon API returns invalid or unexpected data."""
    pass


def wialon_get_session_eid(w_token: str, wialon_url: str = DEFAULT_WIALON_URL) -> Optional[str]:
    """
    Authenticate with Wialon API using a token and return the session ID (eid).

    Args:
        w_token (str): Wialon API token.
        wialon_url (str): URL to Wialon API. Defaults to production endpoint.

    Returns:
        Optional[str]: Session ID (eid) if successful, otherwise None.

    Raises:
        WialonAuthError: If the authentication fails.
        requests.exceptions.RequestException: If the request fails.
    """
    try:
        params = {
            "svc": "token/login",
            "params": json.dumps({"token": w_token}),
        }
        response = requests.post(wialon_url, params=params)
        response.raise_for_status()

        data = response.json()
        eid = data.get("eid")

        if not eid:
            logger.warning("Wialon returned no session ID: %s", data)
            raise WialonAuthError("No session ID returned by Wialon")

        return eid

    except requests.RequestException as e:
        logger.error("Wialon request failed: %s", e)
        raise
    except json.JSONDecodeError as e:
        logger.error("Failed to parse Wialon response: %s", e)
        raise WialonAuthError("Invalid JSON response from Wialon")



def get_wialon_object_id(group_name: str, eid: str, wialon_url: str = DEFAULT_WIALON_URL) -> str:
    """
    Retrieve the ID of a unit group by its name from Wialon.

    Args:
        group_name (str): Name of the unit group to search.
        eid (str): Session ID obtained from Wialon.
        wialon_url (str): Base URL to the Wialon API.

    Returns:
        str: ID of the unit group with the given name.

    Raises:
        requests.exceptions.RequestException: Network-related error.
        WialonAPIError: If the group is not found or response structure is unexpected.
    """
    try:
        params = {
            "svc": "core/search_items",
            "params": json.dumps({
                "spec": {
                    "itemsType": "avl_unit_group",
                    "propName": "sys_name",
                    "propValueMask": "*",
                    "sortType": "sys_id"
                },
                "force": 1,
                "flags": 1,
                "from": 0,
                "to": 0
            }),
            "sid": eid
        }
        response = requests.get(wialon_url, params=params)
        response.raise_for_status()

        data = response.json()
        items = data.get("items")
        if not items or not isinstance(items, list):
            logger.error("Unexpected Wialon response format: %s", data)
            raise WialonAPIError("No unit groups returned from Wialon")

        for item in items:
            if item.get("nm") == group_name:
                return str(item["id"])

        # Если не найдено — собрать список всех групп для вывода
        group_list = [f"{item.get('nm')} (id={item.get('id')})" for item in items]
        message = (
            f"Group '{group_name}' not found. Available groups: "
            + ", ".join(group_list)
        )
        logger.error(message)
        raise WialonAPIError(message)

    except requests.RequestException as e:
        logger.error("Wialon API request failed: %s", e)
        raise
    except (ValueError, KeyError, TypeError) as e:
        logger.error("Failed to parse Wialon response: %s", e)
        raise WialonAPIError("Invalid response format from Wialon") from e
