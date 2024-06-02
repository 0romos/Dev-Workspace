import pyautogui
import pyperclip
from PIL import Image


def get_hex_color():
    x, y = pyautogui.position()
    screenshot = pyautogui.screenshot()
    pixel_rgb = screenshot.getpixel((x, y))
    hex_color = '#{:02x}{:02x}{:02x}'.format(pixel_rgb[0], pixel_rgb[1], pixel_rgb[2])
    return hex_color

color = get_hex_color()
pyperclip.copy(color)
print("Pixel color:", color, "(copied to clipboard)")
