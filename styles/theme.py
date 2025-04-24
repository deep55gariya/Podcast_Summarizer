import streamlit as st

def apply_theme():
    """Apply a custom theme to the Streamlit app."""
    # Set the theme using st.set_page_config in the main app file
    pass

def apply_custom_css():
    """Apply custom CSS to enhance the appearance of the app."""
    st.markdown("""
    <style>
        /* Global Styles and Variables */
        :root {
            --primary-color: #1E88E5;
            --primary-light: #64B5F6;
            --primary-dark: #0D47A1;
            --secondary-color: #6A1B9A;
            --secondary-light: #9C27B0;
            --accent-color: #FF6F00;
            --success-color: #4CAF50;
            --warning-color: #FF9800;
            --error-color: #F44336;
            --background-color: #F5F7FA;
            --card-background: white;
            --text-primary: #212121;
            --text-secondary: #757575;
            --border-radius: 8px;
            --spacing-unit: 8px;
            --box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            --transition-speed: 0.3s;
        }
        
        /* Base Styles */
        .stApp {
            background-color: var(--background-color);
        }
        
        /* Typography */
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            font-weight: 700;
            color: var(--text-primary);
        }
        
        p, li, div {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            color: var(--text-secondary);
            line-height: 1.5;
        }
        
        .subtitle {
            font-size: 1.2rem;
            color: var(--text-secondary);
            margin-top: -1rem;
            margin-bottom: 2rem;
        }
        
        /* Card Styles */
        .input-card {
            background-color: var(--card-background);
            border-radius: var(--border-radius);
            padding: calc(var(--spacing-unit) * 3);
            box-shadow: var(--box-shadow);
            margin-bottom: calc(var(--spacing-unit) * 3);
            transition: all var(--transition-speed) ease;
            border-left: 4px solid var(--primary-color);
        }
        
        .input-card:hover {
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        }
        
        .input-title {
            font-size: 1.5rem;
            margin-bottom: calc(var(--spacing-unit));
            color: var(--primary-dark);
        }
        
        .input-description {
            color: var(--text-secondary);
            margin-bottom: calc(var(--spacing-unit) * 2);
        }
        
        /* View Headers */
        .view-title {
            font-size: 1.8rem;
            color: var(--primary-dark);
            margin-bottom: calc(var(--spacing-unit));
            padding-bottom: calc(var(--spacing-unit));
            border-bottom: 2px solid var(--primary-light);
        }
        
        .view-description {
            font-size: 1.1rem;
            color: var(--text-secondary);
            margin-bottom: calc(var(--spacing-unit) * 3);
        }
        
        .section-title {
            font-size: 1.4rem;
            color: var(--primary-dark);
            margin: calc(var(--spacing-unit) * 3) 0 calc(var(--spacing-unit) * 2);
        }
        
        /* Transcript Section */
        .transcript-container {
            background-color: var(--card-background);
            border-radius: var(--border-radius);
            padding: calc(var(--spacing-unit) * 3);
            box-shadow: var(--box-shadow);
            margin-bottom: calc(var(--spacing-unit) * 3);
            max-height: 400px;
            overflow-y: auto;
        }
        
        .transcript-content {
            white-space: pre-line;
            line-height: 1.6;
        }
        
        /* Summary Section */
        .summary-container {
            background-color: var(--card-background);
            border-radius: var(--border-radius);
            padding: calc(var(--spacing-unit) * 3);
            box-shadow: var(--box-shadow);
            margin-bottom: calc(var(--spacing-unit) * 3);
        }
        
        .summary-content {
            white-space: pre-line;
            line-height: 1.6;
            font-size: 1.1rem;
        }
        
        .hindi-text {
            font-family: 'Noto Sans', sans-serif;
            line-height: 1.8;
        }
        
        /* Speaker Sections */
        .speaker-container {
            display: flex;
            background-color: var(--card-background);
            border-radius: var(--border-radius);
            padding: calc(var(--spacing-unit) * 2);
            box-shadow: var(--box-shadow);
            margin-bottom: calc(var(--spacing-unit) * 2);
            border-left: 4px solid var(--secondary-color);
        }
        
        .speaker-icon {
            font-size: 1.5rem;
            margin-right: calc(var(--spacing-unit) * 2);
            color: var(--secondary-color);
        }
        
        .speaker-content {
            flex: 1;
            white-space: pre-line;
        }
        
        .speaker-summary-card {
            background-color: var(--card-background);
            border-radius: var(--border-radius);
            padding: calc(var(--spacing-unit) * 3);
            box-shadow: var(--box-shadow);
            margin-bottom: calc(var(--spacing-unit) * 3);
            height: 100%;
            border-top: 4px solid var(--secondary-color);
            transition: transform var(--transition-speed) ease;
        }
        
        .speaker-summary-card:hover {
            transform: translateY(-4px);
        }
        
        .speaker-summary-header {
            display: flex;
            align-items: center;
            margin-bottom: calc(var(--spacing-unit) * 2);
        }
        
        .speaker-name {
            font-size: 1.2rem;
            margin: 0;
            color: var(--secondary-color);
        }
        
        .speaker-summary-content {
            line-height: 1.6;
        }
        
        /* Sentiment Section */
        .sentiment-gauge {
            background-color: var(--card-background);
            border-radius: var(--border-radius);
            padding: calc(var(--spacing-unit) * 3);
            box-shadow: var(--box-shadow);
            margin-bottom: calc(var(--spacing-unit) * 3);
            text-align: center;
        }
        
        .gauge-title {
            font-size: 1.2rem;
            font-weight: 500;
            margin-bottom: calc(var(--spacing-unit) * 2);
            color: var(--text-primary);
        }
        
        .gauge-container {
            position: relative;
            height: 30px;
            margin-bottom: calc(var(--spacing-unit) * 1);
        }
        
        .gauge-background {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 100%;
            border-radius: 15px;
            overflow: hidden;
        }
        
        .gauge-indicator {
            position: absolute;
            top: -5px;
            height: calc(100% + 10px);
            width: 1px;
            transition: left 1s ease-in-out;
        }
        
        .gauge-needle {
            position: absolute;
            top: 0;
            left: -5px;
            width: 10px;
            height: 100%;
            border-radius: 5px;
            transition: background-color 1s ease;
        }
        
        .gauge-labels {
            display: flex;
            justify-content: space-between;
            margin-bottom: calc(var(--spacing-unit) * 2);
            font-size: 0.9rem;
        }
        
        .gauge-label-negative {
            color: #F44336;
        }
        
        .gauge-label-neutral {
            color: #9E9E9E;
        }
        
        .gauge-label-positive {
            color: #4CAF50;
        }
        
        .gauge-score {
            font-size: 1.1rem;
            margin-top: calc(var(--spacing-unit) * 2);
        }
        
        .gauge-sentiment {
            font-weight: normal;
            font-style: italic;
        }
        
        .sentiment-metrics-card {
            background-color: var(--card-background);
            border-radius: var(--border-radius);
            padding: calc(var(--spacing-unit) * 3);
            box-shadow: var(--box-shadow);
            height: 100%;
        }
        
        .sentiment-heading {
            display: flex;
            align-items: center;
            margin-bottom: calc(var(--spacing-unit) * 3);
        }
        
        .sentiment-icon {
            font-size: 2rem;
            margin-right: calc(var(--spacing-unit) * 2);
        }
        
        .sentiment-label {
            font-size: 1.4rem;
            font-weight: 600;
            color: var(--text-primary);
        }
        
        .sentiment-metric {
            margin-bottom: calc(var(--spacing-unit) * 2);
        }
        
        .metric-label {
            font-weight: 500;
            display: block;
            margin-bottom: calc(var(--spacing-unit) * 0.5);
            color: var(--text-primary);
        }
        
        .metric-value {
            font-size: 1.2rem;
            font-weight: 600;
            color: var(--primary-dark);
        }
        
        .metric-description {
            font-size: 0.9rem;
            color: var(--text-secondary);
            margin-top: 4px;
        }
        
        .speaker-sentiment-card {
            background-color: var(--card-background);
            border-radius: var(--border-radius);
            padding: calc(var(--spacing-unit) * 3);
            box-shadow: var(--box-shadow);
            margin-bottom: calc(var(--spacing-unit) * 3);
            height: 100%;
        }
        
        .speaker-card-title {
            font-size: 1.2rem;
            margin-bottom: calc(var(--spacing-unit) * 2);
            color: var(--secondary-color);
            text-align: center;
        }
        
        /* Insights Section */
        .key-point-card {
            display: flex;
            background-color: var(--card-background);
            border-radius: var(--border-radius);
            padding: calc(var(--spacing-unit) * 2);
            box-shadow: var(--box-shadow);
            margin-bottom: calc(var(--spacing-unit) * 2);
            align-items: flex-start;
            transition: transform 0.2s ease;
        }
        
        .key-point-card:hover {
            transform: translateX(5px);
        }
        
        .key-point-number {
            font-size: 1.2rem;
            font-weight: 700;
            background-color: var(--primary-color);
            color: white;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: calc(var(--spacing-unit) * 2);
            flex-shrink: 0;
        }
        
        .key-point-text {
            flex: 1;
            line-height: 1.5;
        }
        
        .quote-card {
            position: relative;
            background-color: var(--card-background);
            border-radius: var(--border-radius);
            padding: calc(var(--spacing-unit) * 4) calc(var(--spacing-unit) * 3);
            box-shadow: var(--box-shadow);
            margin-bottom: calc(var(--spacing-unit) * 3);
            border-left: 4px solid var(--accent-color);
        }
        
        .quote-mark {
            position: absolute;
            top: 10px;
            left: 15px;
            font-size: 3rem;
            font-family: Georgia, serif;
            color: rgba(var(--accent-color-rgb), 0.2);
            line-height: 1;
        }
        
        .quote-text {
            font-size: 1.1rem;
            line-height: 1.6;
            font-style: italic;
            margin-bottom: calc(var(--spacing-unit) * 2);
        }
        
        .quote-attribution {
            text-align: right;
            font-weight: 500;
            color: var(--text-primary);
        }
        
        .qa-card {
            background-color: var(--card-background);
            border-radius: var(--border-radius);
            padding: calc(var(--spacing-unit) * 3);
            box-shadow: var(--box-shadow);
            margin-bottom: calc(var(--spacing-unit) * 3);
        }
        
        .question-container, .answer-container {
            display: flex;
            margin-bottom: calc(var(--spacing-unit) * 2);
            align-items: flex-start;
        }
        
        .qa-icon {
            font-size: 1.2rem;
            font-weight: 700;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: calc(var(--spacing-unit) * 2);
            flex-shrink: 0;
        }
        
        .question-container .qa-icon {
            background-color: var(--primary-color);
            color: white;
        }
        
        .answer-container .qa-icon {
            background-color: var(--accent-color);
            color: white;
        }
        
        .question-content, .answer-content {
            flex: 1;
        }
        
        .question-text, .answer-text {
            margin-bottom: calc(var(--spacing-unit));
            line-height: 1.5;
        }
        
        .question-asker, .answer-provider {
            font-size: 0.9rem;
            font-style: italic;
            color: var(--text-secondary);
        }
        
        .theme-card {
            background-color: var(--card-background);
            border-radius: var(--border-radius);
            padding: calc(var(--spacing-unit) * 3);
            box-shadow: var(--box-shadow);
            margin-bottom: calc(var(--spacing-unit) * 3);
            height: 100%;
            transition: transform 0.3s ease;
        }
        
        .theme-card:hover {
            transform: translateY(-5px);
        }
        
        .theme-name {
            font-size: 1.2rem;
            font-weight: 600;
            margin-bottom: calc(var(--spacing-unit) * 2);
        }
        
        .theme-description {
            line-height: 1.6;
        }
        
        /* History Section */
        .history-card {
            background-color: var(--card-background);
            border-radius: var(--border-radius);
            padding: calc(var(--spacing-unit) * 3);
            box-shadow: var(--box-shadow);
            margin-bottom: calc(var(--spacing-unit) * 3);
            transition: transform 0.3s ease;
        }
        
        .history-card:hover {
            transform: translateY(-3px);
        }
        
        .history-card-content {
            display: flex;
            margin-bottom: calc(var(--spacing-unit) * 2);
        }
        
        .history-thumbnail {
            margin-right: calc(var(--spacing-unit) * 3);
            flex-shrink: 0;
        }
        
        .history-thumbnail img {
            width: 160px;
            border-radius: calc(var(--border-radius) / 2);
        }
        
        .history-details {
            flex: 1;
        }
        
        .history-title {
            font-size: 1.3rem;
            margin-bottom: calc(var(--spacing-unit));
            color: var(--primary-dark);
        }
        
        .history-timestamp {
            font-size: 0.9rem;
            color: var(--text-secondary);
            margin-bottom: calc(var(--spacing-unit) / 2);
        }
        
        .history-video-id {
            font-size: 0.9rem;
            color: var(--text-secondary);
        }
        
        /* Audio Player */
        .audio-player {
            background-color: var(--card-background);
            border-radius: var(--border-radius);
            padding: calc(var(--spacing-unit) * 3);
            box-shadow: var(--box-shadow);
            margin-bottom: calc(var(--spacing-unit) * 3);
        }
        
        .audio-label {
            font-weight: 600;
            margin-bottom: calc(var(--spacing-unit));
            color: var(--primary-dark);
        }
        
        .audio-control {
            width: 100%;
            margin-top: calc(var(--spacing-unit));
        }
        
        /* Success Message */
        .success-message {
            display: flex;
            align-items: center;
            background-color: #E8F5E9;
            border-radius: var(--border-radius);
            padding: calc(var(--spacing-unit) * 2);
            margin: calc(var(--spacing-unit) * 2) 0;
            border-left: 4px solid var(--success-color);
            animation: fadeOut 8s forwards;
        }
        
        .success-icon {
            font-size: 1.5rem;
            color: var(--success-color);
            margin-right: calc(var(--spacing-unit) * 2);
            font-weight: bold;
            background-color: var(--success-color);
            color: white;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .success-text {
            color: #2E7D32;
            font-weight: 500;
        }
        
        @keyframes fadeOut {
            0% { opacity: 1; }
            70% { opacity: 1; }
            100% { opacity: 0; }
        }
        
        /* Override Streamlit styles */
        .stButton > button {
            border-radius: var(--border-radius);
            font-weight: 500;
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        
        div.stDownloadButton > button {
            border-radius: var(--border-radius);
            font-weight: 500;
            transition: all 0.3s ease;
        }
        
        div.stDownloadButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: var(--border-radius);
            padding: 8px 16px;
            transition: all 0.3s ease;
        }
        
        .stTabs [data-baseweb="tab-highlight"] {
            background-color: var(--primary-color);
        }
        
        /* Loading Spinner */
        .stSpinner > div > div > div {
            border-top-color: var(--primary-color) !important;
        }
        
        /* Responsive Adjustments */
        @media (max-width: 768px) {
            .history-card-content {
                flex-direction: column;
            }
            
            .history-thumbnail {
                margin-right: 0;
                margin-bottom: calc(var(--spacing-unit) * 2);
                text-align: center;
            }
            
            .history-thumbnail img {
                width: 100%;
                max-width: 240px;
            }
        }
    </style>
    """, unsafe_allow_html=True)