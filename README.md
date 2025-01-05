# PDF-to-MP3-Converter

This script converts the text content of a PDF file into audible speech using Python libraries pdfplumber for extracting text from PDF files and pyttsx3 for text-to-speech conversion.

Libraries Used:

-pdfplumber: For extracting text from PDF files.

-pyttsx3: For converting text to speech.

Features

-Extracts text from a PDF file.

-Converts the extracted text to audio.

-Offers the option to save the audio to a file or play it in real-time.

Notes

-Ensure the PDF file is not password-protected and contains selectable text (not scanned images).

-Adjust the speech rate and volume in the engine.setProperty calls if needed.
