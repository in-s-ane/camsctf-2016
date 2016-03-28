from PIL import Image

width = 360
height = 480

combined = Image.new("RGB", (width, height))
combined_pixels = combined.load()

counter = 0

for x in range(width):
    for y in range(height):
        temp = Image.open("a/%s.png" % counter).convert("RGB")
        combined_pixels[x, y] = (temp.getpixel((0, 0)))
        counter += 1

combined.save("out.png")

# Unzipping the file gives us a ton of png files of just one pixel. Similar to Photo Synthesis 1,
# we need to combine the pixels together to reconstruct the image.

# The code here for brute forcing the resolution isn't here, but to find the correct
# resolution, I tried a bunch of resolutions that multiply to 172800.
# 360x480 is the correct resolution

# {n47ur3}
