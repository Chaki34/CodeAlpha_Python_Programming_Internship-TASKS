
import re
from pathlib import Path


# File names used by the email extractor
INPUT_FILE = "input_emails.txt"
OUTPUT_FILE = "extracted_emails.txt"


def extract_emails(text):
    """
    Find email addresses from the given text
    using a regular expression.
    """

    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

    emails = re.findall(email_pattern, text)

    # Remove duplicate email addresses while preserving their order.
    unique_emails = list(dict.fromkeys(emails))

    return unique_emails


def read_input_file():
    """Read the contents of the input text file."""

    input_path = Path(INPUT_FILE)

    if not input_path.exists():
        print(f"\nError: {INPUT_FILE} was not found.")
        print("Please create the input file and try again.")
        return None

    try:
        with input_path.open("r", encoding="utf-8") as file:
            return file.read()

    except OSError as error:
        print(f"\nUnable to read the input file: {error}")
        return None


def save_emails(emails):
    """Save the extracted email addresses into an output file."""

    try:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as file:

            for email in emails:
                file.write(email + "\n")

        print(f"\nExtracted email addresses saved to {OUTPUT_FILE}")

    except OSError as error:
        print(f"\nUnable to save the output file: {error}")


def main():
    print("=" * 50)
    print("          EMAIL ADDRESS EXTRACTOR")
    print("             CodeAlpha Task 3")
    print("=" * 50)

    # Read the input text file.
    text = read_input_file()

    if text is None:
        return

    # Extract email addresses from the text.
    emails = extract_emails(text)

    print("\nExtraction Results")
    print("-" * 50)

    if not emails:
        print("No email addresses were found.")

    else:
        print(f"Total unique email addresses found: {len(emails)}")

        for number, email in enumerate(emails, start=1):
            print(f"{number}. {email}")

    # Save the extracted results.
    save_emails(emails)

    print("\nEmail extraction process completed.")
    print("=" * 50)


if __name__ == "__main__":
    main()
