# Prompt templates for various AI tasks

SUMMARY_PROMPT = """You are a YouTube video summarizer. You will take the transcript text
and summarize the entire video, providing the important points in under 250 words.
Please provide the summary of the text given here: """

DIARIZATION_PROMPT = """You're analyzing a transcript from a YouTube video to identify different speakers.
Please identify distinct speakers in this transcript and label each segment with the appropriate speaker.
Each speaker should be labeled as Speaker 1, Speaker 2, etc.
Return your response as a JSON object with this format:
{
    "speakers": [
        {
            "id": "Speaker 1",
            "segments": [
                {"text": "First segment text by Speaker 1"},
                {"text": "Another segment by Speaker 1"}
            ]
        },
        {
            "id": "Speaker 2",
            "segments": [
                {"text": "First segment text by Speaker 2"},
                {"text": "Another segment by Speaker 2"}
            ]
        }
    ]
}
Here's the transcript: """

SPEAKER_SUMMARY_PROMPT = """You're analyzing a transcript segment from a specific speaker in a YouTube video.
Please provide a concise summary (50-100 words) of this speaker's key points and contributions.
Focus on their main arguments, insights, or information they shared.
Here's the transcript segment for this speaker: """

# New prompts for insights extraction
KEY_POINTS_PROMPT = """Extract the 5-7 most valuable and important points from this YouTube video transcript.
Focus on insights, takeaways, or information that would be most useful to someone who hasn't watched the video.
Format your response as a JSON array with this structure:
{
    "key_points": [
        "First important point in a concise sentence",
        "Second important point in a concise sentence",
        "Etc."
    ]
}
Here's the transcript: """

QUOTES_PROMPT = """Extract 3-5 of the most impactful, insightful, or memorable quotes from this YouTube video transcript.
Choose quotes that represent significant ideas, are well-articulated, or capture key moments in the discussion.
Format your response as a JSON array with this structure:
{
    "quotes": [
        {
            "text": "The exact quote text",
            "speaker": "Speaker name/number if available, otherwise 'Unknown'"
        },
        {
            "text": "Another quote",
            "speaker": "Speaker name/number if available"
        }
    ]
}
Here's the transcript: """

QA_PROMPT = """Identify any questions and their corresponding answers from this YouTube video transcript.
Look for explicit questions asked and the responses given to them.
Format your response as a JSON array with this structure:
{
    "qa_pairs": [
        {
            "question": "The exact question text",
            "asker": "Speaker who asked the question (if known, otherwise 'Unknown')",
            "answer": "The answer provided in response to the question",
            "answerer": "Speaker who provided the answer (if known, otherwise 'Unknown')"
        }
    ]
}
Here's the transcript: """

THEMES_PROMPT = """Identify 3-5 main themes or topics discussed in this YouTube video transcript.
For each theme, provide a brief description and explanation of how it relates to the video content.
Format your response as a JSON array with this structure:
{
    "themes": [
        {
            "name": "Name of the theme/topic",
            "description": "Brief explanation of this theme and its importance in the video"
        },
        {
            "name": "Name of another theme/topic",
            "description": "Brief explanation of this theme"
        }
    ]
}
Here's the transcript: """