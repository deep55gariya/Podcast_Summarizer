import streamlit as st
from utils.audio import get_audio_player_html

def render_summary_view():
    """Render the summary tab view."""
    st.markdown('<h2 class="view-title">📝 Video Summary</h2>', unsafe_allow_html=True)
    
    # Create tabs for English and Hindi summaries
    summary_tabs = st.tabs(["English Summary", "Hindi Summary", "Audio"])
    
    with summary_tabs[0]:
        # English Summary
        st.markdown(
            f"""
            <div class="summary-container">
                <div class="summary-content">
                    {st.session_state.final_summary}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with summary_tabs[1]:
        # Hindi Summary
        st.markdown(
            f"""
            <div class="summary-container">
                <div class="summary-content hindi-text">
                    {st.session_state.hindi_summary}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with summary_tabs[2]:
        # Audio player for summary
        if st.session_state.summary_audio:
            st.session_state.summary_audio.seek(0)  # Reset pointer
            st.markdown(
                get_audio_player_html(
                    st.session_state.summary_audio, 
                    "Summary Audio (English)"
                ), 
                unsafe_allow_html=True
            )
        else:
            st.info("Summary audio is not available.")
    
    # Download buttons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.session_state.dual_summary_pdf:
            st.download_button(
                "⬇️ Download Bilingual Summary", 
                data=st.session_state.dual_summary_pdf, 
                file_name="Summary_English_Hindi.pdf",
                mime="application/pdf",
                use_container_width=True
            )
    
    with col2:
        if st.session_state.summary_pdf:
            st.download_button(
                "⬇️ Download English Summary", 
                data=st.session_state.summary_pdf, 
                file_name="Summary_English.pdf",
                mime="application/pdf",
                use_container_width=True
            )
    
    with col3:
        if st.session_state.summary_audio:
            st.download_button(
                "⬇️ Download Summary Audio", 
                data=st.session_state.summary_audio, 
                file_name="Summary_English.mp3",
                mime="audio/mp3",
                use_container_width=True
            )