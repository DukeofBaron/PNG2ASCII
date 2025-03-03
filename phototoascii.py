from PIL import Image
ASCII_CHARS="$@%#*+=-:." #Darker to lighter

path = open("YOUR TXT.txt","w")
image = Image.open("Your Png comes here")
image_gray=image.convert("L")

new_width = 100
aspect_ratio = image.height/image.width
new_height = int(new_width*aspect_ratio*0.58)
image_gray = image_gray.resize((new_width,new_height))


sayac = 0
pixels = list(image_gray.getdata())
for pixel in pixels:
    against = int(pixel//28.33)
    karakter = ASCII_CHARS[against]
    path.write(karakter)
    sayac+=1
    if sayac==new_width:
        sayac = 0
        path.write("\n")
