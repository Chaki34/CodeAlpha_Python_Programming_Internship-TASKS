
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from html.parser import HTMLParser
from pathlib import Path


OUTPUT_FILE = "webpage_title.txt"


class TitleExtractor(HTMLParser):
    """Extract the title text from HTML content."""

    def __init__(self):
        super().__init__()
        self.inside_title = False
        self.title_parts = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "title":
            self.inside_title = True

    def handle_endtag(self, tag):
        if tag.lower() == "title":
            self.inside_title = False

    def handle_data(self, data):
        if self.inside_title:
            self.title_parts.append(data.strip())

    def get_title(self):
        return " ".join(part for part in self.title_parts if part).strip()


def extract_webpage_title(url):
    """Fetch a webpage and return its title."""

    request = Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    with urlopen(request, timeout=15) as response:
        html_content = response.read().decode(
            response.headers.get_content_charset() or "utf-8",
            errors="replace"
        )

    parser = TitleExtractor()
    parser.feed(html_content)

    return parser.get_title()


def save_title(url, title):
    """Save the extracted title and URL to a text file."""

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write(f"Webpage URL: {url}\n")
        file.write(f"Webpage Title: {title}\n")

    print(f"\nResult saved successfully to {OUTPUT_FILE}")


def main():
    print("=" * 55)
    print("             WEBPAGE TITLE EXTRACTOR")
    print("                 EXTRA PROJECT")
    print("                  CodeAlpha")
    print("=" * 55)

    url = input("\nEnter webpage URL: ").strip()

    if not url.startswith(("http://", "https://")):
        print("\nError: Please enter a valid URL starting with")
        print("http:// or https://")
        return

    try:
        print("\nFetching webpage and extracting title...")

        title = extract_webpage_title(url)

        if not title:
            print("\nNo webpage title was found.")
            return

        print("\n" + "-" * 55)
        print("EXTRACTION RESULT")
        print("-" * 55)
        print(f"Webpage URL   : {url}")
        print(f"Webpage Title : {title}")
        print("-" * 55)

        save_title(url, title)

    except HTTPError as error:
        print(f"\nHTTP Error: {error.code} - {error.reason}")

    except URLError as error:
        print(f"\nConnection Error: {error.reason}")

    except TimeoutError:
        print("\nError: The request timed out.")

    except OSError as error:
        print(f"\nFile or network error: {error}")

    except Exception as error:
        print(f"\nUnexpected error: {error}")

    print("\nWebpage title extraction process completed.")
    print("=" * 55)


if __name__ == "__main__":
    main()
