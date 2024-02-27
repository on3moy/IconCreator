from PIL import Image
import os

# Variables
IMAGES = './Images/'
SAVE = './Icons/'
EXT = '.ico'

# Iterate through all the images in the images folder and export them as icons within icon folder.
def main():
    for image in os.listdir(IMAGES):
        icon = Image.open(IMAGES + '/' + image)
        file_name = image.split('.')[0]
        icon.save(SAVE + file_name + EXT, format = 'ICO', sizes=[(256, 256)])
        
if __name__ == '__main__':
    main()