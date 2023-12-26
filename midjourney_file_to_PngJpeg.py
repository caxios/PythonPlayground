from PIL import Image
import os
import requests
from bs4 import BeautifulSoup
from io import BytesIO
from google.colab import files
import re

def convert_to_image(img_url, output_format='PNG'):
    # Check if the output format is valid
    if output_format.upper() not in ['JPEG', 'PNG']:
        raise ValueError("Output format must be either 'PNG' or 'JPEG'")

    # Send a get request to the image URL and download the image
    img_data = requests.get(img_url).content

    pattern = r'/([^/]+)/[^/]*$' # regular expression of getting second-to-last part of url(or filepath)
    pattern_filename = re.search(pattern, img_url)

    # open the input file
    try:
        with Image.open(BytesIO(img_data)) as img:
            # generate filename using url
            filename = ''.join(e for e in pattern_filename.group() if e.isalnum())
            """
            change, this line of code : 
            # filename = ''.join(e for e in os.path.basename(img_url) if e.isalnum()) # since file name cannot use !&* something like this symbols
            since, when downloading image, there are so many times filename duplicated. 
            'basename' function returns last part of filename, and image links of midjourney often time same. 
            """
            output_file_name = os.path.splitext(filename)[0] + '.' + output_format.lower()
            # output_file_name = filename.split(".")[0] + '.' + output_format.lower()

            # define the output file path
            output_file_path = os.path.join(os.getcwd(), output_file_name)

            # convert and save the image
            img.convert('RGB').save(output_file_path, output_format.upper())
            print(f"File converted and saved as {output_file_path}")
            
            # download the file
            files.download(output_file_path)

    except Exception as e:
        print(f"An error occurred: {e}")


# convert_to_image('https://cdn.midjourney.com/587f28ef-4744-4ca1-97a8-a5cd66715b29/0_0_2048_N.webp?method=width&qst=6', 'PNG')  # Convert to PNG
