thonimport requests
import json
from .extractors.youtube_parser import parse_youtube_video
from .outputs.data_exporter import export_data

def scrape_youtube_shorts(channel_url, num_videos=10):
    """
    Scrape the latest YouTube Shorts data from a given channel URL.

    Args:
    - channel_url (str): The URL of the YouTube channel.
    - num_videos (int): The number of YouTube Shorts to scrape (default 10).

    Returns:
    - List of dictionaries containing video data.
    """
    video_data = []
    
    # Fetch the YouTube channel page (simulated, would normally use YouTube API)
    response = requests.get(channel_url)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch channel data: {response.status_code}")
    
    # Parse the video data
    for video in range(num_videos):
        video_url = f"{channel_url}/shorts/video{video + 1}"
        video_info = parse_youtube_video(video_url)
        video_data.append(video_info)
    
    # Export data
    export_data(video_data, 'sample_output.json')
    
    return video_data