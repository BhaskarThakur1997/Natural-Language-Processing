# Tokenization of paragraphs/sentences

import nltk

paragraph = " I looked at the stars, and considered how awful it would be for a man to turn his face up to them as he froze to death, and see no help or pity in all the glittering multitude."

# Tokenizing sentences

sentences = nltk.sent_tokenize(paragraph)

# Tokenizing words

words = nltk.word_tokenize(paragraph)
