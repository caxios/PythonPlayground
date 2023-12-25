from PIL import Image
import os
import requests
from bs4 import BeautifulSoup
from io import BytesIO
from google.colab import files


def convert_to_image(img_url, output_format='PNG'):
    # Check if the output format is valid
    if output_format.upper() not in ['JPEG', 'PNG']:
        raise ValueError("Output format must be either 'PNG' or 'JPEG'")

    # Send a GET request to the image URL and download the image
    img_data = requests.get(img_url).content

    # Try to open the input file
    try:
        with Image.open(BytesIO(img_data)) as img:
            safe_filename = ''.join(e for e in os.path.basename(img_url) if e.isalnum())
            # Generate a safe filename from the URL
            output_file_name = os.path.splitext(safe_filename)[0] + '.' + output_format.lower()

            # Define the output file path (you might want to customize the directory)
            output_file_path = os.path.join(os.getcwd(), output_file_name)

            # Convert and save the image
            img.convert('RGB').save(output_file_path, output_format.upper())
            print(f"File converted and saved as {output_file_path}")
            
            # Download the file
            files.download(output_file_path)

    except Exception as e:
        print(f"An error occurred: {e}")


# convert_to_image('https://cdn.midjourney.com/587f28ef-4744-4ca1-97a8-a5cd66715b29/0_0_2048_N.webp?method=width&qst=6', 'PNG')  # Convert to PNG
