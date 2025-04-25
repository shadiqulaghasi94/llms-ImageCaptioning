from transformers import pipeline
import requests
from PIL import Image
from io import BytesIO
from transformers import AutoProcessor, BlipForConditionalGeneration


def extract_text(soup):
        # Extract all text from the webpage
        text = soup.get_text().strip().replace('\n\n','').splitlines()
        text_list = [line for line in text if len(line) > 1000 and len(line) < 2000]

        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

        # Open a file to write the captions
        with open("summaries.txt", "w") as summary_file:
            # Iterate over each img element
            for my_text in text_list:
                summary = summarizer(my_text, max_length=150)[0]['summary_text']

                # Write the caption to the file, prepended by the image URL
                summary_file.write(f"{summary}\n")


def extract_images_and_captions(soup):
    # Load the pretrained processor and model
    processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    # Find all img elements
    img_elements = soup.find_all('img')

    # Open a file to write the captions
    with open("captions.txt", "w") as caption_file:
        # Iterate over each img element
        for img_element in img_elements:
            img_url = img_element.get('src')

            # Skip if the image is an SVG or too small (likely an icon)
            if 'svg' in img_url or '1x1' in img_url:
                continue

            # Correct the URL if it's malformed
            if img_url.startswith('//'):
                img_url = 'https:' + img_url
            elif not img_url.startswith('http://') and not img_url.startswith('https://'):
                continue  # Skip URLs that don't start with http:// or https://

            try:
                # Download the image
                response = requests.get(img_url)
                # Convert the image data to a PIL Image
                raw_image = Image.open(BytesIO(response.content))
                if raw_image.size[0] * raw_image.size[1] < 400:  # Skip very small images
                    continue

                raw_image = raw_image.convert('RGB')

                # Process the image
                inputs = processor(raw_image, return_tensors="pt")
                # Generate a caption for the image
                out = model.generate(**inputs, max_new_tokens=50)
                # Decode the generated tokens to text
                caption = processor.decode(out[0], skip_special_tokens=True)

                # Write the caption to the file, prepended by the image URL
                caption_file.write(f"{img_url}: {caption}\n")
            except Exception as e:
                print(f"Error processing image {img_url}: {e}")
                continue