from PIL import Image
def convert_png_to_ico(png_path, ico_path):
    image = Image.open(png_path)
    image.save(ico_path, format='ICO')
 # Example usage
png_path = r'C:\Users\EDY\Desktop/test_aaa.png'
ico_path = r'C:\Users\EDY\Desktop/image.ico'
convert_png_to_ico(png_path, ico_path)
