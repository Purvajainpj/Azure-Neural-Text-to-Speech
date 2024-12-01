# Azure-Text-to-Speech
## Overview
Azure Neural Text-to-Speech (TTS) is a powerful service that converts text into natural-sounding speech using advanced neural network models. This Streamlit-based application provides a user-friendly interface to interact with Azure's Speech Service, offering various voices, styles, and customization options.

## Multilingual Capabilities
Support for multiple languages in a single voice

Seamless language switching without changing voices

Natural pronunciation across languages

Key multilingual voices include:

Ava (US Multilingual) with advanced style controls

Jenny (US Multilingual) for versatile language support

Ada and Ollie (UK Multilingual) for British English variations

HD Voice Technology
Crystal-clear audio quality with HD neural voices

Enhanced naturalness and clarity

Premium voice options including:

Ava HD for professional applications

Emma HD for clear, natural speech

Jenny HD for high-quality presentations

Andrew HD and Steffan HD for male voice options

Optimal for professional content and production

## Prerequisites
Python 3.6 or higher

Azure account with Speech Service enabled

Azure Speech API key and region

Required Python packages (specified in requirements.txt)

## Installation
Clone the repository

Install the required dependencies:

pip install -r requirements.txt

## Key Features
Voice Options
Multilingual Voices

Ava (US Multilingual)

Styles: Default, Advertisement, Conversation, Social_media, Speech, Sports, Story, Recipe, Disfluent

Jenny (US Multilingual)

Ada (UK Multilingual)

Ollie (UK Multilingual)

HD Voices

Ava (US HD)

Emma (US HD)

Jenny (US HD)

Andrew (US HD)

Steffan (US HD)

Emotional Voices

Aria (Female, US)

Davis (Male, US)

Guy (Male, US)

Styles: Neutral, angry, cheerful, excited, friendly, hopeful, sad, shouting, terrified, unfriendly, whispering

## Audio Format Options
Riff16Khz16BitMonoPcm (Basic quality, smaller file size)

Riff24Khz16BitMonoPcm (Standard quality, balanced file size - recommended)

Riff48Khz16BitMonoPcm (High quality, larger file size)

## Usage Guide
Configuration
Launch the Streamlit application

In the sidebar, enter your:

Azure Speech API Key

Azure Region

Desired output folder

Preferred audio format

Voice Settings
Select a voice from the dropdown menu

Choose a speaking style (if available for the selected voice)

Adjust voice modifications:

Speaking Rate (0.5 to 2.0)

Pitch Adjustment (-50 to +50)

Text Input and Conversion
Enter your text in the text area

Supports multiple languages

Accommodates long-form content

Click "Convert to Speech" to generate audio

Preview the generated audio directly in the browser

Download the audio file using the provided button

## Technical Details

SSML Generation
The application automatically generates SSML (Speech Synthesis Markup Language) with:

Voice selection

Style configuration

Prosody controls (rate and pitch)

XML escaping for special characters

Error Handling
Validates Azure credentials

Provides clear error messages for troubleshooting

Handles synthesis cancellation scenarios

Best Practices
Use appropriate audio format based on your needs:

Choose 16KHz for basic voice applications

Use 24KHz for standard applications

Select 48KHz for professional audio requirements

Voice Style Selection:

Match the style to your content type

Test different styles for optimal results

Consider using emotional styles for more engaging content

Performance Optimization:

Keep SSML well-formed

Use appropriate output folders

Monitor API usage

## Troubleshooting
Verify Azure credentials are correct

Ensure proper network connectivity

Check output folder permissions

Verify SSML syntax if using custom markup

Monitor Azure service quotas and limits

## Security Considerations
Store API keys securely

Use environment variables for sensitive data

Implement proper access controls for output files

Monitor and audit API usage
