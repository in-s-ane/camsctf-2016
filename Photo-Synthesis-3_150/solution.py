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

# We are given a bunch of rgb values, and like the previous Photo Synthesis problems, we need to reconstruct
# the picture using the rgb values.

# The code here for brute forcing the resolution isn't here, but to find the correct
# resolution, I tried a bunch of resolutions that multiply to 79704.
# 738x108 is the correct resolution

# {4nother_l4m3_fl4g}
