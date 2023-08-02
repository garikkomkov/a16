# Открываем файл со скриншотом и обрезаем его так, чтобы отсечь лишнюю информацию
# Importing Image class from PIL module
from PIL import Image
import os
 
# Opens a image in RGB mode
im = Image.open(r"wall-35911547_508056.jpg")
 
 # Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size

# Setting the points for cropped image for tags

x1 = 647
y1 = 67
x2 = x1+(width-1350)
y2 = y1+(height-150)

#543 4233

#right = left+width
#lower = upper+height
 
# Cropped image of above dimension
# (It will not change original image)
im1 = im.crop((x1, y1, x2, y2))
 
# Shows the image in image viewer
#im1.show()
if (os.path.exists("osa_cr.jpg")):
        os.remove("osa_cr.jpg")
im1.save("osa_cr.jpg", "JPEG")