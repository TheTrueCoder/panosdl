from pickle import HIGHEST_PROTOCOL
from operator import contains
from streetlevel.streetview.panorama import StreetViewPanorama
from streetlevel import streetview
import numpy as np
import pickle

start_coord: np.ndarray = np.array([53.4719528, -2.1910897])
end_coord: np.ndarray = np.array([53.473036, -2.190258])
steps = 4

pano_ids: list = []

for i in range(steps):
    current_coord = start_coord + (end_coord - start_coord) * (i/steps)
    print(i)
    print(current_coord)
    pano: StreetViewPanorama | None = streetview.find_panorama(current_coord[0], current_coord[1])
    print(pano)
    
    if contains(pano_ids, pano) == False:
        pano_ids.append(pano)

print(pano_ids)
with open("pano_ids.pkl", "wb") as file:
    pickle.dump(pano_ids, file, protocol=HIGHEST_PROTOCOL)



# streetview.download_panorama(pano, f"{pano.id}.jpg")
