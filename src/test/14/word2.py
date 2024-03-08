import nltk
import random
import time

from tti_2 import generate

nltk.download('wordnet')

from nltk.corpus import wordnet

def get_random_word_and_definition():
    synsets = list(wordnet.all_synsets())
    random_synset = random.choice(synsets)
    random_word = random_synset.lemmas()[0].name()
    definition = random_synset.definition()
    return random_word, definition

while True:
    random_word, definition = get_random_word_and_definition()
    print(f"Rastgele Kelime: {random_word}")
    print(f"Tanım: {definition}")
    generate(word=random_word,definition=definition)    
    time.sleep(30)
