import streamlit as st
from utils.processing import process_youtube_url

def render_input_section():
    """Render the YouTube URL input form."""
    # Apply custom styling to the card
    st.markdown(
        """
        <div class="input-card">
            <h2 class="input-title">Enter a YouTube Video Link</h2>
            <p class="input-description">Extract insights, summaries, and more from any YouTube video with a transcript</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Input form to prevent reloading on every interaction
    with st.form("youtube_form", clear_on_submit=False):
        col1, col2 = st.columns([5, 1])
        
        with col1:
            youtube_link = st.text_input(
                "",
                key="youtube_link", 
                placeholder="Paste YouTube URL here...",
                label_visibility="collapsed"
            )
        
        with col2:
            # Submit button with custom styling
            submit_button = st.form_submit_button(
                "Analyze Video",
                type="primary", 
                use_container_width=True
            )
        
        if submit_button:
            if not youtube_link or 'youtube.com' not in youtube_link and 'youtu.be' not in youtube_link:
                st.error("Please enter a valid YouTube URL")
            else:
                with st.spinner("Processing your video..."):
                    process_youtube_url()