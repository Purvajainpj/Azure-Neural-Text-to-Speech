# Azure Neural Text-to-Speech Streamlit Application

## Overview
Azure Neural Text-to-Speech (TTS) is a powerful Streamlit-based application that converts text into natural-sounding speech using advanced neural network models.
Features

### Multilingual Voices

Support for multiple languages in a single voice
Voices: Ava, Jenny, Ada, Ollie (US and UK Multilingual)


### HD Voice Technology

Crystal-clear audio quality
Premium voices: Ava HD, Emma HD, Jenny HD, Andrew HD, Steffan HD


### Emotional Voice Styles

Multiple emotional styles available
Voices: Aria, Davis, Guy
Styles include: Neutral, angry, cheerful, excited, friendly, and more



## Prerequisites

• Python 3.6+
• Azure account with Speech Service enabled
• Azure Speech API key and region

## Installation

• Clone the repository
• Install dependencies:
• pip install -r requirements.txt


## Usage

• Launch the Streamlit application 
• Configure Azure credentials in the sidebar 
• Select voice and style 
• Enter text 
• Convert text to speech 
• Preview and download audio 

## Audio Format Options

• 16KHz (Basic quality)
• 24KHz (Recommended, balanced quality)
• 48KHz (High quality)

## Key Configurations

• Voice selection
• Speaking style
• Speaking rate (0.5 to 2.0)
• Pitch adjustment (-50 to +50)

## Security Considerations

• Store API keys securely
• Use environment variables
• Implement access controls

## Troubleshooting

• Verify Azure credentials
• Check network connectivity
• Ensure output folder permissions
• Monitor Azure service quotas
