import streamlit as st

def initialize_session_state():
    """Initialize all session state variables needed for the application."""
    
    # Core state variables
    if "transcript_text" not in st.session_state:
        st.session_state.transcript_text = ""
    if "transcript_segments" not in st.session_state:
        st.session_state.transcript_segments = []
    if "final_transcript" not in st.session_state:
        st.session_state.final_transcript = ""
    if "final_summary" not in st.session_state:
        st.session_state.final_summary = ""
    if "hindi_summary" not in st.session_state:
        st.session_state.hindi_summary = ""
    if "video_id" not in st.session_state:
        st.session_state.video_id = ""
    if "processing_complete" not in st.session_state:
        st.session_state.processing_complete = False
        
    # PDF and audio files
    if "transcript_pdf" not in st.session_state:
        st.session_state.transcript_pdf = None
    if "summary_pdf" not in st.session_state:
        st.session_state.summary_pdf = None
    if "dual_summary_pdf" not in st.session_state:
        st.session_state.dual_summary_pdf = None
    if "speaker_pdf" not in st.session_state:
        st.session_state.speaker_pdf = None
    if "insights_pdf" not in st.session_state:
        st.session_state.insights_pdf = None
    if "transcript_audio" not in st.session_state:
        st.session_state.transcript_audio = None
    if "summary_audio" not in st.session_state:
        st.session_state.summary_audio = None
        
    # Speaker diarization data
    if "speaker_data" not in st.session_state:
        st.session_state.speaker_data = {}
    if "speaker_summaries" not in st.session_state:
        st.session_state.speaker_summaries = {}
    if "speaker_sentiment" not in st.session_state:
        st.session_state.speaker_sentiment = {}
        
    # Sentiment analysis data
    if "sentiment_data" not in st.session_state:
        st.session_state.sentiment_data = {}
        
    # Insights data
    if "key_points" not in st.session_state:
        st.session_state.key_points = []
    if "impactful_quotes" not in st.session_state:
        st.session_state.impactful_quotes = []
    if "questions_answers" not in st.session_state:
        st.session_state.questions_answers = []
    if "key_themes" not in st.session_state:
        st.session_state.key_themes = []
        
    # History
    if "video_history" not in st.session_state:
        st.session_state.video_history = {}
        
    # UI state management
    if "current_view" not in st.session_state:
        st.session_state.current_view = "input"
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = False