import streamlit as st
import re
import json
import io

from utils.youtube import extract_transcript_details, get_video_title
from utils.nlp import (
    generate_summary, translate_text, perform_speaker_diarization, 
    generate_speaker_summary, analyze_sentiment, extract_insights
)
from utils.pdf import (
    create_pdf, create_dual_language_summary_pdf
)
from utils.audio import create_audio
from utils.history import save_to_history
from utils.constants import (
    SUMMARY_PROMPT, DIARIZATION_PROMPT, SPEAKER_SUMMARY_PROMPT,
    KEY_POINTS_PROMPT, QUOTES_PROMPT, QA_PROMPT, THEMES_PROMPT
)

def process_youtube_url():
    """Process a YouTube URL to extract transcript and generate all analyses."""
    
    with st.status("Processing video...", expanded=True) as status:
        status.update(label="Extracting transcript from YouTube...", state="running")
        transcript_text, video_id, transcript_segments, transcript_error = extract_transcript_details(st.session_state.youtube_link)
        
        if transcript_error:
            st.error(transcript_error)
            status.update(label=f"Error: {transcript_error}", state="error")
            return False
        
        st.session_state.transcript_text = transcript_text
        st.session_state.transcript_segments = transcript_segments
        st.session_state.video_id = video_id
        video_title = get_video_title(video_id)
        
        # Generate summary
        status.update(label="Generating summary...", state="running")
        summary, summary_error = generate_summary(transcript_text, SUMMARY_PROMPT)
        if summary_error:
            st.error(summary_error)
            status.update(label=f"Error: {summary_error}", state="error")
            return False
        
        # Store English summary
        st.session_state.final_summary = summary
        
        # Generate Hindi translation of summary
        status.update(label="Translating summary to Hindi...", state="running")
        hindi_summary, hindi_trans_error = translate_text(summary, 'hi')
        if hindi_trans_error:
            st.warning(hindi_trans_error)
            st.session_state.hindi_summary = "Hindi translation failed"
        else:
            st.session_state.hindi_summary = hindi_summary
        
        # Create dual language PDF for summary
        status.update(label="Creating dual language summary PDF...", state="running")
        dual_summary_pdf, pdf_error = create_dual_language_summary_pdf(
            summary, 
            st.session_state.hindi_summary,
            title="Video Summary (English & Hindi)"
        )
        
        if pdf_error:
            st.warning(pdf_error)
        else:
            st.session_state.dual_summary_pdf = dual_summary_pdf
        
        # Perform speaker diarization
        status.update(label="Identifying speakers in the transcript...", state="running")
        speaker_data, diarization_error = perform_speaker_diarization(transcript_text)
        if diarization_error:
            st.warning(diarization_error)
            # Create a fallback speaker data structure if diarization fails
            speaker_data = {
                "speakers": [
                    {
                        "id": "Speaker (All)",
                        "segments": [{"text": transcript_text}]
                    }
                ]
            }
        
        st.session_state.speaker_data = speaker_data
        
        # Generate summaries for each speaker
        speaker_summaries = {}
        for speaker in speaker_data.get("speakers", []):
            speaker_id = speaker["id"]
            speaker_text = " ".join([segment["text"] for segment in speaker["segments"]])
            
            if speaker_text:
                speaker_summary, summary_error = generate_speaker_summary(speaker_text)
                if not summary_error:
                    speaker_summaries[speaker_id] = speaker_summary
                else:
                    speaker_summaries[speaker_id] = f"Could not generate summary: {summary_error}"
        
        st.session_state.speaker_summaries = speaker_summaries
        
        # Extract insights
        status.update(label="Extracting key insights from the transcript...", state="running")
        
        # Extract key points
        key_points_data, key_points_error = extract_insights(transcript_text, "key_points")
        if key_points_error:
            st.warning(key_points_error)
            st.session_state.key_points = []
        else:
            st.session_state.key_points = key_points_data.get("key_points", [])
        
        # Extract impactful quotes
        quotes_data, quotes_error = extract_insights(transcript_text, "quotes")
        if quotes_error:
            st.warning(quotes_error)
            st.session_state.impactful_quotes = []
        else:
            st.session_state.impactful_quotes = quotes_data.get("quotes", [])
        
        # Extract Q&A pairs
        qa_data, qa_error = extract_insights(transcript_text, "qa")
        if qa_error:
            st.warning(qa_error)
            st.session_state.questions_answers = []
        else:
            st.session_state.questions_answers = qa_data.get("qa_pairs", [])
        
        # Extract key themes
        themes_data, themes_error = extract_insights(transcript_text, "themes")
        if themes_error:
            st.warning(themes_error)
            st.session_state.key_themes = []
        else:
            st.session_state.key_themes = themes_data.get("themes", [])
        
        # Create insights PDF
        insights_data = {
            "key_points": st.session_state.key_points,
            "quotes": st.session_state.impactful_quotes,
            "qa_pairs": st.session_state.questions_answers,
            "themes": st.session_state.key_themes
        }
        
        insights_pdf, pdf_error = create_pdf(
            "", 
            title="Video Insights",
            is_insights=True,
            insights_data=insights_data
        )
        
        if pdf_error:
            st.warning(pdf_error)
        else:
            st.session_state.insights_pdf = insights_pdf
        
        # Perform sentiment analysis
        status.update(label="Analyzing sentiment...", state="running")
        
        # Overall sentiment
        sentiment_data, sentiment_error = analyze_sentiment(transcript_text)
        if sentiment_error:
            st.warning(sentiment_error)
        st.session_state.sentiment_data = sentiment_data
        
        # Per speaker sentiment
        speaker_sentiment = {}
        for speaker in speaker_data.get("speakers", []):
            speaker_id = speaker["id"]
            speaker_text = " ".join([segment["text"] for segment in speaker["segments"]])
            
            if speaker_text:
                sentiment, _ = analyze_sentiment(speaker_text)
                speaker_sentiment[speaker_id] = sentiment
        
        st.session_state.speaker_sentiment = speaker_sentiment
            
        # Set transcript for display (English only)
        st.session_state.final_transcript = transcript_text
        
        # Create PDF files
        status.update(label="Creating PDF files...", state="running")
        
        transcript_pdf, pdf_error = create_pdf(transcript_text, title="Transcript")
        summary_pdf, pdf_error_summary = create_pdf(summary, title="Summary")
        
        # Create speaker transcript PDF
        speaker_pdf, speaker_pdf_error = create_pdf(
            "", 
            title="Speaker Transcript",
            is_transcript_with_speakers=True,
            speaker_data=speaker_data
        )
        
        if pdf_error:
            st.warning(pdf_error)
        if pdf_error_summary:
            st.warning(pdf_error_summary)
        if speaker_pdf_error:
            st.warning(speaker_pdf_error)
            
        st.session_state.transcript_pdf = transcript_pdf
        st.session_state.summary_pdf = summary_pdf
        st.session_state.speaker_pdf = speaker_pdf
        
        # Create audio files - limit transcript audio to prevent timeouts
        status.update(label="Creating audio files...", state="running")
        
        # Limit transcript audio to first ~1-2 minutes for preview
        transcript_preview = transcript_text.split()[:500]  # About 500 words
        transcript_preview_text = " ".join(transcript_preview)
        
        transcript_audio, transcript_audio_error = create_audio(transcript_preview_text, 'en')
        summary_audio, summary_audio_error = create_audio(summary, 'en')
        
        if transcript_audio_error:
            st.warning(transcript_audio_error)
        if summary_audio_error:
            st.warning(summary_audio_error)
            
        st.session_state.transcript_audio = transcript_audio
        st.session_state.summary_audio = summary_audio
        
        # Save to history
        data_to_save = {
            "summary": summary,
            "hindi_summary": st.session_state.hindi_summary,
            "transcript": transcript_text,
            "speaker_data": speaker_data,
            "speaker_summaries": speaker_summaries,
            "sentiment_data": sentiment_data,
            "speaker_sentiment": speaker_sentiment,
            "key_points": st.session_state.key_points,
            "impactful_quotes": st.session_state.impactful_quotes,
            "questions_answers": st.session_state.questions_answers,
            "key_themes": st.session_state.key_themes
        }
        save_to_history(video_id, video_title, data_to_save)
        
        # Update status and session state
        status.update(label="Processing complete!", state="complete")
        st.session_state.processing_complete = True
        
        return True