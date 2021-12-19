from requests import get  # This function is how we will make requests to a server.
from requests.models import Response  # This is the type of a Response object.

# https://www.guidebox.com/
# https://www.episodate.com/api

# 1. Starting small
# Endpoint: https://boredapi.com/api/activity/, returns a random activity for you to do.
bored_api_response: Response = get("https://boredapi.com/api/activity/")

# 200 means everything works, 400 means I messed up, 500 means the server had a problem (rerun)
# print(bored_api_response.status_code)
# print(bored_api_response.json())

# 2. Requests with params
# Endpoint: https://api.agify.io, returns average age for people with a given name (passed as a parameter)

agify_api_response: Response = get("https://api.agify.io", params={"name": "Shristi"})
print(agify_api_response.status_code)
print(agify_api_response.json())

def grab_url(planet: str, is_planet: bool) -> str:
    """Helper function to populate url variable in app.py. The file paths we build relate to files in our 'static' directory."""
    if is_planet:
        return f"/{planet.lower()}.jpg"
    else:
        return f"/space.jpg"

# 3. Requests with an API key
# TODO: Sign up for an API key: https://api.nasa.gov/
# Endpoint: https://api.nasa.gov/planetary/apod, returns the astronomy picture of the day! 
apod_response: Response = get("https://api.nasa.gov/planetary/apod?", params={"api_key": "VkIcz9ovFacBjGsicdbrq8t0YcXiyff0OL81nMIQ"})
print(apod_response.status_code)
print(apod_response.json())
