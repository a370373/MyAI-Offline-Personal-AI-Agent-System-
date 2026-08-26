import requests


def search(keyword):

    try:

        url = "https://www.google.com/search"

        params = {
            "q": keyword
        }

        headers = {
            "User-Agent":
            "Mozilla/5.0"
        }


        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=10
        )


        return {
            "success": True,
            "keyword": keyword,
            "content": response.text[:2000]
        }


    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }



def run(keyword=""):

    return search(
        keyword
    )
