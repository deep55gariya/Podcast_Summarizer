import streamlit as st
import datetime
import pickle
import os

def save_to_history(video_id, video_title, data_dict):
    """Save video processing results to history."""
    try:
        # Create a timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Create history entry
        history_entry = {
            "video_id": video_id,
            "video_title": video_title,
            "timestamp": timestamp,
            "data": data_dict
        }
        
        # Add to history dictionary using video_id as key
        st.session_state.video_history[video_id] = history_entry
        
        # Optionally save to disk for persistence across sessions
        try:
            # Make sure directory exists
            os.makedirs('.streamlit', exist_ok=True)
            with open('.streamlit/video_history.pkl', 'wb') as f:
                pickle.dump(st.session_state.video_history, f)
        except Exception as e:
            st.warning(f"Could not save history to disk: {e}")
            
        return True
    except Exception as e:
        st.warning(f"Error saving history: {e}")
        return False

def load_history_from_disk():
    """Load history from disk file."""
    try:
        with open('.streamlit/video_history.pkl', 'rb') as f:
            st.session_state.video_history = pickle.load(f)
        return True
    except Exception:
        # If file doesn't exist or can't be read, just use empty dict
        if "video_history" not in st.session_state:
            st.session_state.video_history = {}
        return False

def load_video_from_history(video_id):
    """Load a specific video's data from history."""
    if video_id in st.session_state.video_history:
        history_entry = st.session_state.video_history[video_id]
        data = history_entry["data"]
        
        # Load data back into session state
        st.session_state.final_summary = data.get("summary", "")
        st.session_state.hindi_summary = data.get("hindi_summary", "")
        st.session_state.final_transcript = data.get("transcript", "")
        st.session_state.speaker_data = data.get("speaker_data", {})
        st.session_state.speaker_summaries = data.get("speaker_summaries", {})
        st.session_state.sentiment_data = data.get("sentiment_data", {})
        st.session_state.speaker_sentiment = data.get("speaker_sentiment", {})
        st.session_state.key_points = data.get("key_points", [])
        st.session_state.impactful_quotes = data.get("impactful_quotes", [])
        st.session_state.questions_answers = data.get("questions_answers", [])
        st.session_state.key_themes = data.get("key_themes", [])
        st.session_state.video_id = video_id
        
        # Regenerate dual language PDF for summary
        from utils.pdf import create_dual_language_summary_pdf
        dual_summary_pdf, pdf_error = create_dual_language_summary_pdf(
            st.session_state.final_summary, 
            st.session_state.hindi_summary,
            title="Video Summary (English & Hindi)"
        )
        
        if pdf_error:
            st.warning(pdf_error)
        else:
            st.session_state.dual_summary_pdf = dual_summary_pdf
        
        st.session_state.processing_complete = True
        return True
    return False