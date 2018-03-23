from PIL import Image

def resize_images(img,path):
	img = Image.open(img)
	out = img.resize((2000, 2000), Image.ANTIALIAS)  # resize image with high-quality
	out.save(path)
