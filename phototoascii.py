from PIL import Image
ASCII_CHARS="$@%#*+=-:." #Darker to lighter

path = open("YOUR TXT.txt","w")
image = Image.open("Your Png comes here")
image_gray=image.convert("L")

new_width = 100
aspect_ratio = image.height/image.width
new_height = int(new_width*aspect_ratio*0.58)
image_gray = image_gray.resize((new_width,new_height))


counter = 0
pixels = list(image_gray.getdata())
for pixel in pixels:
    against = int(pixel//28.33)
    char = ASCII_CHARS[against]
    path.write(char)
    counter+=1
    if counter==new_width:
        counter = 0
        path.write("\n")
