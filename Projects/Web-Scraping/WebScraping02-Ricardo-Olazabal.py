import requests
res = requests.get("https://www.gutenberg.org/cache/epub/32370/pg32370.txt")
res.raise_for_status()
playFile = open("Secret Diplomatic History of The Eighteenth Century.text", "wb")
for chunk in res.iter_content(1000000):
    playFile.write(chunk)
playFile.close()