"""
NOTICE: Image and sound files are hosted online for your convenience
===================================================================================

Ducky Clicker 2025
- Created by Zak Richards and Niall Bottomley

This is an evaluation / beta copy of the game with unreleased features.

===================================================================================
MIT License

Copyright (c) 2025 Creative Commons

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
===================================================================================
"""


# Imported modules (Start of code file)
import pygame
import random
import os
import requests
import io
from PIL import Image
from io import BytesIO
from PIL import Image
import urllib3
import threading

pygame.init()
pygame.mixer.init()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def load_image_from_url(url):
    try:
        response = requests.get(url, verify=False, timeout=5)
        response.raise_for_status()
        return pygame.image.load(io.BytesIO(response.content)).convert_alpha()
    except Exception as e:
        print(f"[WARN] Failed to load image from {url}: {e}")
        # create a red placeholder surface
        surf = pygame.Surface((250, 250))
        surf.fill((255, 100, 100))
        return surf


def load_sound_from_url(url):
    try:
        response = requests.get(url, verify=False, timeout=10)
        response.raise_for_status()
        return pygame.mixer.Sound(io.BytesIO(response.content))
    except requests.exceptions.RequestException as e:
        print(f"Failed to load sound from {url}: {e}")
        return None
    except pygame.error as pe:
        print(f"Pygame failed to load sound from {url}: {pe}")
        return None



# IMAGE URLS ONLINE
image_urls = {
    "icon": "https://i.ibb.co/bMZPYs6y/1-Default-Duck.png",
    "duck": "https://i.ibb.co/bMZPYs6y/1-Default-Duck.png",
    "dps1": "https://i.ibb.co/SHZ0Xvh/Dps1.png",
    "dps2": "https://i.ibb.co/wrsv0v5n/Dps2.png",
    "dps3": "https://i.ibb.co/5XcDC1pQ/Dps3.png",
    "dps4": "https://i.ibb.co/8nZB2JJJ/Dps4.jpg",
    "dps5": "https://i.ibb.co/xq5Jf9TH/Dps5.png",
    "defaultduck": "https://i.ibb.co/bMZPYs6y/1-Default-Duck.png",
    "demolitionduck": "https://i.ibb.co/fVDXRJ5c/2-Demolition-Duck.png",
    "dapperduck": "https://i.ibb.co/0y9t559R/3-Dapper-Duck.png",
    "daredevilduck": "https://i.ibb.co/bMZPYs6y/1-Default-Duck.png",
    "donnerduck": "https://i.ibb.co/bMZPYs6y/1-Default-Duck.png",
    "demonduck": "https://i.ibb.co/1GS4Lw9Z/6-Demon-Duck.png"
}
"""
dps_images = {
    "dps1": pygame.transform.scale(load_image_from_url(image_urls["dps1"]), (int(184 * 1.823), int(96 / 3.87))),
    "dps2": pygame.transform.scale(load_image_from_url(image_urls["dps2"]), (int(184 * 1.815), int(96 / 4.04))),
    "dps3": pygame.transform.scale(load_image_from_url(image_urls["dps3"]), (int(184 * 1.578), int(96 / 3.52))),
    "dps4": pygame.transform.scale(load_image_from_url(image_urls["dps4"]), (int(184 / 1.361), int(96 / 7.3))),
    "dps5": pygame.transform.scale(load_image_from_url(image_urls["dps5"]), (int(184 * 3.135), int(96 / 1.755))),
}

# Duck images
duck_images = {
    "default": pygame.transform.scale(load_image_from_url(image_urls["defaultduck"]), (250, 250)),
    "demolition": pygame.transform.scale(load_image_from_url(image_urls["demolitionduck"]), (250, 250)),
    "dapper": pygame.transform.scale(load_image_from_url(image_urls["dapperduck"]), (250, 250)),
    "daredevil": pygame.transform.scale(load_image_from_url(image_urls["daredevilduck"]), (250, 250)),
    "donner": pygame.transform.scale(load_image_from_url(image_urls["donnerduck"]), (250, 250)),
    "demon": pygame.transform.scale(load_image_from_url(image_urls["demonduck"]), (250, 250)),
}
"""

