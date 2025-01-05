import pdfplumber #Library to extrace PDF files
import pyttsx3 #Text to Speech conversion library

def pdf_to_audio(pdf_path, output_audio_path=None):
    try:
        # Initialize text-to-speech engine
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # Speed of speech (words per minute)
        engine.setProperty('volume', 0.9)  # Volume 
        
        # Extract text from PDF
        with pdfplumber.open(pdf_path) as pdf:
            full_text = ""
            for page in pdf.pages:
                full_text += page.extract_text() + "\n"
        
        # Read text aloud
        print("Converting PDF text to audio...")
        if output_audio_path:
            engine.save_to_file(full_text, output_audio_path)
        else:
            engine.say(full_text)
        engine.runAndWait()

        print("Conversion complete!")
        if output_audio_path:
            print(f"Audio saved to: {output_audio_path}")
    except Exception as e:
        print(f"Error: {e}")

# Provide the path to your PDF file
pdf_path = r"C:\Users\Invcuser_96\Documents\Projects\Data_Science\PDF_Reader\sample.pdf" 
# Update the file name as needed if None is given audio will be played live
output_audio_path = None

# Convert PDF to audio
pdf_to_audio(pdf_path, output_audio_path)
