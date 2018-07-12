import requests
import math
import json
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

    z = 15
    lat = 38.878103
    lon = -94.859009
    x, y = deg2num(lat, lon, z)

    r_json = requests.get('https://tile.thunderforest.com/thunderforest.outdoors-v1.json?apikey=e25c01ab4aa14652b5bd3472c5e1f859')

    print('Request Vector Outdoors')
    print(r_json.headers['Content-Type'])
    print(r_json.status_code)

    if r_json.status_code == requests.codes.ok:
        # Load into JSON for usage
        json_data = json.loads(r_json.text)

        # Pretty Printing for ease of reading
        print(json.dumps(json_data, sort_keys=True, indent=4, separators=(',', ': ')))

        if 'center' in json_data:
            print(json_data['center'])
            json_data['center'] = [z, lat, lon]
            print(json_data['center'])
            print(json.dumps(json_data, sort_keys=True, indent=4, separators=(',', ': ')))

    r_img = requests.get('https://tile.thunderforest.com/cycle/' + str(z) + '/' + str(x) + '/' + str(y) + '.jpg90?apikey=e25c01ab4aa14652b5bd3472c5e1f859')

    print('Request CYCLE IMG')
    print(r_img.headers['Content-Type'])
    print(r_img.status_code)

    if r_img.status_code == requests.codes.ok:
        i = Image.open(BytesIO(r_img.content))
        imgplot = plt.imshow(i)
        plt.show()

    left = str(-94.840385)
    right = str(-94.788114)
    bottom = str(38.845563)
    top = str(38.89488)
    r_osm = requests.get('https://api.openstreetmap.org/api/0.6/map?bbox=' + left + ',' + bottom + ',' + right + ',' + top)
    
    print('Request OSM')
    print(r_osm.headers['Content-Type'])
    print(r_osm.status_code)
    
    if r_osm.status_code == requests.codes.ok:
        with open('osm.xml', 'wb') as f_osm:
            f_osm.write(r_osm.content)

if __name__ == "__main__":
   main()