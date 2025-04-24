import streamlit as st
from utils.audio import get_audio_player_html

def render_transcript_view():
    """Render the transcript tab view."""
    st.markdown('<h2 class="view-title">📜 Full Transcript</h2>', unsafe_allow_html=True)
    
    # Create a tab-like interface for different transcript views
    transcript_tabs = st.tabs(["Text View", "Audio Preview"])
    
    with transcript_tabs[0]:
        st.markdown(
            f"""
            <div class="transcript-container">
                <div class="transcript-content">
                    {st.session_state.final_transcript}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.session_state.transcript_pdf:
                st.download_button(
                    "⬇️ Download Transcript as PDF", 
                    data=st.session_state.transcript_pdf, 
                    file_name="Transcript.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
        
        with col2:
            if st.session_state.transcript_audio:
                st.download_button(
                    "⬇️ Download Audio Preview", 
                    data=st.session_state.transcript_audio, 
                    file_name="Transcript_Preview.mp3",
                    mime="audio/mp3",
                    use_container_width=True
                )
    
    with transcript_tabs[1]:
        # Audio player for transcript
        if st.session_state.transcript_audio:
            st.session_state.transcript_audio.seek(0)  # Reset pointer
            st.markdown(
                get_audio_player_html(
                    st.session_state.transcript_audio, 
                    "Transcript Audio Preview"
                ), 
                unsafe_allow_html=True
            )
            st.caption("Note: Audio preview is limited to approximately the first 500 words")
        else:
            st.info("Audio preview is not available.")