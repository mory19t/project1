import requests


def search_movie(movie_name):
    url = "https://redl.ink/myupera/links"

    params = {
        "q": f'title:"{movie_name}" AND mediatype:movies',
        "fl[]": ["identifier", "title"],
        "output": "json",
        "rows": 10
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    return data["response"]["docs"]


def get_movie_files(identifier):
    url = f"https://redl.ink/myupera/links/{identifier}"

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    for file in data.get("files", []):
        name = file.get("name", "")

        if name.lower().endswith(".mp4"):
            return {
                "name": name,
                "url": f"https://redl.ink/myupera/links/{identifier}/{name}"
            }

    return None
