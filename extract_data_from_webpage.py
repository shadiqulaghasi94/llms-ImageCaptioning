import argparse
import requests
from bs4 import BeautifulSoup
from web_extraction.utils import extract_text, extract_images_and_captions

# Suppress warnings from the transformers library
import warnings
warnings.filterwarnings("ignore")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract data from a webpage.")
    parser.add_argument(
        "--url", type=str, 
        help="The URL of the webpage to scrape.", 
        default="https://en.wikipedia.org/wiki/IBM")
    parser.add_argument(
        "--extract", choices=["images", "text"], 
        required=True, 
        help="Choose whether to extract images or text.")
    args = parser.parse_args()

    # Download the page
    response = requests.get(args.url)
    # Parse the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Perform the chosen extraction
    if args.extract == "images":
        extract_images_and_captions(soup)
    elif args.extract == "text":
        extract_text(soup)