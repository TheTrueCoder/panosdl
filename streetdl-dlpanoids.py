from os import mkdir
from streetlevel import streetview
import pickle

with open("pano_ids.pkl", "rb") as file:
    pano_ids = pickle.load(file)

pano_ids
print(pano_ids)
if input("Good? Anything to stop") != "":
    exit()

mkdir('panos')
for pano in pano_ids:
    print(pano)
    streetview.download_panorama(pano, f"panos/{pano.id}.jpg")
