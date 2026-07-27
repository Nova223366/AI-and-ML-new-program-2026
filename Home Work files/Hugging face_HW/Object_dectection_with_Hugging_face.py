import os, io, time, random, requests, mimetypes
from datetime import datetime
from PIL import image, ImageDraw, ImageFont
#from config import HF_API_KEY

MODEL = "facebook/detr-resnet-50"

API = f"https://router.huggingface.co/hf-inference/model/{MODEL}"

ALLOWED, MAX_MB = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp", ".tiff"}, 8

MOJI = {"person":"🧍","car":"🚗","truck":"🚚","bus":"🚌","bicycle":"🚲","motorcycle":"🏍️","dog":"🐶","cat":"🐱",

"bird":"🐦","horse":"🐴","sheep":"🐑","cow":"🐮","bear":"🐻","giraffe":"🦒","zebra":"🦓","banana":"🍌",

"apple":"🍎","orange":"🍊","pizza":"🍕","broccoli":"🥦","book":"📘","laptop":"💻","tv":"📺","bottle":"🧴","cup":"🥤"}

def font(sz=18):
    for f in ("DejaVuSans.ttf", "arial.ttf"):
        try: return ImageFont.truetype(f, sz)
        except: pass
    return ImageFont.load_default

def ask_image():
    print("\n pick an image (JPG/PNG/Webp/TIFF < 8MB) from this folder.")
    while True:
        p = input("Image path: ").strip().strip('"').strip("'")
        if not p or not os.path.isfile(p): print("Not found"); continue
        if os.path.splittext(p)[1].lower() not in ALLOWED: print("Unsupported type."); continue
        if os.path.getsize(p)/(1024*1024) > MAX_MB: print("Too big (>8MB)."); continue
        try: Image.open(p).verify()
        except: print("Corrupted image."); continue
        return p

def infer(path, img_bytes, tries = 8):
    mime, _ = mimetypes.guess_type(path)
    for _ in range(tries):
        if mime and mime.startswith("image/"):
            r = requests.post(API,
                              headers={"AUthorization": f"bearer {HF_API_KEY}", "Content-Type": mime}, data= img_bytes, timeout=60) 
        else:
            r = requests.post(API,
                              headers="Authorization": f"Bearer {HF_API_KEY},
                              files = {"input": (os.path.basename(path), img_bytes, "application/octet-stream")},
                              timeout= 60)
        if