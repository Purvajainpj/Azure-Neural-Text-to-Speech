# Azure Neural Text-to-Speech Streamlit Application

## Overview
Azure Neural Text-to-Speech (TTS) is a powerful Streamlit-based application that converts text into natural-sounding speech using advanced neural network models.

## Features
1. Multilingual Voices,
Support for multiple languages in a single voice.
Voices: Ava, Jenny, Ada, Ollie (US and UK Multilingual)
2. HD Voice Technology,
Crystal-clear audio quality.
Premium voices: Ava HD, Emma HD, Jenny HD, Andrew HD, Steffan HD
3. Emotional Voice Styles, 
Multiple emotional styles available.
Voices: Aria, Davis, Guy
Styles include: Neutral, angry, cheerful, excited, friendly, and more

## Prerequisites
1. Python 3.6+
2. Azure account with Speech Service enabled
3. Azure Speech API key and region

## Installation
1.	Clone the repository
2.	Install dependencies: 

pip install -r requirements.txt

## Usage
1.	Launch the Streamlit application
2.	Configure Azure credentials in the sidebar
3.	Select voice and style
4.	Enter text
5.	Convert text to speech
6.	Preview and download audio

## Audio Format Options
1. 16KHz (Basic quality)
2. 24KHz (Recommended, balanced quality)
3.	48KHz (High quality)

## Key Configurations
1. Voice selection
2. Speaking style
3. Speaking rate (0.5 to 2.0)
4. Pitch adjustment (-50 to +50)

## Security Considerations
1. Store API keys securely
2. Use environment variables
3. Implement access controls

## Troubleshooting
1. Verify Azure credentials
2. Check network connectivity
3. Ensure output folder permissions
4. Monitor Azure service quotas


