from PIL import Image

f = open("photosynthesis3.txt", "r").read().strip().split("\n")[1:]

width = 738
height = 108
img = Image.new("RGB", (width,height))
pixels = img.load()

counter = 0

for x in range(width):
    for y in range(height):
        temp = f[counter].strip().split()
        pixels[x, y] = (int(temp[0]), int(temp[1]), int(temp[2]))
        counter += 1

img.save("out.png")

# {4nother_l4m3_fl4g}
