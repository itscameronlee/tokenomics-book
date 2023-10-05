import requests
import os
import re
import shutil

# I had chat gpt throw together some quick code for the images
# It doesnt really work and i dont have time to fix it
# I'm leaving it here in case anyone wants to build on it
#
# I moved this to a subdirectory so you'll need to update filepaths to use this
#


def download_images_and_update_urls(markdown_text):
    # Check for/create images directory
    if not os.path.exists('images'):
        os.makedirs('images')

    # Regex to find markdown image syntax and special syntax
    image_regex = re.compile(r'(!\[(.*?)\]\((.*?)\))|(!https://[^\s]+)')

    # Function to download image and return new image path
    def replace_url(match):
        # Determine the URL based on the matched syntax
        url = match.group(3) if match.group(3) else match.group(4)
        
        # Remove '!' from the beginning of the URL if present
        url = url[1:] if url.startswith('!') else url
        
        try:
            response = requests.get(url, stream=True, timeout=10)  # added a timeout
            response.raise_for_status()  # check that the request was successful
        except requests.RequestException as e:
            print(f"Failed to retrieve {url}: {e}")
            return match.group(0)  # return the original text if the request fails
        
        # Get image filename from URL or create a new filename
        filename = url.split('/')[-1] if '/' in url else 'image.jpg'
        filepath = os.path.join('images', filename)
        
        # Ensure the filename includes a filetype
        if '.' not in filename:
            filepath += '.jpg'  # default to .jpg if no filetype is provided
        
        # Save image to disk
        with open(filepath, 'wb') as f:
            shutil.copyfileobj(response.raw, f)
        
        # Return new markdown image syntax with local path
        return f'![Alt text]({filepath})'
    
    # Replace all markdown image syntax with new syntax with local paths
    updated_markdown_text = image_regex.sub(replace_url, markdown_text)
    
    return updated_markdown_text

# Read the markdown text from a file
with open('tokenomics-book.md', 'r') as f:
    markdown_text = f.read()

updated_text = download_images_and_update_urls(markdown_text)

# Save the updated text to a new file
with open('updated_text.md', 'w') as f:
    f.write(updated_text)
