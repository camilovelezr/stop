from gtts import gTTS
import os
from string import ascii_lowercase
from random import choice, random
from time import sleep
import json

letters = ascii_lowercase
sleep(choice([3, 2, 1]) + random())
with open("letters.json", "rb") as file:
    lett = json.load(file)["letters"]
r = choice(letters)
while r in lett:
    r = choice(letters)
lett.append(r)
with open("letters.json", "w") as file:
    json.dump({"letters": lett}, file)
sleep(random())
o = gTTS(text=r, lang="es", slow=False)
o.save("stop.mp3")
os.system("mpg321 stop.mp3")
print(r)
