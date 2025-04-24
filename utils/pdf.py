import io
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def create_pdf(text, title="Document", is_transcript_with_speakers=False, speaker_data=None, is_insights=False, insights_data=None):
    """Create a PDF document with the provided text and formatting."""
    try:
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        styles = getSampleStyleSheet()
        
        # Create custom styles
        speaker_style = ParagraphStyle(
            'SpeakerStyle',
            parent=styles['Heading2'],
            textColor=colors.blue,
            spaceBefore=12,
            spaceAfter=6
        )
        
        heading_style = ParagraphStyle(
            'HeadingStyle',
            parent=styles['Heading1'],
            textColor=colors.black,
            spaceBefore=12,
            spaceAfter=6
        )
        
        subheading_style = ParagraphStyle(
            'SubheadingStyle',
            parent=styles['Heading2'],
            textColor=colors.darkblue,
            spaceBefore=10,
            spaceAfter=5
        )
        
        highlight_style = ParagraphStyle(
            'HighlightStyle',
            parent=styles['Normal'],
            textColor=colors.black,
            backColor=colors.lightgrey,
            spaceBefore=6,
            spaceAfter=6,
            borderWidth=1,
            borderColor=colors.grey,
            borderPadding=5
        )
        
        story = []
        
        # Add title
        story.append(Paragraph(title, styles['Title']))
        story.append(Spacer(1, 12))
        
        if is_insights and insights_data:
            # Format insights document
            # Key Points
            story.append(Paragraph("Key Points", heading_style))
            if "key_points" in insights_data and insights_data["key_points"]:
                for i, point in enumerate(insights_data["key_points"], 1):
                    story.append(Paragraph(f"{i}. {point}", styles["Normal"]))
                    story.append(Spacer(1, 6))
            else:
                story.append(Paragraph("No key points extracted.", styles["Normal"]))
            story.append(Spacer(1, 12))
            
            # Impactful Quotes
            story.append(Paragraph("Impactful Quotes", heading_style))
            if "quotes" in insights_data and insights_data["quotes"]:
                for i, quote in enumerate(insights_data["quotes"], 1):
                    quote_text = quote.get("text", "")
                    speaker = quote.get("speaker", "Unknown")
                    story.append(Paragraph(f'"{quote_text}"', highlight_style))
                    story.append(Paragraph(f"- {speaker}", styles["Italic"]))
                    story.append(Spacer(1, 8))
            else:
                story.append(Paragraph("No impactful quotes extracted.", styles["Normal"]))
            story.append(Spacer(1, 12))
            
            # Questions and Answers
            story.append(Paragraph("Questions & Answers", heading_style))
            if "qa_pairs" in insights_data and insights_data["qa_pairs"]:
                for i, qa in enumerate(insights_data["qa_pairs"], 1):
                    question = qa.get("question", "")
                    asker = qa.get("asker", "Unknown")
                    answer = qa.get("answer", "")
                    answerer = qa.get("answerer", "Unknown")
                    
                    story.append(Paragraph(f"Q{i}: {question}", subheading_style))
                    story.append(Paragraph(f"Asked by: {asker}", styles["Italic"]))
                    story.append(Spacer(1, 4))
                    story.append(Paragraph(f"A: {answer}", styles["Normal"]))
                    story.append(Paragraph(f"Answered by: {answerer}", styles["Italic"]))
                    story.append(Spacer(1, 10))
            else:
                story.append(Paragraph("No question-answer pairs extracted.", styles["Normal"]))
            story.append(Spacer(1, 12))
            
            # Key Themes
            story.append(Paragraph("Key Themes", heading_style))
            if "themes" in insights_data and insights_data["themes"]:
                for i, theme in enumerate(insights_data["themes"], 1):
                    name = theme.get("name", "")
                    description = theme.get("description", "")
                    story.append(Paragraph(f"{i}. {name}", subheading_style))
                    story.append(Paragraph(description, styles["Normal"]))
                    story.append(Spacer(1, 8))
            else:
                story.append(Paragraph("No key themes extracted.", styles["Normal"]))
                
        elif is_transcript_with_speakers and speaker_data and 'speakers' in speaker_data:
            # Format document with speaker segments
            for speaker in speaker_data['speakers']:
                # Add speaker heading
                story.append(Paragraph(speaker['id'], speaker_style))
                
                # Add each segment for this speaker
                for segment in speaker['segments']:
                    if segment['text'].strip():
                        p = Paragraph(segment['text'], styles["Normal"])
                        story.append(p)
                        story.append(Spacer(1, 6))
                
                story.append(Spacer(1, 12))
        else:
            # Regular text document
            paragraphs = text.split('\n')
            for para in paragraphs:
                if para.strip():  # Skip empty paragraphs
                    p = Paragraph(para, styles["Normal"])
                    story.append(p)
                    story.append(Spacer(1, 6))
        
        doc.build(story)
        buffer.seek(0)
        return buffer, None
    except Exception as e:
        return None, f"PDF creation failed: {str(e)}"

def create_dual_language_summary_pdf(english_summary, hindi_summary, title="Dual Language Summary"):
    """Create a PDF with both English and Hindi summaries."""
    try:
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        styles = getSampleStyleSheet()
        
        # Create custom styles
        heading_style = ParagraphStyle(
            'HeadingStyle',
            parent=styles['Heading1'],
            textColor=colors.black,
            spaceBefore=12,
            spaceAfter=6
        )
        
        language_heading_style = ParagraphStyle(
            'LanguageHeading',
            parent=styles['Heading2'],
            textColor=colors.darkblue,
            spaceBefore=12,
            spaceAfter=6
        )
        
        story = []
        
        # Add title
        story.append(Paragraph(title, styles['Title']))
        story.append(Spacer(1, 12))
        
        # English section
        story.append(Paragraph("English Summary", language_heading_style))
        story.append(Spacer(1, 6))
        
        english_paragraphs = english_summary.split('\n')
        for para in english_paragraphs:
            if para.strip():  # Skip empty paragraphs
                p = Paragraph(para, styles["Normal"])
                story.append(p)
                story.append(Spacer(1, 6))
        
        story.append(Spacer(1, 12))
        
        # Hindi section
        story.append(Paragraph("Hindi Summary (हिंदी सारांश)", language_heading_style))
        story.append(Spacer(1, 6))
        
        hindi_paragraphs = hindi_summary.split('\n')
        for para in hindi_paragraphs:
            if para.strip():  # Skip empty paragraphs
                # Using a custom style for Hindi text if needed
                p = Paragraph(para, styles["Normal"])
                story.append(p)
                story.append(Spacer(1, 6))
        
        doc.build(story)
        buffer.seek(0)
        return buffer, None
    except Exception as e:
        return None, f"Dual language PDF creation failed: {str(e)}"