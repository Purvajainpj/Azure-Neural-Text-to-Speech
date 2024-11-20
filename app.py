import streamlit as st
import random
import os
from azure.cognitiveservices.speech import (
    AudioDataStream,
    SpeechConfig,
    SpeechSynthesizer,
    SpeechSynthesisOutputFormat,
    ResultReason,
    CancellationReason,
    SpeechSynthesisCancellationDetails
)

# Updated dictionary with Ava's complete styles
VOICE_STYLES = {
    "en-US-AvaMultilingualNeural": {
        "name": "Ava (US Multilingual)",
        "styles": ["Default","Advertisement", "Conversation", "Social_media", "Speech", "Sports", "Story", "Recipe", "Disfluent"]
    },
    "en-US-JennyMultilingualNeural": {
        "name": "Jenny (US Multilingual)",
        "styles": ["Default"]
    },
    "en-GB-AdaMultilingualNeural": {
        "name": "Ada (UK Multilingual)",
        "styles": ["Default"]
    },
    "en-GB-OllieMultilingualNeural": {
        "name": "Ollie (UK Multilingual)",
        "styles": ["Default"]
    },
    "en-US-Ava:DragonHDLatestNeural": {
        "name": "Ava (US HD)",
        "styles": ["Default"]
    },
    "en-US-Emma2:DragonHDLatestNeural": {
        "name": "Emma (US HD)",
        "styles": ["Default"]
    },
    "en-US-Jenny:DragonHDLatestNeural": {
        "name": "Jenny (US HD)",
        "styles": ["Default"]
    },
    "en-US-Andrew2:DragonHDLatestNeural": {
        "name": "Andrew (US HD)",
        "styles": ["Default"]
    },
    "en-US-Steffan:DragonHDLatestNeural": {
        "name": "Steffan (US HD)",
        "styles": ["Default"]
    },
    "en-US-AriaNeural": {
        "name": "Aria (Female, US)",
        "styles": ["Neutral","angry", "cheerful", "excited", "friendly", "hopeful", "sad", "shouting", "terrified", "unfriendly", "whispering"]
    },
    "en-US-DavisNeural": {
        "name": "Davis (Male, US)",
        "styles": ["Neutral","angry", "cheerful", "excited", "friendly", "hopeful", "sad", "shouting", "terrified", "unfriendly", "whispering"]
    },
    "en-US-GuyNeural": {
        "name": "Guy (Male, US)",
        "styles": ["Neutral","angry", "cheerful", "excited", "friendly", "hopeful", "sad", "shouting", "terrified", "unfriendly", "whispering"]
    }
}

def create_ssml(text, voice_name, style=None, rate=1.0, pitch=0):
    """Convert plain text to SSML format with style and prosody controls"""
    text = (text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&apos;"))
    
    language = voice_name[:5]
    
    # Different SSML format for Ava's styles
    if voice_name == "en-US-AvaMultilingualNeural":
        ssml = f"""<?xml version="1.0" encoding="UTF-8"?>
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
       xmlns:mstts="http://www.w3.org/2001/mstts" xml:lang="{language}">
    <voice name="{voice_name}">
        <mstts:silence type="Tailing" value="0"/>"""
        
        if style:
            if style == "Disfluent":
                ssml += f'<mstts:express-as style="Disfluent" stutter="20" nervousness="50">'
            elif style == "Advertisement":
                ssml += f'<mstts:express-as style="{style}" stutter="0" nervousness="0">'
            else:
                ssml += f'<mstts:express-as style="{style}">'
        
        ssml += f'<prosody rate="{rate}" pitch="{pitch:+}%">{text}</prosody>'
        
        if style:
            ssml += '</mstts:express-as>'
        
        ssml += """</voice>
</speak>"""
    else:
        # Original SSML format for other voices
        ssml = f"""<?xml version="1.0" encoding="UTF-8"?>
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
       xmlns:mstts="http://www.w3.org/2001/mstts" xml:lang="{language}">
    <voice name="{voice_name}">"""
        
        if style and style != "Default":
            ssml += f'<mstts:express-as style="{style}">'
        
        ssml += f'<prosody rate="{rate}" pitch="{pitch:+}%">{text}</prosody>'
        
        if style and style != "Default":
            ssml += '</mstts:express-as>'
        
        ssml += """</voice>
</speak>"""
    
    return ssml

def convert_text_to_speech(subscription_key, subscription_region, text, audio_format, 
                          output_folder, voice_name, style=None, rate=1.0, pitch=0):
    """Convert text to speech using Azure's TTS service"""
    os.makedirs(output_folder, exist_ok=True)
    output_file = f"file-{random.randint(10000,99999)}.wav"
    
    try:
        speech_config = SpeechConfig(subscription=subscription_key, region=subscription_region)
        speech_config.set_speech_synthesis_output_format(
            SpeechSynthesisOutputFormat[audio_format]
        )
        speech_config.speech_synthesis_voice_name = voice_name
        
        synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=None)
        
        ssml_text = create_ssml(text, voice_name, style, rate, pitch)
        #st.write("Generated SSML:", ssml_text)  # For debugging
        
        result = synthesizer.speak_ssml_async(ssml_text).get()
        
        if result.reason == ResultReason.SynthesizingAudioCompleted:
            stream = AudioDataStream(result)
            output_path = os.path.join(output_folder, output_file)
            stream.save_to_wav_file(output_path)
            return output_path
        else:
            cancellation_details = SpeechSynthesisCancellationDetails(result)
            raise Exception(f"Speech synthesis failed. Error: {cancellation_details.error_details}")
            
    except Exception as e:
        raise Exception(f"Error in text-to-speech conversion: {str(e)}")

