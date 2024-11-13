from PIL import Image

def crop_transparent(image_path, output_path):
    image = Image.open(image_path)
    image = image.convert("RGBA")
    bbox = image.getbbox()
    cropped_image = image.crop(bbox)
    cropped_image.save(output_path, "PNG")

crop_transparent("input.png", "output.png")