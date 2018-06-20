import requests
import math
from PIL import Image
from io import BytesIO

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

"""
From
https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#Lon..2Flat._to_tile_numbers_2
"""
def deg2num(lat_deg, lon_deg, zoom):
  lat_rad = math.radians(lat_deg)
  n = 2.0 ** zoom
  xtile = int((lon_deg + 180.0) / 360.0 * n)
  ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
  return (xtile, ytile)

def main():

    z = 5
    x, y = deg2num(38.878103, -94.859009, z)
    r = requests.get('https://tile.thunderforest.com/cycle/' + str(z) + '/' + str(x) + '/' + str(y) + '.png?apikey=e25c01ab4aa14652b5bd3472c5e1f859')

    if r.status_code == requests.codes.ok:
        
        i = Image.open(BytesIO(r.content))
        imgplot = plt.imshow(i)
        plt.show()



if __name__ == "__main__":
   main()