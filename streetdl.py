from streetlevel import streetview

pano = streetview.find_panorama(53.472291, -2.1908061)
print(pano)
streetview.download_panorama(pano, f"{pano.id}.jpg")
