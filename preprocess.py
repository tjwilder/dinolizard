# Python program to read image using OpenCV 

# importing OpenCV(cv2) module
import cv2
import sys
import numpy as np
from os import mkdir, listdir
from os.path import join, exists

print()

# Folder
if len(sys.argv) > 1:
    root = sys.argv[1]

# If they entered more arguments, we'll categorize them
categories = []
if len(sys.argv) > 2:
    for i in np.arange(2, len(sys.argv)):
        categories.append(sys.argv[i])
        cat_dir = root + '_out_' + sys.argv[i]
        if not exists(cat_dir):
            mkdir(cat_dir)
    print('Images will be categorized starting at 1: ')
    print(categories)
    print('Or enter \'q\' at any time to quit')
    print()


# Save and quit function
def save_and_quit(last_file):
    f = open('progress.txt', 'w')
    f.write(root + '\n')
    f.write(last_file + '\n')
    f.write(','.join(f'{cat}' for _, cat in enumerate(categories)))
    f.close()

    cv2.destroyAllWindows() 
    sys.exit(0)

# Load progress
def load():
    print('Original state is being loaded...')
    f = open('progress.txt', 'r')
    stuff = f.read().split('\n')
    root = stuff[0]
    last_file = stuff[1]
    categories = stuff[2].split(',')
    f.close()

    # If we added additional categories manually, we need to make dirs for them
    for category in categories:
        cat_dir = root + '_out_' + category
        if not exists(cat_dir):
            mkdir(cat_dir)

    print('Continuing in', root, 'from', last_file)
    print('Categories: ', str(categories))
    print('If more categories are needed, please quit add them to progress.txt manually')
    print()

    return root, last_file, categories

last_file = False
if len(sys.argv) == 1:
    # Continue previous session
    root, last_file, categories = load()

output = root + '_out'

files = [f for f in listdir(root)]
num_skipped = 0

# For each lizard file
for file in files:
    if last_file and last_file == file:
        print(f'Already classified {num_skipped} files')
        print('Continuing from previous file...')
        print()
        last_file = False
    elif last_file:
        num_skipped += 1
        continue

    try:
        # Save image in set directory
        # Read RGB image
        img = cv2.imread(join(root, file))

        # Resize the image
        img = cv2.resize(img, (256,256))


        # If we're categorizing, write to category, otherwise default
        if (len(categories) > 0):
            cv2.imshow(file, img)
            category = int(cv2.waitKey(0)) # Wait indefinitely
            if (category == 113 or category == 81): # If q
                print('Saving progress and exiting')
                save_and_quit(file)
            category -= 49 # Get number (49 is ASCII of 1)
            if (category < 0 or category >= len(categories)):
                print('Please use positive indices 1 - #categories')
                print('Program will exit cleanly, so please relaunch!')
                save_and_quit(file)

            cv2.imwrite(join(output + '_' + categories[category], file), img);
        else:
            cv2.imwrite(join(output, file), img);
        img.close()
    except SystemExit as e:
        raise
    except Exception as e:
        print('Image failed to process, continuing...')

print ('Pre-processing complete!')