# Load the music
sound_urls = [
    "https://raw.githubusercontent.com/zakr0112/DuckyClicker/main/Source/Music/Symbolism.mp3",
    "https://raw.githubusercontent.com/zakr0112/DuckyClicker/main/Source/Music/Symbolism2.mp3",
    "https://raw.githubusercontent.com/zakr0112/DuckyClicker/main/Source/Music/Symbolism3.mp3"
]

#Game screen creation
screen_width = 1900
screen_height = 950
background_color = (255, 255, 255)
border_color = (0, 0, 255)
border_thickness = 25



# Set the screen size
screen = pygame.display.set_mode((screen_width, screen_height))


# Set the background color to white
screen.fill(background_color)


# Initialize pygame
pygame.display.set_caption("Ducky Clicker | Beta Release 1.8v3 (21/11/2025)")


print("Loading Images... Please Wait")
pygame.display.update()

loading_font = pygame.font.Font(None, 50)
y_offset = 400

def load_image_from_url(url):
    """Load online image with short timeout, no caching, and in-memory only."""
    try:
        response = requests.get(url, verify=False, timeout=5)
        response.raise_for_status()
        return pygame.image.load(io.BytesIO(response.content)).convert_alpha()
    except Exception as e:
        print(f"[WARN] Failed to load image from {url}: {e}")
        # red placeholder surface for missing image
        surf = pygame.Surface((250, 250))
        surf.fill((255, 100, 100))
        return surf

# Initialize image dictionaries
duck_images = {}
dps_images = {}

# Duck list (name, url key)
duck_list = [
    ("default", "defaultduck"),
    ("demolition", "demolitionduck"),
    ("dapper", "dapperduck"),
    ("daredevil", "daredevilduck"),
    ("donner", "donnerduck"),
    ("demon", "demonduck"),
]

# DPS list (name, url key, w_scale, h_scale)
dps_list = [
    ("dps1", "dps1", 1.823, 3.87),
    ("dps2", "dps2", 1.815, 4.04),
    ("dps3", "dps3", 1.578, 3.52),
    ("dps4", "dps4", 1 / 1.361, 7.3),
    ("dps5", "dps5", 3.135, 1.755),
]

