import requests

url = 'https://assets.ctfassets.net/0tc4847zqy12/20xaFcHqrIxnfTpY9Oqw0Y/21ebb6c4209a5089eadd58e91b8d0a1e/Qdoba_Nutrition_Information_2021.pdf'

req = requests.get(url, stream=True)

filename = req.url[url.rfind('/') + 1:]

with open(filename, 'wb') as f:
    for chunk in req.iter_content(chunk_size=8092):
        if chunk:
            f.write(chunk)

    print(filename + " has been downloaded")
