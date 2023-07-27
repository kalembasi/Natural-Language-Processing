# this chatbot is smarter than first one
# it reduces unnecessary punctuations, find the root of the word, converts lower case, tokenizes, removes common words

import json
import os
import string
import nltk
# Import specific modules from NLTK library
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary NLTK data
nltk.download('punkt')  # This is for tokenizing
nltk.download('stopwords')  # This is for removing common words


def chat_bot():
    # Check if database file exists
    if os.path.exists("database_2.json"):
        # If file exists, open and load JSON data into 'database'
        with open('database_2.json', 'r') as f:
            database = json.load(f)
    else:
        # If file doesn't exist, start with an empty dictionary
        database = {}

    # Initialize stemmer (a tool for reducing words to their root form)
    stemmer = PorterStemmer()

    # Start the conversation loop
    while True:
        # Ask for user input and convert it to lowercase
        user_input = input("User: ").lower()

        # Remove punctuation from user input
        user_input = user_input.translate(str.maketrans('', '', string.punctuation))

        # Tokenize (split into individual words) the user input
        user_input = word_tokenize(user_input)

        # For each word in the user input, stem it (reduce it to root form)
        # and remove it if it is a common word (stopword), then join back into a string
        user_input = ' '.join([stemmer.stem(word) for word in user_input if word not in stopwords.words('english')])

        # Check if the processed input is in the database
        if user_input in database:
            # If it's in the database, print the corresponding response
            print("Bot: ", database[user_input])
        else:
            # If it's not in the database, ask for an appropriate response
            print("Bot: I don't know how to answer, give me an instance.")
            user_example = input("User: ")
            # Add the new input and response to the database
            database[user_input] = user_example

            # Save the updated database to the JSON file
            with open('database_2.json', 'w') as f:
                json.dump(database, f)


# Call the chat_bot function to start the chatbot
chat_bot()
