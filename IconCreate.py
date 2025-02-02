from PIL import Image
import os

# Variables
IMAGES_FOLDER = 'Images'
SAVE_FOLDER = 'Icons'
EXT = 'ico'

def create_folders():
    # Get current working directory
    cwd = os.getcwd()
    
    # Add folder to cwd
    image_path = os.path.join(cwd, IMAGES_FOLDER)
    save_path = os.path.join(cwd, SAVE_FOLDER)

    # Create folders if they do not exist
    if not os.path.exists(image_path):
        os.mkdir(image_path)
        print(f'Created Folder: {IMAGES_FOLDER}')

    if not os.path.exists(save_path):
        os.mkdir(save_path)
        print(f'Created Folder: {SAVE_FOLDER}')
    
    return (image_path, save_path)

# Iterate through all the images in the images folder and export them as icons within icon folder.
def main(): 
    img_path, save_path = create_folders()

    if len(os.listdir(img_path)) == 0:
        print('No Image Files within folder! ❌\n')
        
    for image in os.listdir(img_path):
        icon_path = os.path.join(img_path, image)
        icon = Image.open(icon_path)
        file_name = image.split('.')[0]
        icon_name = f'{save_path}/{file_name}.{EXT}'
        icon.save(icon_name, format = 'ICO', sizes=[(256, 256)])
        print(f'Icon Created: {icon_name}')
        
if __name__ == '__main__':
    main()