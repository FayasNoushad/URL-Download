import requests
import domain_extract


def download(url, name=""):
    try:
        response = requests.get(url)
        domain = domain_extract.domain(response.url)
        if not name:
            return raise Exception("No name found")
        with open(name, "wb") as file:
            file.write(response.content)
        return name 
    except Exception as error:
        return raise Exception(error)
