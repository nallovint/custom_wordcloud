import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from PIL import Image, ImageDraw, ImageFont
import random
import re
from collections import Counter
import math

def download_nltk_data():
    # Download required NLTK data
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('punkt_tab')
    nltk.download('averaged_perceptron_tagger_eng')

def process_text(text):
    # Process text to remove stopwords and get meaningful words, and convert to lowercase and remove special characters
    text = re.sub(r'[^\w\s]', '', text.lower())
    
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Get English stopwords
    stop_words = set(stopwords.words('english'))
    
    # POS tag the tokens
    pos_tags = pos_tag(tokens)
    
    # Filter for nouns (NN*) and adjectives (JJ*), and remove stopwords and short words
    filtered_words = [
        word for word, tag in pos_tags 
        if (tag.startswith('NN') or tag.startswith('JJ'))  # Only nouns and adjectives
        and word not in stop_words 
        and len(word) > 2
    ]
    
    # Count word frequencies
    word_freq = Counter(filtered_words)
    
    # Get top 100 words
    top_words = dict(word_freq.most_common(100))
    
    # Print top 15 words and their frequencies
    print("\nTop 15 nouns and adjectives and their frequencies:")
    print("-" * 40)
    for word, freq in list(word_freq.most_common(15)):
        # Get the POS tag for this word
        word_tag = next((tag for w, tag in pos_tags if w.lower() == word), '')
        pos_type = "Noun" if word_tag.startswith('NN') else "Adjective"
        print(f"{word:15} : {freq:3d} times ({pos_type})")
    print("-" * 40 + "\n")
    
    return top_words

def get_word_size(freq, max_freq, min_size=20, max_size=100):
    # Calculate font size based on word frequency
    return min_size + (max_size - min_size) * (freq / max_freq)

def get_random_color():
    # Generate a random bright color for better contrast against black background
    return (
        random.randint(150, 255),  # Brighter colors for better visibility
        random.randint(150, 255),
        random.randint(150, 255)
    )

def is_overlapping(x, y, width, height, placed_words):
    # Check if a word overlaps with any previously placed words
    for word_info in placed_words:
        if (x < word_info['x'] + word_info['width'] and
            x + width > word_info['x'] and
            y < word_info['y'] + word_info['height'] and
            y + height > word_info['y']):
            return True
    return False

def generate_custom_wordcloud(text, output_file='custom_wordcloud.png'):
    # Generate a custom word cloud using PIL
    # Process text to get word frequencies
    word_freq = process_text(text)
    
    # Image settings
    width = 1200
    height = 800
    background_color = (0, 0, 0)  # Black background
    
    # Create image and drawing context
    image = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(image)
    
    # Load font (using default system font)
    base_font = ImageFont.load_default()
    
    # Sort words by frequency (descending)
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    max_freq = sorted_words[0][1]
    
    # Store placed words information
    placed_words = []
    
    # Try to place each word
    for word, freq in sorted_words:
        # Calculate font size based on frequency
        font_size = int(get_word_size(freq, max_freq))
        font = ImageFont.truetype("Arial", font_size)
        
        # Get word dimensions
        bbox = draw.textbbox((0, 0), word, font=font)
        word_width = bbox[2] - bbox[0]
        word_height = bbox[3] - bbox[1]
        
        # Try to place the word
        max_attempts = 100
        placed = False
        
        for _ in range(max_attempts):
            # Random position
            x = random.randint(0, width - word_width)
            y = random.randint(0, height - word_height)
            
            # Check for overlap
            if not is_overlapping(x, y, word_width, word_height, placed_words):
                # Draw the word
                draw.text((x, y), word, font=font, fill=get_random_color())
                
                # Store word information
                placed_words.append({
                    'x': x,
                    'y': y,
                    'width': word_width,
                    'height': word_height
                })
                
                placed = True
                break
        
        if not placed:
            print(f"Could not place word: {word}")
    
    # Save the image
    image.save(output_file, 'PNG')
    print(f"Word cloud has been generated as '{output_file}'")

def main():
    # Download required NLTK data
    download_nltk_data()
    
    # Get input filename from user
    print("Please enter the name of your text file (e.g., 'sample.txt'):")
    filename = input().strip()
    
    try:
        # Read the text file
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Generate output filename by removing .txt extension
        output_filename = filename.rsplit('.', 1)[0] + '_wordcloud.png'
        
        # Generate word cloud
        generate_custom_wordcloud(text, output_file=output_filename)
        print(f"Word cloud has been generated as '{output_filename}'")
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found in the current directory.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main() 