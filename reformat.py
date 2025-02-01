from PIL import Image
import os

images = ["beach.bmp", "water.bmp", "sky.bmp"]

for imagePath in images:
    image = Image.open(os.path.join(imagePath))

    if image.mode != 'RGB':
        image = image.convert('RGB')

    bmp_path = imagePath
    image.save(bmp_path, "BMP", quality=100)

    print(f"{bmp_path} processed")