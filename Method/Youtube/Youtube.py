import requests

import Constants as keys


# Use the `requests` library to make a GET request to the YouTube API
# to search for videos with the specified query
def search_youtube(query):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "key": keys.YT_API,
        "q": query,
        "part": "id",
        "type": "video",
        "maxResults": 1
    }
    response = requests.get(url, params=params)
    # Check the status code of the response to ensure that the request was successful
    if response.status_code == 200:
        # Extract the video ID from the response
        video_id = response.json()["items"][0]["id"]["videoId"]

        # Return the URL of the video
        return f"https://www.youtube.com/watch?v={video_id}"
    else:
        # If the request was not successful, return an error message
        return "An error occurred while searching for the video."
