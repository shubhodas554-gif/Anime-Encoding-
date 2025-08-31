import cv2, os, random, asyncio
from PIL import Image, ImageOps, ImageFilter, ImageDraw, ImageFont
from string import ascii_uppercase, digits
import requests
from bs4 import BeautifulSoup as bs
from config import CHANNEL_TITLE

async def get_cover(id):
    try:
        url = f"https://anilist.co/anime/{id}"
        r = requests.get(url).content
        soup = bs(r, "html.parser")
        img = soup.find("img", "cover").get("src")
        r = requests.get(img).content
        fname = "./" + "".join(random.choices(ascii_uppercase + digits, k=10)) + ".jpg"
        with open(fname, "wb") as f:
            f.write(r)
        return fname
    except:
        await asyncio.sleep(2)
        return "assets/c4UUTC4DAe.jpg"

def get_screenshot(file):
    cap = cv2.VideoCapture(file)
    name = "./" + "".join(random.choices(ascii_uppercase + digits, k=10)) + ".jpg"
    total_frames = round(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    frame_num = random.randint(0, total_frames)
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num - 1)
    res, frame = cap.read()
    cv2.imwrite(name, frame)
    cap.release()
    return name

def make_col():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
