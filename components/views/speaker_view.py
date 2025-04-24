import streamlit as st
from utils.audio import create_audio, get_audio_player_html

def render_speaker_view():
    """Render the speaker diarization tab view."""
    st.markdown('<h2 class="view-title">👥 Speaker Identification</h2>', unsafe_allow_html=True)
    st.markdown('<p class="view-description">Automatically identified speakers and their contributions in the video.</p>', unsafe_allow_html=True)
    
    speaker_data = st.session_state.speaker_data
    
    if speaker_data and "speakers" in speaker_data:
        # Download full speaker transcript
        if "speaker_pdf" in st.session_state and st.session_state.speaker_pdf:
            st.download_button(
                "⬇️ Download Complete Speaker Transcript",
                data=st.session_state.speaker_pdf,
                file_name="Speaker_Transcript.pdf",
                mime="application/pdf",
                use_container_width=True
            )
        
        # Show speaker segments in expandable sections
        for speaker in speaker_data["speakers"]:
            speaker_id = speaker['id']
            speaker_text = "\n\n".join([segment["text"] for segment in speaker["segments"]])
            
            with st.expander(f"{speaker_id}", expanded=False):
                st.markdown(
                    f"""
                    <div class="speaker-container">
                        <div class="speaker-icon">👤</div>
                        <div class="speaker-content">
                            {speaker_text}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                
                # Create audio for this speaker's transcript
                if st.button(
                    f"🔊 Generate Audio for {speaker_id}", 
                    key=f"audio_{speaker_id}",
                    use_container_width=True
                ):
                    with st.spinner(f"Creating audio for {speaker_id}..."):
                        # Limit to first 1000 words
                        preview_text = " ".join(speaker_text.split()[:1000])
                        speaker_audio, audio_error = create_audio(preview_text, 'en')
                        
                        if audio_error:
                            st.warning(audio_error)
                        elif speaker_audio:
                            st.markdown(
                                get_audio_player_html(
                                    speaker_audio, 
                                    f"{speaker_id} Audio"
                                ), 
                                unsafe_allow_html=True
                            )
                            st.download_button(
                                f"⬇️ Download {speaker_id} Audio",
                                data=speaker_audio,
                                file_name=f"{speaker_id.replace(' ', '_')}_Audio.mp3",
                                mime="audio/mp3",
                                use_container_width=True
                            )
    else:
        st.warning("Speaker identification could not be performed for this transcript.")

def render_speaker_summaries():
    """Render the speaker summaries tab view."""
    st.markdown('<h2 class="view-title">🗣️ Speaker Insights</h2>', unsafe_allow_html=True)
    st.markdown('<p class="view-description">Key points and contributions from each speaker.</p>', unsafe_allow_html=True)
    
    speaker_summaries = st.session_state.speaker_summaries
    
    if speaker_summaries:
        # Create a grid layout for speaker summaries
        num_speakers = len(speaker_summaries)
        cols_per_row = 2  # Number of columns per row
        
        # Split speakers into rows
        for i in range(0, num_speakers, cols_per_row):
            cols = st.columns(cols_per_row)
            
            for j in range(cols_per_row):
                idx = i + j
                if idx < num_speakers:
                    speaker_id = list(speaker_summaries.keys())[idx]
                    summary = speaker_summaries[speaker_id]
                    
                    with cols[j]:
                        st.markdown(
                            f"""
                            <div class="speaker-summary-card">
                                <div class="speaker-summary-header">
                                    <div class="speaker-icon">👤</div>
                                    <h3 class="speaker-name">{speaker_id}</h3>
                                </div>
                                <div class="speaker-summary-content">
                                    {summary}
                                </div>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
                        
                        # Generate PDF for this speaker's summary
                        if st.button(
                            f"📄 Create PDF", 
                            key=f"pdf_{speaker_id}",
                            use_container_width=True
                        ):
                            with st.spinner(f"Creating PDF for {speaker_id}..."):
                                from utils.pdf import create_pdf
                                summary_pdf, pdf_error = create_pdf(
                                    summary, 
                                    title=f"Summary of {speaker_id}'s Contribution"
                                )
                                
                                if pdf_error:
                                    st.warning(pdf_error)
                                elif summary_pdf:
                                    st.download_button(
                                        f"⬇️ Download PDF",
                                        data=summary_pdf,
                                        file_name=f"{speaker_id.replace(' ', '_')}_Summary.pdf",
                                        mime="application/pdf",
                                        use_container_width=True
                                    )
    else:
        st.warning("Speaker summaries could not be generated for this transcript.")