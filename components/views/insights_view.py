import streamlit as st

def render_insights_view():
    """Render the key insights tab view."""
    st.markdown('<h2 class="view-title">🔍 Key Insights</h2>', unsafe_allow_html=True)
    st.markdown('<p class="view-description">Automatically extracted valuable insights from the video content.</p>', unsafe_allow_html=True)
    
    # Download full insights PDF
    if st.session_state.insights_pdf:
        st.download_button(
            "⬇️ Download Complete Insights as PDF",
            data=st.session_state.insights_pdf,
            file_name="Video_Insights.pdf",
            mime="application/pdf",
            use_container_width=False
        )
    
    # Create tabs for different types of insights
    insight_tabs = st.tabs(["Key Points", "Quotes", "Q&A", "Themes"])
    
    with insight_tabs[0]:
        render_key_points()
    
    with insight_tabs[1]:
        render_quotes()
    
    with insight_tabs[2]:
        render_qa_pairs()
    
    with insight_tabs[3]:
        render_themes()

def render_key_points():
    """Render the key points section."""
    st.markdown('<h3 class="section-title">📌 Key Points</h3>', unsafe_allow_html=True)
    
    key_points = st.session_state.key_points
    if key_points:
        for i, point in enumerate(key_points, 1):
            st.markdown(
                f"""
                <div class="key-point-card">
                    <div class="key-point-number">{i}</div>
                    <div class="key-point-text">{point}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.info("No key points were extracted from this video.")

def render_quotes():
    """Render the impactful quotes section."""
    st.markdown('<h3 class="section-title">💬 Impactful Quotes</h3>', unsafe_allow_html=True)
    
    quotes = st.session_state.impactful_quotes
    if quotes:
        for quote in quotes:
            quote_text = quote.get("text", "")
            speaker = quote.get("speaker", "Unknown")
            
            st.markdown(
                f"""
                <div class="quote-card">
                    <div class="quote-mark">"</div>
                    <div class="quote-text">{quote_text}</div>
                    <div class="quote-attribution">— {speaker}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.info("No impactful quotes were extracted from this video.")

def render_qa_pairs():
    """Render the questions and answers section."""
    st.markdown('<h3 class="section-title">❓ Questions & Answers</h3>', unsafe_allow_html=True)
    
    qa_pairs = st.session_state.questions_answers
    if qa_pairs:
        for i, qa in enumerate(qa_pairs, 1):
            question = qa.get("question", "")
            asker = qa.get("asker", "Unknown")
            answer = qa.get("answer", "")
            answerer = qa.get("answerer", "Unknown")
            
            st.markdown(
                f"""
                <div class="qa-card">
                    <div class="question-container">
                        <div class="qa-icon">Q</div>
                        <div class="question-content">
                            <div class="question-text">{question}</div>
                            <div class="question-asker">Asked by: {asker}</div>
                        </div>
                    </div>
                    <div class="answer-container">
                        <div class="qa-icon">A</div>
                        <div class="answer-content">
                            <div class="answer-text">{answer}</div>
                            <div class="answer-provider">Answered by: {answerer}</div>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.info("No question-answer pairs were extracted from this video.")

def render_themes():
    """Render the key themes section."""
    st.markdown('<h3 class="section-title">🏷️ Key Themes</h3>', unsafe_allow_html=True)
    
    themes = st.session_state.key_themes
    if themes:
        # Create a grid layout for themes
        cols = st.columns(min(len(themes), 3))
        
        for i, theme in enumerate(themes):
            col_idx = i % len(cols)
            name = theme.get("name", "")
            description = theme.get("description", "")
            
            # Generate a theme color based on index
            colors = ["#E3F2FD", "#F3E5F5", "#E8F5E9", "#FFF8E1", "#FFEBEE"]
            text_colors = ["#1565C0", "#7B1FA2", "#2E7D32", "#F57F17", "#C62828"]
            color_idx = i % len(colors)
            
            with cols[col_idx]:
                st.markdown(
                    f"""
                    <div class="theme-card" style="background-color: {colors[color_idx]};">
                        <div class="theme-name" style="color: {text_colors[color_idx]};">{name}</div>
                        <div class="theme-description">{description}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
    else:
        st.info("No key themes were extracted from this video.")