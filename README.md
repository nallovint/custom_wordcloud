# Custom Word Cloud Generator

This project generates a word cloud image from a text file, with the size of each word proportional to its frequency in the text. The program focuses on descriptive words by including only nouns and adjectives, and filters out common stopwords (like 'the', 'and', 'or').

## Features
- Reads text from a user-specified file in the project root
- Filters out common English stopwords
- Only includes nouns and adjectives in the word cloud
- Displays the top 15 nouns/adjectives and their frequencies in the terminal
- Generates a word cloud image with a name based on the input file (e.g., `frankenstein_wordcloud.png`)

## How It Works
1. **Prompt for Filename:** The program asks the user to enter the name of a text file in the project root directory.
2. **Text Processing:**
   - Converts text to lowercase and removes special characters
   - Tokenizes the text into words
   - Removes stopwords (common words that add little meaning)
   - Uses part-of-speech (POS) tagging to keep only nouns and adjectives
   - Counts the frequency of each remaining word
3. **Display Top Words:** Prints the top 15 nouns/adjectives and their frequencies in the terminal.
4. **Word Cloud Generation:**
   - Places words randomly on a canvas, avoiding overlap
   - Sizes each word based on its frequency
   - Uses random dark colors for readability
   - Saves the result as `[input_filename]_wordcloud.png`

## Library Usage
- **nltk** (Natural Language Toolkit):
  - `word_tokenize`: Splits text into individual words
  - `stopwords`: Provides a list of common English stopwords to filter out
  - `pos_tag`: Tags each word with its part of speech (noun, adjective, etc.)
  - `download`: Ensures required NLTK data is available
- **Pillow (PIL):**
  - `Image`, `ImageDraw`, `ImageFont`: Used to create and draw the word cloud image
- **collections.Counter:**
  - Counts the frequency of each word
- **random:**
  - Randomizes word placement and color for the word cloud
- **re:**
  - Cleans the text by removing special characters

## Setup & Usage
1. **Clone the repository and navigate to the project folder.**
2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Add your text file** (e.g., `frankenstein.txt`) to the project root.
5. **Run the program:**
   ```bash
   python custom_wordcloud.py
   ```
6. **When prompted, enter the filename** (e.g., `frankenstein.txt`).
7. **View the generated word cloud** in `[input_filename]_wordcloud.png`.

## Example
```
Please enter the name of your text file (e.g., 'sample.txt'):
frankenstein.txt

Top 15 nouns and adjectives and their frequencies:
----------------------------------------
monster          :  50 times (Noun)
strange          :  30 times (Adjective)
...
----------------------------------------
Word cloud has been generated as 'frankenstein_wordcloud.png'
```

## Notes
- Only the top 100 most frequent nouns and adjectives are included in the word cloud.
- The program will print an error if the specified file is not found.
- The word cloud image is named based on the input file (e.g., `frankenstein_wordcloud.png`).

---
Feel free to modify the code to adjust the appearance or filtering logic to suit your needs! 