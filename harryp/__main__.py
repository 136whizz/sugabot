import glob 
from pathlib import Path 
from harryp.utils import load_plug
import logging 
from . import bot 


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

path = "harryp/plugins/*.py"
files = glob.glob(path)

for name in files:
  with open(name) as a:
    pxt = Path(a.name)
    plug_name = pxt.stem
    load_plug(plug_name.replace(".py",""))
    
   
print("HARRYP BOT STARTED & LOADED ALL PLUGINS")

if __name__ == "__main__":
  bot.run_until_disconnected()