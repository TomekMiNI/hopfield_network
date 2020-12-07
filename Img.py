from PIL import Image

def vector_to_img(v, height, width, display):
    img = Image.new( 'RGB', (width, height), "black") # Create a new black image
    pixels = img.load() # Create the pixel map
    for h in range(height):
        for w in range(width):
            if v[h * width + w] == 1:
                pixels[w, h] = (0,0,0)
            else:
                pixels[w, h] = (255,255,255)
    if display:
        img.show()