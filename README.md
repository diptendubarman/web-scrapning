# Email Extractor from Google Search

This Python script extracts email addresses from Google search results using Playwright and Chromium. The script accepts a proxy (such as a browserless.io or SuperProxy proxy) to connect through Chromium's CDP (Chrome DevTools Protocol) and automates Google search scraping for emails related to a given query.

## Features

- Automatically generates Google search URLs based on the provided query.
- Extracts emails from search result pages using regex.
- Saves the extracted emails to a text file (`emails.txt`).
- Handles pagination of Google search results.
- Graceful handling of script interruptions.

## Requirements

- Python 3.7+
- [Playwright](https://playwright.dev/python/docs/intro)
- Chromium browser for Playwright
- A valid proxy URL for connecting to Chromium's CDP (Chrome DevTools Protocol).

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/email-extractor.git
   cd email-extractor
   ```

2. Install the required dependencies:

   ```bash
   pip install playwright
   playwright install
   ```

3. Run the script:

   ```bash
   python email_extractor.py
   ```

## Usage

1. Enter the proxy URL (e.g., `https://brd.superproxy.io:9222` or another valid proxy).
2. Enter your Google search query (e.g., `california "gmail.com"`).
3. The script will extract emails from the Google search results and save them in `emails.txt`.

### Example

```bash
Enter the proxy (e.g., https://brd.superproxy.io:9222): https://yourproxy.io:9222
Enter your search query (e.g., "california \"gmail.com\""): california "gmail.com"
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for review.

## Disclaimer

Google search scraping is against Google’s [Terms of Service](https://policies.google.com/terms). Use this script responsibly and consider the legal implications before running it.