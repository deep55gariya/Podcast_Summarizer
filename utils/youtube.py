import re
from youtube_transcript_api import YouTubeTranscriptApi
import streamlit as st

def extract_video_id(youtube_url):
    """Extract video ID from various YouTube URL formats."""
    # Handle different URL formats
    patterns = [
        r'(?:v=|\/)([0-9A-Za-z_-]{11}).*',  # Standard and short URL
        r'(?:embed\/)([0-9A-Za-z_-]{11})',  # Embed URL
        r'(?:youtu\.be\/)([0-9A-Za-z_-]{11})'  # Shortened URL
    ]
    
    for pattern in patterns:
        match = re.search(pattern, youtube_url)
        if match:
            return match.group(1)
    
    return None

def extract_transcript_details(youtube_video_url):
    """Get transcript from YouTube video URL."""
    try:
        video_id = extract_video_id(youtube_video_url)
        if not video_id:
            return "", video_id, None, "Invalid YouTube URL format"
        
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        # Directly extract text from transcript items
        transcript = " ".join([item['text'] for item in transcript_list])
        return transcript, video_id, transcript_list, None
    except Exception as e:
        error_message = str(e)
        return "", "", [], f"Failed to retrieve transcript: {error_message}"

def get_video_title(video_id):
    """Get video title from video ID."""
    try:
        # This is a placeholder - in a production app, you would use the YouTube API
        # For now, let's return a generic title with the video ID
        return f"YouTube Video (ID: {video_id})"
    except Exception as e:
        return f"Unknown Video (ID: {video_id})"