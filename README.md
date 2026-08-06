
# DM Holiday Automation

Automatically monitors the **Uttarakhand DIPR Facebook page** for school holiday announcements and triggers a **SinricPro Motion Sensor** when a matching post is detected. The project is designed to run periodically (e.g., every 10–15 minutes) using **GitHub Actions** or any other scheduler.

## Features

- Monitors the official Uttarakhand DIPR Facebook page.
- Detects holiday announcements using configurable keyword matching.
- Uses Selenium with headless Chrome.
- Sends a motion event to a SinricPro Motion Sensor.
- Reads credentials securely from environment variables.
- Suitable for scheduled execution on GitHub Actions or a Linux server.

## Requirements

- Python 3.10+
- Google Chrome or Chromium
- Selenium
- SinricPro Python SDK

Install dependencies:

```bash
pip install selenium sinricpro
```

## Configuration

Set the following environment variables:

| Variable                 | Description                       |
| ------------------------ | --------------------------------- |
| `DMSWITCH_DEVICE_ID`   | SinricPro Motion Sensor Device ID |
| `SINRICPRO_APP_KEY`    | SinricPro App Key                 |
| `SINRICPRO_APP_SECRET` | SinricPro App Secret              |

## How It Works

1. Launches a headless Chrome browser.
2. Opens the Uttarakhand DIPR Facebook page.
3. Closes the cookie/dialog popup if present.
4. Scrolls to load recent posts.
5. Searches for a Facebook post containing the configured keywords.
6. Sends a motion event (`True` or `False`) to SinricPro.
7. Exits.

The script is intended to be executed periodically by a scheduler rather than running continuously.

## Customizing Detection

The keywords used to identify a holiday announcement are defined in `checker.py` as an XPath expression. Update them whenever the announcement format changes.

## Disclaimer

This project relies on the current structure of Facebook pages. If Facebook changes its HTML or page layout, the Selenium selectors may need to be updated.

This project is not affiliated with Meta, Facebook, the Uttarakhand Department of Information and Public Relations (DIPR), or SinricPro.

## **AI Usage Disclosure**

Generative AI was used solely to assist with writing and editing the repository’s documentation and metadata (such as the README, repository description, and similar explanatory text).

The application code, automation logic, Selenium implementation, and overall software design were developed by the author. AI was **not** used to generate or write the project’s source code.
