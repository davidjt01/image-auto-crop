import os
from PIL import Image

def crop_transparent(image_path, output_path):
    try:
        image = Image.open(image_path).convert("RGBA")
        bbox = image.getbbox()
        if bbox:
            cropped_image = image.crop(bbox)
        else:
            cropped_image = image
        cropped_image.save(output_path, "PNG")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

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
