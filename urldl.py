import requests


def download(url, name):
    try:
        response = requests.get(url)
        with open(name, "wb") as file:
            file.write(response.content)
        return name 
    except Exception as error:
        raise Exception(error)
