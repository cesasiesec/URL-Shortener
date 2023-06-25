
import pyshorteners

url = input("Enter URL :")
print("Done ! : ", pyshorteners.Shortener().tinyurl.short(url))

