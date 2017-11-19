import os
import urllib2
import json
import errno


directory = '/Users/' + os.environ.get('USER') + '/Pictures/Wallpapers'
if not os.path.exists(directory):
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

bing_url = 'http://www.bing.com'
url = bing_url + '/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US'

content = json.load(urllib2.urlopen(url))
image_url = bing_url + content['images'][0]['url']
name = image_url.split('/')[-1]

response = urllib2.urlopen(image_url)

image_path = directory + '/' + name
with open(image_path, 'w') as f:
    f.write(response.read())

os.system("""osascript -e 'tell application "System Events" to tell every desktop to set picture to "{}"'""".format(image_path))


