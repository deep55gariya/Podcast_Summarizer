import streamlit as st

# ✅ Must be the first Streamlit command
st.set_page_config(
    page_title="Podcast Summarizer",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

from dotenv import load_dotenv
import os

from components.navigation import setup_navigation
from components.input_section import render_input_section
from components.views.transcript_view import render_transcript_view
from components.views.summary_view import render_summary_view
from components.views.speaker_view import render_speaker_view, render_speaker_summaries
from components.views.sentiment_view import render_sentiment_view
from components.views.insights_view import render_insights_view
from components.views.history_view import render_history_view
from utils.processing import process_youtube_url
from utils.session import initialize_session_state
from styles.theme import apply_theme, apply_custom_css
from utils.history import load_history_from_disk

# Load environment variables and configure API
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("Google API key not found. Please check your .env file.")

def main():
    # Apply custom theme and CSS
    apply_theme()
    apply_custom_css()
    
    # Initialize session state variables
    initialize_session_state()
    
    # Load history from disk
    load_history_from_disk()
    
    # Header section with logo and title
    col1, col2 = st.columns([1, 4])
    with col1:
        # st.image("assets/logo.png", width=100)
        st.image("https://upload.wikimedia.org/wikipedia/commons/0/08/YouTube_Logo_2017.svg", width=100)

    with col2:
        st.title("Podcast AI Notes")
        st.markdown(
            """
            <p class="subtitle">Transform videos into interactive notes, summaries, and insights</p>
            """, 
            unsafe_allow_html=True
        )
    
    # Input section for YouTube URL
    render_input_section()
    
    # If processing is complete, show the results
    if st.session_state.processing_complete:
        # Display YouTube video if we have a video ID
        if st.session_state.video_id:
            st.video(f"https://www.youtube.com/watch?v={st.session_state.video_id}")
        
        # Create the navigation tabs
        tab_titles = [
            "📜 Transcript", 
            "📝 Summary", 
            "👥 Speakers",
            "🗣️ Speaker Insights",
            "😊 Sentiment", 
            "🔍 Key Insights",
            "📚 History"
        ]
        tabs = setup_navigation(tab_titles)
        
        # Render the different views based on the selected tab
        with tabs[0]:
            render_transcript_view()
        
        with tabs[1]:
            render_summary_view()
        
        with tabs[2]:
            render_speaker_view()
        
        with tabs[3]:
            render_speaker_summaries()
        
        with tabs[4]:
            render_sentiment_view()
        
        with tabs[5]:
            render_insights_view()
        
        with tabs[6]:
            render_history_view()
        
        # Show success message that fades out
        st.markdown(
            """
            <div class="success-message">
                <div class="success-icon">✓</div>
                <div class="success-text">Analysis complete! Navigate through the tabs to explore your results.</div>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        # Add a reset button to start over
        st.button(
            "🔄 Process Another Video", 
            on_click=lambda: reset_session(), 
            key="reset_button"
        )

def reset_session():
    # Reset all session state variables except history
    for key in list(st.session_state.keys()):
        if key not in ["youtube_link", "video_history"]:
            del st.session_state[key]
    
    st.session_state.processing_complete = False
    st.rerun()

if __name__ == "__main__":
    main()
