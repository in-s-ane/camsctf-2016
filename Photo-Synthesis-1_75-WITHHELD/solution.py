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

# Read the flag backwards
# {C6H1206}
