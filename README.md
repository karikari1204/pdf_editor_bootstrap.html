# Web Page Scraper to GAS

This repository contains a Python script that uses Selenium to scrape content from a web page and send it to a Google Apps Script (GAS) endpoint.

## Requirements

- Python 3.8+
- Chromium and chromedriver (or Chrome and chromedriver) installed
- `pip` for installing Python packages

Install Python dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

Set the GAS endpoint URL as an environment variable:

```bash
export GAS_URL="https://script.google.com/macros/s/EXAMPLE/exec"
```

Run the script with the target URL and a CSS selector for the element you wish to extract:

```bash
python web_to_gas.py "https://example.com" "h1"
```

The text from the selected element will be sent to the GAS endpoint as JSON.

## Google Apps Script Example

A minimal GAS script that accepts a POST request:

```javascript
function doPost(e) {
  const data = JSON.parse(e.postData.contents);
  // handle data.text as needed
  return ContentService.createTextOutput('Received: ' + data.text);
}
```

Save this as a Web App and use the deployed URL as `GAS_URL`.
