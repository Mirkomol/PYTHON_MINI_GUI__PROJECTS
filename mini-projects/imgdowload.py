import urllib.request

# Adding information about user agent
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

filename = input("Enter name of picture") + '.jpg'
image_url = input("Enter your image url: ")

def dl_jpg(filename,image_url):
    urllib.request.urlretrieve(image_url, filename)

dl_jpg(filename, image_url)


