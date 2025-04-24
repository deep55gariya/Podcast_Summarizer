import streamlit as st
from utils.history import load_video_from_history

def render_history_view():
    """Render the history tab view."""
    st.markdown('<h2 class="view-title">📚 Video History</h2>', unsafe_allow_html=True)
    st.markdown('<p class="view-description">Access previously processed videos without reprocessing them.</p>', unsafe_allow_html=True)
    
    # Check if we have any history
    if st.session_state.video_history:
        # Create a sorted list of history entries (most recent first)
        history_entries = list(st.session_state.video_history.values())
        history_entries.sort(key=lambda x: x["timestamp"], reverse=True)
        
        # Display history entries as cards
        for entry in history_entries:
            video_id = entry["video_id"]
            video_title = entry["video_title"]
            timestamp = entry["timestamp"]
            
            st.markdown(
                f"""
                <div class="history-card">
                    <div class="history-card-content">
                        <div class="history-thumbnail">
                            <img src="https://img.youtube.com/vi/{video_id}/mqdefault.jpg" alt="Thumbnail">
                        </div>
                        <div class="history-details">
                            <h3 class="history-title">{video_title}</h3>
                            <p class="history-timestamp">Processed on: {timestamp}</p>
                            <p class="history-video-id">Video ID: {video_id}</p>
                        </div>
                    </div>
                    <div class="history-card-actions" id="actions-{video_id}">
                        <!-- Action buttons are added via Streamlit -->
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            # Create a unique key for this card's actions
            cols = st.columns(3)
            
            with cols[0]:
                # Button to load this video's data
                if st.button(
                    "📂 Load Data", 
                    key=f"load_{video_id}",
                    use_container_width=True
                ):
                    with st.spinner("Loading video data..."):
                        load_video_from_history(video_id)
                        st.success("Video data loaded successfully!")
                        st.rerun()  # Force a rerun to update all tabs
            
            with cols[1]:
                # Button to watch the video
                if st.button(
                    "▶️ Watch Video", 
                    key=f"watch_{video_id}",
                    use_container_width=True
                ):
                    st.video(f"https://www.youtube.com/watch?v={video_id}")
            
            with cols[2]:
                # Option to delete this entry
                if st.button(
                    "🗑️ Delete", 
                    key=f"delete_{video_id}",
                    use_container_width=True
                ):
                    if video_id in st.session_state.video_history:
                        del st.session_state.video_history[video_id]
                        # Update disk storage
                        try:
                            import os
                            import pickle
                            os.makedirs('.streamlit', exist_ok=True)
                            with open('.streamlit/video_history.pkl', 'wb') as f:
                                pickle.dump(st.session_state.video_history, f)
                        except Exception as e:
                            st.warning(f"Could not update history file: {e}")
                        st.success("Entry deleted successfully!")
                        st.rerun()  # Force a rerun to update the history list
        
        # Clear all history button
        if st.button("🧹 Clear All History", type="secondary"):
            st.session_state.video_history = {}
            # Update disk storage
            try:
                import os
                import pickle
                os.makedirs('.streamlit', exist_ok=True)
                with open('.streamlit/video_history.pkl', 'wb') as f:
                    pickle.dump(st.session_state.video_history, f)
            except Exception as e:
                st.warning(f"Could not update history file: {e}")
            st.success("History cleared successfully!")
            st.rerun()  # Force a rerun to update the UI
    else:
        st.info("No video processing history available. Process some videos to see them here!")