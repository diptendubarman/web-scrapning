# email_extractor.py

import asyncio
import re
from playwright.async_api import async_playwright


# Generate Google search URL
def generate_google_search_url(query, page):
    base_url = "https://www.google.com/search"
    query = query.replace(" ", "+")  # URL encode the query
    start = page * 10
    url = f"{base_url}?q={query}&start={start}"
    return url


async def extract_emails_from_google(sbr_cdp, query):
    async with async_playwright() as pw:
        browser = await pw.chromium.connect_over_cdp(sbr_cdp)
        try:
            page = await browser.new_page()
            page_number = 0
            found_emails = set()  # Set to store unique email addresses

            while True:
                try:
                    # Generate Google search URL
                    url = generate_google_search_url(query, page_number)
                    print(f"Fetching page {page_number + 1} from: {url}")

                    # Navigate to the Google search results page
                    await page.goto(url)

                    # Wait for the page to load
                    await page.wait_for_timeout(2000)

                    # Get the content of the page
                    html = await page.content()

                    # Use regex to find all email addresses
                    emails = set(
                        re.findall(
                            r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", html
                        )
                    )
                    found_emails.update(emails)  # Add found emails to the set

                    if emails:
                        print(f"Found emails: {len(emails)}")
                    else:
                        print("No emails found on this page. Stopping script.")
                        break  # Stop if no emails are found

                    page_number += 1  # Move to the next page
                    
                except KeyboardInterrupt:
                    print("\nScript stopped by user. Exiting gracefully...")
                    break  # Exit the loop to stop scraping

            # Save found emails to a text file named after the city
            if found_emails:
                with open("emails.txt", "w") as f:
                    for email in found_emails:
                        f.write(email + "\n")
                print(f"Saved {len(found_emails)} emails to 'emails.txt'")
            else:
                print("No emails found to save.")
        
        finally:
            await browser.close()


# Example usage
if __name__ == "__main__":
    try:
        # Get proxy input
        while True:
            proxy = input("Enter the proxy (e.g., https://brd.superproxy.io:9222): ")
            if proxy.strip():  # Check if input is not empty
                break
            print("Proxy is required. Please enter a valid proxy.")

        # Get query input
        while True:
            query = input('Enter your search query (e.g., "california \"gmail.com\""): ')
            if query.strip():  # Check if input is not empty
                break
            print("Query is required. Please enter a valid search query.")
        
        asyncio.run(extract_emails_from_google(proxy, query))

    except KeyboardInterrupt:
        print("\nExiting gracefully...")