# Unified loader for ducks and DPS
for name, key in duck_list + [d[:2] for d in dps_list]:
    text = loading_font.render(f"Loading {name.title()}...", True, (0, 0, 255))
    screen.fill((255, 255, 255))
    screen.blit(text, (screen_width // 2 - 200, y_offset))
    pygame.display.update()
    pygame.event.pump()  # keeps the window responsive

    img = load_image_from_url(image_urls[key])
    if name.startswith("dps"):
        # find its scaling info
        _, _, w_scale, h_scale = next(d for d in dps_list if d[0] == name)
        new_w = int(img.get_width() * w_scale)
        new_h = int(img.get_height() / h_scale)
        img = pygame.transform.scale(img, (new_w, new_h))
        dps_images[name] = img
    else:
        img = pygame.transform.scale(img, (250, 250))
        duck_images[name] = img

    y_offset += 50

print("All images loaded into memory successfully!")



# --- Scale and position all DPS images once, after image loading ---
dps1_img = dps_images["dps1"]
dps1_img = pygame.transform.scale(dps1_img, (int(dps1_img.get_width() * 1.823), int(dps1_img.get_height() / 3.87)))
dps1_rect = dps1_img.get_rect(center=(1230, 75))

dps2_img = dps_images["dps2"]
dps2_img = pygame.transform.scale(dps2_img, (int(dps2_img.get_width() * 1.815), int(dps2_img.get_height() / 4.04)))
dps2_rect = dps2_img.get_rect(center=(1230, 178))

dps3_img = dps_images["dps3"]
dps3_img = pygame.transform.scale(dps3_img, (int(dps3_img.get_width() * 1.578), int(dps3_img.get_height() / 3.52)))
dps3_rect = dps3_img.get_rect(center=(1230, 278))

dps4_img = dps_images["dps4"]
dps4_img = pygame.transform.scale(dps4_img, (int(dps4_img.get_width() / 1.361), int(dps4_img.get_height() / 7.3)))
dps4_rect = dps4_img.get_rect(center=(1230, 378))

dps5_img = dps_images["dps5"]
dps5_img = pygame.transform.scale(dps5_img, (int(dps5_img.get_width() * 3.135), int(dps5_img.get_height() / 1.755)))
dps5_rect = dps5_img.get_rect(center=(1230, 477))

# --- Scale and position all Duck images once ---
default_duck_img = pygame.transform.scale(duck_images["default"], (250, 250))
demolition_duck_img = pygame.transform.scale(duck_images["demolition"], (250, 250))
dapper_duck_img = pygame.transform.scale(duck_images["dapper"], (250, 250))
daredevil_duck_img = pygame.transform.scale(duck_images["daredevil"], (250, 250))
donner_duck_img = pygame.transform.scale(duck_images["donner"], (250, 250))
demon_duck_img = pygame.transform.scale(duck_images["demon"], (250, 250))

# --- Set default duck image/rect for the start ---
duck_img = default_duck_img
duck_rect = duck_img.get_rect(center=(375, 525))




# --- Set icon ---
if "default" in duck_images:
    pygame.display.set_icon(duck_images["default"])


pygame.display.set_icon(duck_images["default"])

sounds = []
for url in sound_urls:
    snd = load_sound_from_url(url)
    if snd:
        sounds.append(snd)

# play background music
if sounds:
    sounds[0].play(-1)


# Set Scores and Balances
Ducks = 0
Gold = 0
click_power = 1
dps1_upgrade_cost = 100
dps1_original_upgrade_cost = 100
dps2_upgrade_cost = 1500
dps2_original_upgrade_cost = 1500
dps2_upgrade_clicks = 0
dps3_upgrade_cost = 30000
dps3_original_upgrade_cost = 30000
dps3_upgrade_clicks = 0
dps4_upgrade_cost = 750000
dps4_original_upgrade_cost = 750000
dps4_upgrade_clicks = 0
dps5_upgrade_cost = 22500000
dps5_original_upgrade_cost = 22500000
dps5_upgrade_clicks = 0
current_gold_increase_factor = 0
last_gold_increase = 0
last_gold_increase_factor = 0

# Load the duck image
#duck_img = load_image_from_url(image_urls["duck"])
#duck_rect = duck_img.get_rect(center=(0, 0))



sounds = []
for url in sound_urls:
    snd = load_sound_from_url(url)
    if snd:
        sounds.append(snd)


# DPS Images
#dps1_img = load_image_from_url(image_urls["dps1"])
#dps1_rect = dps1_img.get_rect(center=(0, 0))
#dps2_img = load_image_from_url(image_urls["dps2"])
#dps2_rect = dps2_img.get_rect(center=(0, 0))
#dps3_img = load_image_from_url(image_urls["dps3"])
#dps3_rect = dps3_img.get_rect(center=(0, 0))
#dps4_img = load_image_from_url(image_urls["dps4"])
#dps4_rect = dps4_img.get_rect(center=(0, 0))
#dps5_img = load_image_from_url(image_urls["dps5"])
#dps5_rect = dps5_img.get_rect(center=(0, 0))


# Define the font for the score text
font = pygame.font.Font(None, 30)


# Upgrade Buttons
dps1_upgrade_cost == Gold + 1
dps1_upgrade_x = 1705  # Moves Box Horizontally
dps1_upgrade_y = 77  # Moves Box Vertically
dps1_upgrade_w = 170  # Increases Box Width
dps1_upgrade_h = 48  # Increases Box Height
dps1_upgrade_rect = pygame.Rect(dps1_upgrade_x, dps1_upgrade_y, dps1_upgrade_w, dps1_upgrade_h)
if Gold >= dps1_upgrade_cost:
    Gold -= dps1_upgrade_cost
    dps1_upgrade_cost = dps1_upgrade_cost + dps1_original_upgrade_cost  # Increase the cost for the next upgrade
    click_power == click_power + 1

dps2_upgrade_cost == Gold + 1500
dps2_upgrade_x = 1705  # Moves Box Horizontally
dps2_upgrade_y = 180  # Moves Box Vertically
dps2_upgrade_w = 170  # Increases Box Width
dps2_upgrade_h = 45  # Increases Box Height
dps2_upgrade_rect = pygame.Rect(dps2_upgrade_x, dps2_upgrade_y, dps2_upgrade_w, dps2_upgrade_h)
if Gold >= dps2_upgrade_cost:
    Gold -= dps2_upgrade_cost
    dps2_upgrade_cost = dps2_upgrade_cost + dps2_original_upgrade_cost  # Increase the cost for the next upgrade

dps3_upgrade_cost == Gold + 30000
dps3_upgrade_x = 1705  # Moves Box Horizontally
dps3_upgrade_y = 280  # Moves Box Vertically
dps3_upgrade_w = 170  # Increases Box Width
dps3_upgrade_h = 45  # Increases Box Height
dps3_upgrade_rect = pygame.Rect(dps3_upgrade_x, dps3_upgrade_y, dps3_upgrade_w, dps3_upgrade_h)
if Gold >= dps3_upgrade_cost:
    Gold -= dps3_upgrade_cost
    dps3_upgrade_cost = dps3_upgrade_cost + dps3_original_upgrade_cost  # Increase the cost for the next upgrade

dps4_upgrade_cost == Gold + 750000
dps4_upgrade_x = 1705  # Moves Box Horizontally
dps4_upgrade_y = 380  # Moves Box Vertically
dps4_upgrade_w = 170  # Increases Box Width
dps4_upgrade_h = 45  # Increases Box Height
dps4_upgrade_rect = pygame.Rect(dps4_upgrade_x, dps4_upgrade_y, dps4_upgrade_w, dps4_upgrade_h)
if Gold >= dps4_upgrade_cost:
    Gold -= dps4_upgrade_cost
    dps4_upgrade_cost = dps4_upgrade_cost + dps4_original_upgrade_cost  # Increase the cost for the next upgrade

dps5_upgrade_cost == Gold + 22500000
dps5_upgrade_x = 1705  # Moves Box Horizontally
dps5_upgrade_y = 480  # Moves Box Vertically
dps5_upgrade_w = 170  # Increases Box Width
dps5_upgrade_h = 45  # Increases Box Height
dps5_upgrade_rect = pygame.Rect(dps5_upgrade_x, dps5_upgrade_y, dps5_upgrade_w, dps5_upgrade_h)
if Gold >= dps5_upgrade_cost:
    Gold -= dps5_upgrade_cost
    dps5_upgrade_cost = dps5_upgrade_cost + dps5_original_upgrade_cost  # Increase the cost for the next upgrade


# Example: Play first sound
#sounds[0].play()



#loading screen
def show_loading_screen():
    clock = pygame.time.Clock()
    loading_font_size = 120
    loading_font = pygame.font.Font(None, loading_font_size)

    small_font_size = 35
    small_font = pygame.font.Font(None, small_font_size)

    loading_text = loading_font.render("PRE-RELEASE BETA VERSION", True, (255, 0, 0))
    loading_rect = loading_text.get_rect(center=(screen_width // 2, screen_height // 2))

    loading_credits = loading_font.render("Ducky Clicker", True, (0, 0, 255))
    loading_rect2 = loading_text.get_rect(center=(screen_width // 1.5, screen_height // 3))

    loading_smalltext = small_font.render("Created by Zak & Niall", True, (0, 0, 255))
    loading_rect3 = loading_smalltext.get_rect(center=(screen_width // 2, screen_height // 1.05))


    screen.fill((255, 255, 255))  # Fill the screen with white
    screen.blit(loading_text, loading_rect)
    screen.blit(loading_credits, loading_rect2)
    screen.blit(loading_smalltext, loading_rect3)
    pygame.display.update()
    print()
    print("========================================")
    print("Thank you for downloading Ducky Clicker!")
    print("a copy of the License is provided at the")
    print("top of the python file")
    print()
    print("This is a WIP and there are bugs with this")
    print("current build as we have switched from local")
    print("Image and music files, to online hosted ones")
    print("to make this a one-file game!")
    print()
    print()
    print("Game Details:")
    print("Beta Release: 1.8v4")
    print("Date of release: 24/11/2025")
    print("Provider: Github (releases beta 1.8v4)")
    print("RELEASED VIA GIT RELEASES")
    print("========================================")
    print()
    pygame.time.wait(8500)  # Display "Starting!" for 8.5 seconds


#running the game loop
running = True
dps2_increase_time = pygame.time.get_ticks()
dps3_increase_time = pygame.time.get_ticks()
dps4_increase_time = pygame.time.get_ticks()
dps5_increase_time = pygame.time.get_ticks()
show_loading_screen()
clock = pygame.time.Clock()
duck_img = duck_images["default"]
duck_rect = duck_img.get_rect(center=(375, 525))

while running:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            # Check if the duck image is clicked
            if duck_rect.collidepoint(pos):
                Ducks += click_power
                if Ducks >= 10:
                    gold_increase = (Ducks // 10) - (last_gold_increase // 10)
                    if gold_increase > 0:
                        Gold += gold_increase
                        last_gold_increase = Ducks


            if dps1_upgrade_rect.collidepoint(pos):
                if Gold >= dps1_upgrade_cost:
                    Gold -= dps1_upgrade_cost
                    click_power += 100
                    dps1_upgrade_cost = dps1_upgrade_cost + dps1_original_upgrade_cost

            if dps2_upgrade_rect.collidepoint(pos):
                if Gold >= dps2_upgrade_cost:
                    Gold -= dps2_upgrade_cost
                    dps2_upgrade_cost = dps2_upgrade_cost + dps2_original_upgrade_cost
                    dps2_upgrade_clicks += 1

            if dps3_upgrade_rect.collidepoint(pos):
                if Gold >= dps3_upgrade_cost:
                    Gold -= dps3_upgrade_cost
                    dps3_upgrade_cost = dps3_upgrade_cost + dps3_original_upgrade_cost
                    dps3_upgrade_clicks += 1

            if dps4_upgrade_rect.collidepoint(pos):
                if Gold >= dps4_upgrade_cost:
                    Gold -= dps4_upgrade_cost
                    dps4_upgrade_cost = dps4_upgrade_cost + dps4_original_upgrade_cost
                    dps4_upgrade_clicks += 1

            if dps5_upgrade_rect.collidepoint(pos):
                if Gold >= dps5_upgrade_cost:
                    Gold -= dps5_upgrade_cost
                    dps5_upgrade_cost = dps5_upgrade_cost + dps5_original_upgrade_cost
                    dps5_upgrade_clicks += 1


    # Fill the screen with white to clear previous score
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, border_color, (0, 0, screen_width / 2.5, screen_height), border_thickness)
    pygame.draw.rect(screen, border_color, (0, 0, screen_width, screen_height), border_thickness)
    pygame.draw.rect(screen, border_color, (735, 125, screen_width / 1.25, screen_height), border_thickness - 20)
    pygame.draw.rect(screen, border_color, (735, 225, screen_width / 1.25, screen_height), border_thickness - 20)
    pygame.draw.rect(screen, border_color, (735, 325, screen_width / 1.25, screen_height), border_thickness - 20)
    pygame.draw.rect(screen, border_color, (735, 425, screen_width / 1.25, screen_height), border_thickness - 20)
    pygame.draw.rect(screen, border_color, (735, 525, screen_width / 1.25, screen_height), border_thickness - 20)
    pygame.draw.rect(screen, border_color, (735, 625, screen_width / 1.25, screen_height), border_thickness - 20)
    pygame.draw.rect(screen, border_color, (735, 725, screen_width / 1.25, screen_height), border_thickness - 20)
    pygame.draw.rect(screen, border_color, (735, 825, screen_width / 1.25, screen_height), border_thickness - 20)
    pygame.draw.rect(screen, border_color, (735, 925, screen_width / 1.25, screen_height), border_thickness - 20)
    pygame.draw.rect(screen, border_color, (1700, 0, screen_width / 1.25, screen_height), border_thickness - 20)
    pygame.draw.rect(screen, border_color, (1700, 73.5, screen_width / 1.25, screen_height), border_thickness - 20)
    pygame.draw.rect(screen, border_color, (1700, 175.5, screen_width / 1.25, screen_height), border_thickness - 20)
    pygame.draw.rect(screen, border_color, (1700, 275.5, screen_width / 1.25, screen_height), border_thickness - 20)
    pygame.draw.rect(screen, border_color, (1700, 375.5, screen_width / 1.25, screen_height), border_thickness - 20)
    pygame.draw.rect(screen, border_color, (1700, 475.5, screen_width / 1.25, screen_height), border_thickness - 20)
    pygame.draw.rect(screen, border_color, (1700, 575.5, screen_width / 1.25, screen_height), border_thickness - 20)
    pygame.draw.rect(screen, border_color, (1700, 675.5, screen_width / 1.25, screen_height), border_thickness - 20)
    pygame.draw.rect(screen, border_color, (1700, 775.5, screen_width / 1.25, screen_height), border_thickness - 20)
    pygame.draw.rect(screen, border_color, (1700, 875.5, screen_width / 1.25, screen_height), border_thickness - 20)


    # Display the Images
    screen.blit(duck_img, duck_rect)
    screen.blit(dps1_img, dps1_rect)
    screen.blit(dps2_img, dps2_rect)
    screen.blit(dps3_img, dps3_rect)
    screen.blit(dps4_img, dps4_rect)
    screen.blit(dps5_img, dps5_rect)


    # Font Sizes
    Ducks_font_size = 50  # Number of Ducks font size
    Gold_font_size = 50  # Number of Gold font size
    Duck_name_font_size = 50  # Name of Ducks font size
    dps1_upgrade_font_size = 20  # Name of Upgrades
    dps2_upgrade_font_size = 20  # Name of Upgrades
    dps3_upgrade_font_size = 20  # Name of Upgrades
    dps4_upgrade_font_size = 20  # Name of Upgrades
    dps5_upgrade_font_size = 20  # Name of Upgrades


    # Create font objects with their respective sizes
    Ducks_font = pygame.font.Font(None, Ducks_font_size)
    Gold_font = pygame.font.Font(None, Gold_font_size)
    Duck_name_font = pygame.font.Font(None, Duck_name_font_size)
    dps1_upgrade_font = pygame.font.Font(None, dps1_upgrade_font_size)
    dps2_upgrade_font = pygame.font.Font(None, dps2_upgrade_font_size)
    dps3_upgrade_font = pygame.font.Font(None, dps3_upgrade_font_size)
    dps4_upgrade_font = pygame.font.Font(None, dps4_upgrade_font_size)
    dps5_upgrade_font = pygame.font.Font(None, dps5_upgrade_font_size)


    # Load the DPS Images within their respective areas
    dps1_img = dps_images["dps1"]
    dps1_img = pygame.transform.scale(dps1_img, (int(dps1_img.get_width() * 1), int(dps1_img.get_height() / 3.87)))

    dps1_rect = dps1_img.get_rect(center=(1230, 75))
    formatted_dps1_upgrade_cost = "{:,}".format(dps1_upgrade_cost)
    pygame.draw.rect(screen, (255, 255, 0), dps1_upgrade_rect)
    dps1_upgrade_text = dps1_upgrade_font.render(f"Gold Cost: ({formatted_dps1_upgrade_cost})", True, (0, 0, 255))
    dps1_upgrade_text_rect = dps1_upgrade_text.get_rect(center=(dps1_upgrade_w + dps1_upgrade_x, dps1_upgrade_y + dps1_upgrade_h))
    screen.blit(dps1_upgrade_text, (1720, 95))

    dps2_img = dps_images["dps2"]
    dps2_img = pygame.transform.scale(dps2_img, (int(dps2_img.get_width() * 1), int(dps2_img.get_height() / 4.04)))

    dps2_rect = dps2_img.get_rect(center=(1230, 178))
    formatted_dps2_upgrade_cost = "{:,}".format(dps2_upgrade_cost)
    pygame.draw.rect(screen, (255, 255, 0), dps2_upgrade_rect)
    dps2_upgrade_text = dps2_upgrade_font.render(f"Gold Cost: ({formatted_dps2_upgrade_cost})", True, (0, 0, 255))
    dps2_upgrade_text_rect = dps2_upgrade_text.get_rect(center=(dps2_upgrade_w + dps2_upgrade_x, dps2_upgrade_y + dps2_upgrade_h))
    screen.blit(dps2_upgrade_text, (1720, 200))

    dps3_img = dps_images["dps3"]
    dps3_img = pygame.transform.scale(dps3_img, (int(dps3_img.get_width() * 1), int(dps3_img.get_height() / 3.52)))

    dps3_rect = dps3_img.get_rect(center=(1230, 278))
    formatted_dps3_upgrade_cost = "{:,}".format(dps3_upgrade_cost)
    pygame.draw.rect(screen, (255, 255, 0), dps3_upgrade_rect)
    dps3_upgrade_text = dps3_upgrade_font.render(f"Gold Cost: ({formatted_dps3_upgrade_cost})", True, (0, 0, 255))
    dps3_upgrade_text_rect = dps3_upgrade_text.get_rect(center=(dps3_upgrade_w + dps3_upgrade_x, dps3_upgrade_y + dps3_upgrade_h))
    screen.blit(dps3_upgrade_text, (1720, 300))

    dps4_img = dps_images["dps4"]
    dps4_img = pygame.transform.scale(dps4_img, (int(dps4_img.get_width() / 1), int(dps4_img.get_height() / 7.3)))

    dps4_rect = dps4_img.get_rect(center=(1230, 378))
    formatted_dps4_upgrade_cost = "{:,}".format(dps4_upgrade_cost)
    pygame.draw.rect(screen, (255, 255, 0), dps4_upgrade_rect)
    dps4_upgrade_text = dps4_upgrade_font.render(f"Gold Cost: ({formatted_dps4_upgrade_cost})", True, (0, 0, 255))
    dps4_upgrade_text_rect = dps4_upgrade_text.get_rect(center=(dps4_upgrade_w + dps4_upgrade_x, dps4_upgrade_y + dps4_upgrade_h))
    screen.blit(dps4_upgrade_text, (1720, 400))

    dps5_img = dps_images["dps5"]
    dps5_img = pygame.transform.scale(dps5_img, (int(dps5_img.get_width() * 1), int(dps5_img.get_height() / 1.755)))

    dps5_rect = dps5_img.get_rect(center=(1230, 477))
    formatted_dps5_upgrade_cost = "{:,}".format(dps5_upgrade_cost)
    pygame.draw.rect(screen, (255, 255, 0), dps5_upgrade_rect)
    dps5_upgrade_text = dps5_upgrade_font.render(f"Gold Cost: ({formatted_dps5_upgrade_cost})", True, (0, 0, 255))
    dps5_upgrade_text_rect = dps5_upgrade_text.get_rect(center=(dps5_upgrade_w + dps5_upgrade_x, dps5_upgrade_y + dps5_upgrade_h))
    screen.blit(dps5_upgrade_text, (1720, 500))

    # Load the duck images and resize them
    #default_duck_img = duck_images["default"]
    #default_duck_img = pygame.transform.scale(default_duck_img, (int(default_duck_img.get_width() * 2.5), int(default_duck_img.get_height() * 2.5)))

    #demolition_duck_img = duck_images["demolition"]
    #demolition_duck_img = pygame.transform.scale(demolition_duck_img, (int(demolition_duck_img.get_width() * 2.5), int(demolition_duck_img.get_height() * 2.5)))

    #dapper_duck_img = duck_images["dapper"]
    #dapper_duck_img = pygame.transform.scale(dapper_duck_img, (int(dapper_duck_img.get_width() * 2.5), int(dapper_duck_img.get_height() * 2.5)))

    #daredevil_duck_img = duck_images["daredevil"]
    #daredevil_duck_img = pygame.transform.scale(daredevil_duck_img, (int(daredevil_duck_img.get_width() * 2.5), int(daredevil_duck_img.get_height() * 2.5)))

    #donner_duck_img = duck_images["donner"]
    #donner_duck_img = pygame.transform.scale(donner_duck_img, (int(donner_duck_img.get_width() * 2.5), int(donner_duck_img.get_height() * 2.5)))

    #demon_duck_img = duck_images["demon"]
    #demon_duck_img = pygame.transform.scale(demon_duck_img, (int(demon_duck_img.get_width() * 2.5), int(demon_duck_img.get_height() * 2.5)))


    # Load the duck image based on the score
    if Ducks >= 0 and Ducks < 9999:
        duck_img = default_duck_img
        duck_rect = duck_img.get_rect(center=(375, 525))
        Duck_text = Duck_name_font.render("Current Duck - Default Duck!", True, (80, 42, 255))
        Duck_rect = Duck_text.get_rect(center=(265, 800))
        screen.blit(Duck_text, Duck_rect)

    if Ducks >= 10000 and Ducks < 999999:
        duck_img = demolition_duck_img
        duck_rect = duck_img.get_rect(center=(375, 525))
        Duck_text = Duck_name_font.render("Current Duck - Demolition Duck!", True, (80, 42, 255))
        Duck_rect = Duck_text.get_rect(center=(296, 800))
        screen.blit(Duck_text, Duck_rect)

    if Ducks >= 1000000 and Ducks < 99999999:
        duck_img = dapper_duck_img
        duck_rect = duck_img.get_rect(center=(375, 525))
        Duck_text = Duck_name_font.render("Current Duck - Dapper Duck!", True, (80, 42, 255))
        Duck_rect = Duck_text.get_rect(center=(268, 800))
        screen.blit(Duck_text, Duck_rect)

    if Ducks >= 100000000 and Ducks < 9999999999:
        duck_img = daredevil_duck_img
        duck_rect = duck_img.get_rect(center=(375, 525))
        Duck_text = Duck_name_font.render("Current Duck - Daredevil Duck!", True, (80, 42, 255))
        Duck_rect = Duck_text.get_rect(center=(285, 800))
        screen.blit(Duck_text, Duck_rect)

    if Ducks >= 10000000000 and Ducks < 999999999999:
        duck_img = donner_duck_img
        duck_rect = duck_img.get_rect(center=(375, 525))
        Duck_text = Duck_name_font.render("Current Duck - Donner Duck!", True, (80, 42, 255))
        Duck_rect = Duck_text.get_rect(center=(266, 800))
        screen.blit(Duck_text, Duck_rect)

    if Ducks >= 1000000000000 and Ducks < 99999999999999:
        duck_img = demon_duck_img
        duck_rect = duck_img.get_rect(center=(375, 525))
        Duck_text = Duck_name_font.render("Current Duck - Demon Duck!", True, (80, 42, 255))
        Duck_rect = Duck_text.get_rect(center=(264, 800))
        screen.blit(Duck_text, Duck_rect)


    # DPS score - Ducks Per Second Added Automatically
    if dps2_upgrade_clicks >= 1:
        if current_time - dps2_increase_time >= 1000:
            Ducks += 5 * dps2_upgrade_clicks
            dps2_increase_time = current_time

            current_gold_increase_factor = (Ducks // 10) - (last_gold_increase // 10)
            if current_gold_increase_factor >= last_gold_increase_factor:
                gold_increase = current_gold_increase_factor - last_gold_increase_factor
                Gold += gold_increase
                last_gold_increase_factor = current_gold_increase_factor

    if dps3_upgrade_clicks >= 1:
        if current_time - dps3_increase_time >= 1000:
            Ducks += 50 * dps3_upgrade_clicks
            dps3_increase_time = current_time

            current_gold_increase_factor = (Ducks // 10) - (last_gold_increase // 10)
            if current_gold_increase_factor >= last_gold_increase_factor:
                gold_increase = current_gold_increase_factor - last_gold_increase_factor
                Gold += gold_increase
                last_gold_increase_factor = current_gold_increase_factor

    if dps4_upgrade_clicks >= 1:
        if current_time - dps4_increase_time >= 1000:
            Ducks += 250 * dps4_upgrade_clicks
            dps4_increase_time = current_time

            current_gold_increase_factor = (Ducks // 10) - (last_gold_increase // 10)
            if current_gold_increase_factor >= last_gold_increase_factor:
                gold_increase = current_gold_increase_factor - last_gold_increase_factor
                Gold += gold_increase
                last_gold_increase_factor = current_gold_increase_factor

    if dps5_upgrade_clicks >= 1:
        if current_time - dps5_increase_time >= 1000:
            Ducks += 2500 * dps5_upgrade_clicks
            dps5_increase_time = current_time

            current_gold_increase_factor = (Ducks // 10) - (last_gold_increase // 10)
            if current_gold_increase_factor >= last_gold_increase_factor:
                gold_increase = current_gold_increase_factor - last_gold_increase_factor
                Gold += gold_increase
                last_gold_increase_factor = current_gold_increase_factor


    # Display the score
    formatted_Ducks = "{:,.0f}".format(Ducks) if Ducks == int(Ducks) else "{:,.2f}".format(Ducks).rstrip('0').rstrip('.')
    Ducks_text = Ducks_font.render(f"Ducks: {formatted_Ducks}", True, (80, 42, 255))
    Ducks_rect = Ducks_text.get_rect(center=(375, 175))  # Centered under the song choice buttons
    screen.blit(Ducks_text, Ducks_rect, )

    formatted_Gold = "{:,}".format(Gold)
    Gold_text = Gold_font.render(f"Gold: {formatted_Gold}", True, (80, 42, 255))
    Gold_rect = Gold_text.get_rect(center=(375, 225))  # Centered under the song choice buttons
    screen.blit(Gold_text, Gold_rect, )


    # Update the screen
    pygame.display.update()
    clock.tick(60)


# Quit pygame
pygame.quit()
