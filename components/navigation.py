import streamlit as st

def setup_navigation(tab_titles):
    """Create navigation tabs in the UI."""
    # Create the tabs with CSS classes for styling
    tabs = st.tabs(tab_titles)
    
    # Add custom styling for the selected tab
    # (The actual styling is in the CSS)
    
    return tabs