def main():
    st.title("Text-to-Speech Converter")
    
    # Configuration
    st.sidebar.header("Configuration")
    subscription_key = st.sidebar.text_input(
        "Azure Speech API Key",
        type="password",
        placeholder="Enter your Azure Speech API key"
    )
    subscription_region = st.sidebar.text_input(
        "Azure Region",
        placeholder="e.g., westeurope"
    )
    
    # Voice settings
    st.header("Voice Settings")
    col1, col2 = st.columns(2)
    
    with col1:
        selected_voice_name = st.selectbox(
            "Select Voice",
            options=[voice["name"] for voice in VOICE_STYLES.values()],
            help="Choose from available multilingual voices"
        )
        
        voice_id = [k for k, v in VOICE_STYLES.items() if v["name"] == selected_voice_name][0]
        
    with col2:
        available_styles = VOICE_STYLES[voice_id]["styles"]
        selected_style = st.selectbox(
            "Speaking Style",
            options=available_styles,
            help="Choose the speaking style for the voice"
        )
    
    # Voice modifications
    st.header("Voice Modifications")
    col3, col4 = st.columns(2)
    
    with col3:
        speaking_rate = st.slider(
            "Speaking Rate",
            min_value=0.5,
            max_value=2.0,
            value=1.0,
            step=0.1,
            help="Adjust how fast or slow the voice speaks"
        )
    
    with col4:
        pitch = st.slider(
            "Pitch Adjustment",
            min_value=-50,
            max_value=50,
            value=0,
            step=10,
            help="Adjust the pitch of the voice"
        )
    
    # Audio format
    audio_format = st.sidebar.selectbox(
        "Audio Format",
        ["Riff16Khz16BitMonoPcm", "Riff24Khz16BitMonoPcm", "Riff48Khz16BitMonoPcm"],
        index=1,
        help="Higher KHz = better quality but larger file size"
    )
    
    output_folder = st.sidebar.text_input(
        "Output Folder",
        value="output"
    )
    
    # Text input
    st.header("Text Input")
    input_text = st.text_area(
        "Enter your text here",
        value="Hello! This is a test message. 你好！这是一条测试消息。 Bonjour! Ceci est un message test.",
        height=200,
        help="Enter text in any supported language"
    )
    
    # Convert button
    if st.button("Convert to Speech"):
        if not subscription_key or not subscription_region:
            st.error("Please enter your Azure Speech API key and region in the sidebar.")
        else:
            try:
                with st.spinner("Converting text to speech..."):
                    output_path = convert_text_to_speech(
                        subscription_key,
                        subscription_region,
                        input_text,
                        audio_format,
                        output_folder,
                        voice_id,
                        selected_style if selected_style != "Default" else None,
                        speaking_rate,
                        pitch
                    )
                
                st.success("Conversion completed!")
                
                with open(output_path, "rb") as audio_file:
                    audio_bytes = audio_file.read()
                    st.audio(audio_bytes, format="audio/wav")
                
                st.download_button(
                    label="Download audio file",
                    data=audio_bytes,
                    file_name=os.path.basename(output_path),
                    mime="audio/wav"
                )
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    
    # Help section
    with st.expander("Help & Information"):
        st.markdown("""
        ### How to use this application:
        1. Enter your Azure Speech API key and region in the sidebar
        2. Choose a voice from the available multilingual options
        3. Select a speaking style (if available for the selected voice)
        4. Adjust the speaking rate and pitch if desired
        5. Enter your text (supports multiple languages)
        6. Click 'Convert to Speech' to generate the audio
        
        ### Available Voices:
        - Multilingual Voices:
            - Ava (US Multilingual) - Supports Default, Advertisement, Conversation, Social_media, Speech, Sports, Story, Recipe, Disfluent
            - Jenny (US Multilingual), Ada (UK Multilingual), Ollie (UK Multilingual) - Default style only

        - HD Voices:
            - Ava (US HD), Emma (US HD), Jenny (US HD), Andrew (US HD), Steffan (US HD) - Default style only

        - Emotional Voices:
            - Aria (Female, US), Davis (Male, US), Guy (Male, US) - Supports Neutral, angry, cheerful, excited, friendly, hopeful, sad, shouting, terrified, unfriendly, whispering
        
        ### Audio Formats:
        - Riff16Khz16BitMonoPcm: Basic quality, smaller file size
        - Riff24Khz16BitMonoPcm: Standard quality, balanced file size (recommended)
        - Riff48Khz16BitMonoPcm: High quality, larger file size
        """)

if __name__ == "__main__":
    main()
