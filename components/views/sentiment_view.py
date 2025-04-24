import streamlit as st

def display_sentiment_gauge(polarity, title="Sentiment"):
    """Create a sentiment gauge visualization."""
    # Convert polarity (-1 to 1) to percentage (0 to 100)
    polarity_percentage = ((polarity + 1) / 2) * 100
    
    # Determine color based on sentiment
    if polarity > 0.1:
        color = "#4CAF50"  # Green for positive
        gradient = "linear-gradient(90deg, #E8F5E9 0%, #A5D6A7 50%, #4CAF50 100%)"
    elif polarity < -0.1:
        color = "#F44336"  # Red for negative
        gradient = "linear-gradient(90deg, #FFEBEE 0%, #EF9A9A 50%, #F44336 100%)"
    else:
        color = "#9E9E9E"  # Gray for neutral
        gradient = "linear-gradient(90deg, #F5F5F5 0%, #E0E0E0 50%, #9E9E9E 100%)"
    
    # Calculate needle position
    needle_position = polarity_percentage
    
    # Create a simple gauge visualization with CSS
    gauge_html = f"""
    <div class="sentiment-gauge">
        <p class="gauge-title">{title}</p>
        <div class="gauge-container">
            <div class="gauge-background" style="background: {gradient};">
                <div class="gauge-indicator" style="left: {needle_position}%;">
                    <div class="gauge-needle" style="background-color: {color};"></div>
                </div>
            </div>
        </div>
        <div class="gauge-labels">
            <span class="gauge-label-negative">Negative</span>
            <span class="gauge-label-neutral">Neutral</span>
            <span class="gauge-label-positive">Positive</span>
        </div>
        <div class="gauge-score">
            Score: <span style="color: {color}; font-weight: bold;">{polarity:.2f}</span> 
            <span class="gauge-sentiment">({sentiment_to_text(polarity)})</span>
        </div>
    </div>
    """
    return gauge_html

def sentiment_to_text(polarity):
    """Convert polarity score to descriptive text."""
    if polarity > 0.5:
        return "Very Positive"
    elif polarity > 0.1:
        return "Positive"
    elif polarity < -0.5:
        return "Very Negative"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"

def render_sentiment_view():
    """Render the sentiment analysis tab view."""
    st.markdown('<h2 class="view-title">😊 Sentiment Analysis</h2>', unsafe_allow_html=True)
    st.markdown('<p class="view-description">Analysis of emotional tone throughout the conversation.</p>', unsafe_allow_html=True)
    
    # Overall sentiment
    sentiment_data = st.session_state.sentiment_data
    speaker_sentiment = st.session_state.speaker_sentiment
    
    if sentiment_data:
        st.markdown('<h3 class="section-title">Overall Sentiment</h3>', unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown(
                display_sentiment_gauge(
                    sentiment_data.get("polarity", 0), 
                    "Overall Emotional Tone"
                ), 
                unsafe_allow_html=True
            )
        
        with col2:
            # Create a card to display sentiment metrics
            polarity = sentiment_data.get('polarity', 0)
            subjectivity = sentiment_data.get('subjectivity', 0)
            sentiment_label = sentiment_data.get('sentiment', 'Neutral')
            
            # Determine sentiment icon
            if sentiment_label == "Positive":
                icon = "😊"
            elif sentiment_label == "Negative":
                icon = "😔"
            else:
                icon = "😐"
                
            st.markdown(
                f"""
                <div class="sentiment-metrics-card">
                    <div class="sentiment-heading">
                        <span class="sentiment-icon">{icon}</span>
                        <span class="sentiment-label">{sentiment_label}</span>
                    </div>
                    <div class="sentiment-metric">
                        <span class="metric-label">Polarity Score:</span>
                        <span class="metric-value">{polarity:.2f}</span>
                        <div class="metric-description">Range: -1 (negative) to +1 (positive)</div>
                    </div>
                    <div class="sentiment-metric">
                        <span class="metric-label">Subjectivity:</span>
                        <span class="metric-value">{subjectivity:.2f}</span>
                        <div class="metric-description">Range: 0 (objective) to 1 (subjective)</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
        
        # Per-speaker sentiment
        if speaker_sentiment:
            st.markdown('<h3 class="section-title">Sentiment by Speaker</h3>', unsafe_allow_html=True)
            
            # Create a grid for speaker sentiment cards
            num_speakers = len(speaker_sentiment)
            cols_per_row = 2
            
            for i in range(0, num_speakers, cols_per_row):
                cols = st.columns(cols_per_row)
                
                for j in range(cols_per_row):
                    idx = i + j
                    if idx < num_speakers:
                        speaker_id = list(speaker_sentiment.keys())[idx]
                        sentiment = speaker_sentiment[speaker_id]
                        
                        with cols[j]:
                            st.markdown(
                                f"""
                                <div class="speaker-sentiment-card">
                                    <h4 class="speaker-card-title">{speaker_id}</h4>
                                    {display_sentiment_gauge(
                                        sentiment.get("polarity", 0), 
                                        f"Emotional Tone"
                                    )}
                                </div>
                                """,
                                unsafe_allow_html=True
                            )
    else:
        st.warning("Sentiment analysis could not be performed for this transcript.")