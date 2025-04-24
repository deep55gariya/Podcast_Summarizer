import streamlit as st
import re
import json
import google.generativeai as genai
from textblob import TextBlob
from deep_translator import GoogleTranslator
import os

# Initialize Gemini API
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

def generate_summary(text, prompt):
    """Generate a summary using Gemini Pro API."""
    try:
        # Limit text length to avoid API limits
        max_length = 100000
        if len(text) > max_length:
            text = text[:max_length] + "... (truncated due to length)"
        
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(prompt + text)
        return response.text, None
    except Exception as e:
        return "", f"Summary generation failed: {str(e)}"

def translate_text(text, target_language):
    """Translate text to target language."""
    try:
        # Handle text in chunks if it's too long
        max_chunk_size = 4900  # Google Translator limit is 5000 characters
        
        if len(text) <= max_chunk_size:
            translator = GoogleTranslator(source='auto', target=target_language)
            return translator.translate(text), None
        
        # Split text into chunks for translation
        chunks = [text[i:i+max_chunk_size] for i in range(0, len(text), max_chunk_size)]
        translator = GoogleTranslator(source='auto', target=target_language)
        translated_chunks = [translator.translate(chunk) for chunk in chunks]
        
        return ''.join(translated_chunks), None
    except Exception as e:
        return "", f"Translation failed: {str(e)}"

def perform_speaker_diarization(transcript):
    """Identify different speakers in the transcript."""
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        from utils.constants import DIARIZATION_PROMPT
        response = model.generate_content(DIARIZATION_PROMPT + transcript)
        
        # Parse the JSON from the response
        content = response.text
        # Extract JSON if it's wrapped in markdown code blocks
        json_match = re.search(r'```(?:json)?\s*([\s\S]*?)\s*```', content)
        if json_match:
            content = json_match.group(1)
        
        # Clean any remaining text and parse JSON
        speaker_data = json.loads(content)
        return speaker_data, None
    except Exception as e:
        return {}, f"Speaker diarization failed: {str(e)}"

def generate_speaker_summary(speaker_text):
    """Generate a summary for a specific speaker's text."""
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        from utils.constants import SPEAKER_SUMMARY_PROMPT
        response = model.generate_content(SPEAKER_SUMMARY_PROMPT + speaker_text)
        return response.text, None
    except Exception as e:
        return "", f"Speaker summary generation failed: {str(e)}"

def analyze_sentiment(text):
    """Perform sentiment analysis on text."""
    try:
        # Use TextBlob for sentiment analysis
        blob = TextBlob(text)
        # Get polarity score (-1 to 1, where -1 is negative, 0 is neutral, 1 is positive)
        polarity = blob.sentiment.polarity
        # Get subjectivity score (0 to 1, where 0 is objective, 1 is subjective)
        subjectivity = blob.sentiment.subjectivity
        
        # Determine sentiment category
        if polarity > 0.1:
            sentiment = "Positive"
        elif polarity < -0.1:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
            
        return {
            "polarity": polarity,
            "subjectivity": subjectivity,
            "sentiment": sentiment
        }, None
    except Exception as e:
        return {}, f"Sentiment analysis failed: {str(e)}"

def extract_insights(transcript, prompt_type):
    """Extract various types of insights from transcript."""
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        
        prompt = ""
        if prompt_type == "key_points":
            from utils.constants import KEY_POINTS_PROMPT
            prompt = KEY_POINTS_PROMPT
        elif prompt_type == "quotes":
            from utils.constants import QUOTES_PROMPT
            prompt = QUOTES_PROMPT
        elif prompt_type == "qa":
            from utils.constants import QA_PROMPT
            prompt = QA_PROMPT
        elif prompt_type == "themes":
            from utils.constants import THEMES_PROMPT
            prompt = THEMES_PROMPT
        
        # Limit text length to avoid API limits
        max_length = 100000
        if len(transcript) > max_length:
            transcript = transcript[:max_length] + "... (truncated due to length)"
            
        response = model.generate_content(prompt + transcript)
        content = response.text
        
        # Extract JSON if it's wrapped in markdown code blocks
        json_match = re.search(r'```(?:json)?\s*([\s\S]*?)\s*```', content)
        if json_match:
            content = json_match.group(1)
            
        # Parse JSON response
        result = json.loads(content)
        return result, None
    except Exception as e:
        return {}, f"Insights extraction failed for {prompt_type}: {str(e)}"