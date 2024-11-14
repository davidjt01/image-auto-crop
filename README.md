# Image auto crop
Simple Python script which takes all png images in an input folder and crops out transparent areas and saves all cropped images in an output folder. Output folder is automatically created if it does not exist.

Main usage would be for cropping sprites or assets for web or app development.

## Requirements
* Python
* Pillow library

Install Pillow using:
```
pip install pillow
```

## Usage
1. Download or clone the repository in your chosen directory.
2. Create a new folder in the same directory and name it "input".
3. Place all the images to be cropped in the "input" folder.
4. Run the script using:
    ```
    python image_auto_crop.py
    ```
5. All images will be cropped and saved in the folder "output" which will be created if it does not exist.
