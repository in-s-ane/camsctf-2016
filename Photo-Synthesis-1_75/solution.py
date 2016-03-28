from PIL import Image

width = 180
height = 308

img_orig = Image.open("photosynthesis1.png").convert("RGB")
orig_pixels = img_orig.load()

img = Image.new("RGB", (width,height))
pixels = img.load()

counter= 0
for x in range(width):
    for y in range(height):
        pixels[x, y] = orig_pixels[counter, 0]
        counter += 1

img.save("out.png")

# We are given a really long picture 1 pixel tall and 55440 pixels long
# To reconstruct the image, we need to rearrange the the pixels to create
# an image with a proper resolution

# The code here for brute forcing the resolution isn't here, but to find the correct
# resolution, I tried a bunch of resolutions that multiply to 55440.
# 180x308 is the correct resolution

# Read the flag backwards
# {C6H12O6}
