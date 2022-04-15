import pyshorteners

url_input = input("Enter link or url to shorten: ")

shortner = pyshorteners.Shortener()

x = shortner.tinyurl.short(url_input)

print("\n","\033[91m {}\033[00m".format("Here is your shortened link :"), x)