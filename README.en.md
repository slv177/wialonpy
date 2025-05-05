# Wialonpy

**Wialonpy** is a Python library that simplifies working with the Wialon Hosting and Wialon Local APIs.

## Why This Library

Among fleet management systems, Wialon holds a leading position. One of its main advantages is a powerful and flexible API that allows for nearly any operation. However, this flexibility can also make the API challenging to use—especially for seemingly simple tasks like retrieving a report.

That was exactly our case when we first started using the API: we faced numerous parameters, concise but complex documentation ([sdk.wialon.com](https://sdk.wialon.com/wiki/en/start)), and often had to reach out to support (which, to be fair, is very responsive and helpful).

## What the Library Does

Wialonpy is the library we wished we had from the beginning. It implements a set of the most commonly used API calls, primarily focused on working with reports.

### Key Functions:

- `get_session_eid` – retrieves the session key
- `get_wialon_object_id` – retrieves the ID of an object (usually a unit group) by its name
- `get_wialon_report_id` – retrieves the report template ID by name
- `get_wialon_units` – retrieves a list of units with their IDs
- `wialon_exec_report` – executes a report on the server
- `wialon_select_result` – fetches report result rows, with optional `row_from`, `row_to`, and `level` support

### Support for Wialon Hosting and Local

The library allows you to specify a custom server URL, making it compatible with both Wialon Hosting and Wialon Local (self-hosted by a service provider).

## Installation

```bash
pip install wialonpy
```

### Feedback

Wialonpy is under active development. We welcome suggestions and feedback, especially regarding other useful Wialon API calls you’d like to see implemented.

### Disclaimer

We are independent developers specializing in Wialon-based solutions. We are not affiliated with Gurtam, the vendor of Wialon and other fleet management products.