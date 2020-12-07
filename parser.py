from PIL import Image
import csv
# from IPython.display import display

with open('SN_projekt3/animals-14x9.csv', newline='') as csvfile:
    #reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    reader = csv.reader(csvfile)
    width = 9
    height = 14
    for row in reader:
        img = Image.new( 'RGB', (width, height), "black") # Create a new black image
        pixels = img.load() # Create the pixel map
        for h in range(height):
            for w in range(width):
                if row[h * width + w] == '-1':
                    pixels[w, h] = (255,255,255)
                else:
                    pixels[w, h] = (0,0,0)
        img.show()
        # display(img)


    
    # for i in range(img.size[0]):    # For every pixel:
    #     for j in range(img.size[1]):
    #         pixels[i,j] = (i, j, 100) # Set the colour accordingly
