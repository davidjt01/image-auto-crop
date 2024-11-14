import os
from PIL import Image

def crop_transparent(image_path, output_path):
    image = Image.open(image_path)
    image = image.convert("RGBA")
    bbox = image.getbbox()
    cropped_image = image.crop(bbox)
    cropped_image.save(output_path, "PNG")

def process_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            crop_transparent(input_path, output_path)
        else:
            print(f"Skipping {filename}: Not a PNG file")

input_folder = "input"
output_folder = "output"
process_folder(input_folder, output_folder)
