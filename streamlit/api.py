from requests import get


def get_movie_list_by_page(page=1):
    url = "https://moviesapi.ir/api/v1/movies"

    try:
        response = get(
            url,
            params={"page": page},
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        return data.get("data", [])

    except Exception:
        return []


if __name__ == "__main__":
    result = get_movie_list_by_page()
    print(result)