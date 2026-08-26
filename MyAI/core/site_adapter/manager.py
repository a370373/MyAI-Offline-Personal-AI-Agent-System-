from urllib.parse import urlparse


def get_site(url):


    host=urlparse(url).hostname or ""



    if "google" in host:

        return "google"



    if "youtube" in host:

        return "youtube"



    if "github" in host:

        return "github"



    return "generic"
