# Image to Icon Converter 🦖

This Python script converts images from a specified folder into `.ico` (icon) files and saves them in a separate folder.

## Features
- Automatically creates necessary folders (`Images` and `Icons`) if they don't exist.
- Converts all images in the `Images` folder to `.ico` format.
- Saves the generated icons in the `Icons` folder.
- Supports batch conversion.

## Prerequisites
This script requires Python and the `Pillow` library.

### Install Pillow
```sh
pip install pillow
```

## Usage
1. Place your image files inside the `Images` folder.
2. Run the script:
```sh
python IconCreate.py
```
3. Converted `.ico` files will be saved in the `Icons` folder.

## Script Overview
### Variables
- `IMAGES_FOLDER`: Folder where input images are stored.
- `SAVE_FOLDER`: Folder where output `.ico` files are saved.
- `EXT`: The target format (default: `.ico`).

### Functions
- `create_folders()`: Ensures `Images` and `Icons` directories exist.
- `main()`: Iterates through the images in `Images`, converts them to `.ico`, and saves them in `Icons`.

## Example Output
```sh
Created Folder: Images
Created Folder: Icons
No Image Files within folder! ❌
```
Or if images are present:
```sh
Icon Created: Icons/sample.ico
Icon Created: Icons/logo.ico
```

## Notes
- Ensure the images placed in `Images` are in a compatible format (e.g., PNG, JPG).
- The script generates `.ico` files with a resolution of `256x256`.