from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

api_key = u'43fe8dfd294b944a72de095666cc2e77'
api_secret = u'6a601d17ddff726e'

animalname = sys.argv[1]
savedir = "./animals/" + animalname
waittime = 1

flickr = FlickrAPI(api_key, api_secret, format="parsed-json")

result = flickr.photos.search(
    text = animalname,
    per_page = 400,
    media = 'photos',
    sort = 'relevance',
    safe_search = 1,
    extras = 'url_q, license')

photos = result['photos']
# pprint(photos)


for i, photo in enumerate(photos['photo']):
    url_q = photo["url_q"]
    filepath = savedir + '/' + photo['id'] + '.jpg'
    if os.path.exists(filepath): continue
    urlretrieve(url_q, filepath)
    time.sleep(waittime)