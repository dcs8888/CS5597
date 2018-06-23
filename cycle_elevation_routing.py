import requests
import math

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

    z = 15
    x, y = deg2num(38.878103, -94.859009, z)
    
    r = requests.get('https://tile.thunderforest.com/thunderforest.outdoors-v1.json?apikey=e25c01ab4aa14652b5bd3472c5e1f859')

    print(r.headers['Content-Type'])
    print(r.status_code)
    
    if r.status_code == requests.codes.ok:
        
        print(r.json())

if __name__ == "__main__":
   main()