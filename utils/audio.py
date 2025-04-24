import io
from gtts import gTTS

def create_audio(text, language='en'):
    """Create an MP3 audio file from text using Google TTS."""
    try:
        audio_buffer = io.BytesIO()
        tts = gTTS(text=text, lang=language, slow=False)
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)
        return audio_buffer, None
    except Exception as e:
        return None, f"Audio creation failed: {str(e)}"

def get_audio_player_html(audio_data, label="Audio Player"):
    """Create an HTML audio player with the given audio data."""
    import base64
    audio_base64 = base64.b64encode(audio_data.read()).decode()
    audio_html = f"""
        <div class="audio-player">
            <p class="audio-label">{label}</p>
            <audio controls class="audio-control">
                <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
                Your browser does not support the audio element.
            </audio>
        </div>
    """
    return audio_html