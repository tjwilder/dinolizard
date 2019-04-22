
# Download images from the given file

import sys
import urllib.request
import requests
from os import mkdir
from os.path import join, exists

file = open(sys.argv[1], 'r')
root = './' + sys.argv[1][: sys.argv[1].rfind('.')]
print(root)
if not exists(root):
    mkdir(root)

urls = file.read().split('\n')

file.close()

# Make the actual request, set the timeout for no data to 10 seconds and enable streaming responses so we don't have to keep the large files in memory


# Now for each url, load the image
downloads = 0
for url in urls:
    img_name = url[url.rfind('/')+1:]
    try:
        request = requests.get(url, timeout=3, stream=True)
        # Open the output file and make sure we write in binary mode
        with open(join(root, img_name), 'wb') as fh:
            # Walk through the request response in chunks of 1024 * 1024 bytes, so 1MiB
            for chunk in request.iter_content(1024 * 1024):
                # Write the chunk to the file
                fh.write(chunk)
                # Optionally we can check here if the download is taking too long
        downloads += 1
        print(f'Downloaded {downloads}')
    except SystemExit as e:
        raise
    except:
        print('Missing file, continuing...')
