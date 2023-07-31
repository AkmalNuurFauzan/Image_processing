from PIL import Image

img = Image.open("lenna.png")

p_map = img.load()

w, h = img.size

for i in range(0,128):
    for j in range(h):
        r, g, b = img.getpixel((i, j))
        gs = (0.299*r + 0.587*g + 0.114*b)
        # p_map[i, j] = (int(gs), int(gs), int(gs))
        p_map[i,j] = (255, g, b)

for i in range(128, 256):
    for j in range(h):
        r, g, b = img.getpixel((i, j))
        gs = (0.299*r + 0.587*g + 0.114*b)
        # p_map[i, j] = (int(gs), int(gs), int(gs))
        p_map[i,j] = (r, g, 255)

for i in range(256,384):
    for j in range(h):
        r, g, b = img.getpixel((i, j))
        gs = (0.299*r + 0.587*g + 0.114*b)
        # p_map[i, j] = (int(gs), int(gs), int(gs))
        p_map[i,j] = (r, 255, b)

for i in range(384,512):
    for j in range(h):
        r, g, b = img.getpixel((i, j))
        gs = (0.299*r + 0.587*g + 0.114*b)
        # p_map[i, j] = (int(gs), int(gs), int(gs))
        p_map[i,j] = (r, g, b)

img.save("sesudah", format="png")

img.show()