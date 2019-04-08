# DinoLizard

## Preprocessing Images
### Setup
Install OpenCV2: `pip3 install opencv-python`

### Running
Run the program: `python3 preprocess.py IMAGE_FOLDER CATEGORY_1 CATEGORY_2`
Go to the open image, and press 1 or 2 (up to 9 categories possible) and it will save a standard-size (256x256px) version into the folder `{IMAGE_FOLDER}_out_{CATEGORY_x}`
At any time, press `q` to exit the program and save your progress

To continue an existing task (you can't have multiple active at once!):
Simply run `python3 preprocess.py` and it will continue from the image you last quit on.
You can manually add additional categories in the `progress.txt` file

