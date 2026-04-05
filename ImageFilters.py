# Lab 9 – Image Processing
# Name:Gavin Grow
# Date:4/5/26
# Assignment:Image Filters

from PIL import Image


def swapGreenBlue(img):
    """Swap the green and blue values for every pixel in the image."""
    
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            pixel = pixels[x, y]
            if len(pixel) == 4:
                red, green, blue, alpha = pixel
                pixels[x, y] = (red, blue, green, alpha)
            else:
                red, green, blue = pixel
                pixels[x, y] = (red, blue, green)

    img.save("swapGB.png")


def darken(img, amount):
    """Darken the image by reducing RGB values by the given amount."""
    
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            pixel = pixels[x, y]
            if len(pixel) == 4:
                red, green, blue, alpha = pixel
                red = max(red - amount, 0)
                green = max(green - amount, 0)
                blue = max(blue - amount, 0)
                pixels[x, y] = (red, green, blue, alpha)
            else:
                red, green, blue = pixel
                red = max(red - amount, 0)
                green = max(green - amount, 0)
                blue = max(blue - amount, 0)
                pixels[x, y] = (red, green, blue)

    img.save("darkImg.png")


def bwFilter(img):
    """Example function: converts image to grayscale."""
    
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            red, green, blue = pixels[x, y]
            avg = (red + green + blue) // 3
            pixels[x, y] = (avg, avg, avg)

    img.save("bwImg.png")


def main():
    # Open the image file
    source = "durango.png"

    # Generate swapGB.png from the original image
    swapGreenBlue(Image.open(source))

    # Generate darkImg.png from the original image
    darken(Image.open(source), 80)

    # Example (already completed)
    # bwFilter(Image.open(source))


if __name__ == "__main__":
    main()
