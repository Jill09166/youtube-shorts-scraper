thonimport requests
from bs4 import BeautifulSoup

def parse_youtube_video(video_url):
    """
    Extracts video details from a YouTube Shorts URL.
    
    Args:
    - video_url (str): The URL of the YouTube Shorts video.

    Returns:
    - dict: Video details like title, views, likes, and more.
    """
    response = requests.get(video_url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch video data: {response.status_code}")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    video_data = {
        'title': soup.title.string.strip(),
        'url': video_url,
        'viewCount': soup.find('span', {'class': 'view-count'}).text.strip(),
        'likes': soup.find('button', {'aria-label': 'Like'}).text.strip(),
        'channelName': soup.find('a', {'class': 'channel-name'}).text.strip(),
        'channelUrl': soup.find('a', {'class': 'channel-name'})['href'],
        'duration': soup.find('span', {'class': 'duration'}).text.strip(),
        'commentsCount': soup.find('span', {'class': 'comments-count'}).text.strip(),
    }
    
    return video_data