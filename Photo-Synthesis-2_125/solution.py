from PIL import Image

width, height = (360, 480)

combined = Image.new("RGB", (width, height))
combined_pixels = combined.load()

counter = 0

for x in range(width):
    for y in range(height):
        temp = Image.open("a/%s.png" % counter).convert("RGB")
        combined_pixels[x, y] = (temp.getpixel((0, 0)))
        counter += 1

combined.save("out.png")

# {n47ur3}
