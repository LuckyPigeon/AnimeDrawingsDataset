import errno, json, os, requests, urllib.request

from bs4 import BeautifulSoup

baseurl = "http://danbooru.donmai.us/posts/"
f = open('./data.json')
items = json.load(f)
file_names = [item["file_name"] for item in items]

print("Create output directory...")

try:
    os.mkdir("./imgs")
except OSError as e:
    if e.errno == errno.EEXIST:
        print("Directory already exists!")

for file_name in file_names:
    basefile = os.path.basename(file_name)
    url = baseurl + basefile.split('.')[0]
    print(url)
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, "html.parser")
    urllib.request.urlretrieve(soup.select('picture')[0].find("source")['srcset'], "./imgs/" + basefile)
    print("Save " + url + " to image name: " + basefile)

print("Done!")