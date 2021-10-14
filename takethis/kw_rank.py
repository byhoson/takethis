import json
import os

import numpy as np

# paths
PROJECT_HOME = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
GLOSSARY_PATH = os.path.join(PROJECT_HOME, 'course/glossary.txt')
KW_CACHE_PATH = os.path.join(PROJECT_HOME, '.cache/foo')

cache_keywords_set = None

def get_rank(career):
    global cache_keywords_set

    if cache_keywords_set == None:
        cache_keywords_set = set()
        with open(GLOSSARY_PATH) as f:
            cache_keywords_set = set(f.read().splitlines())

    result = dict()
    for keyword in cache_keywords_set:
        result.update({keyword:keyword_sim(keyword, career, measure=0)})

    return result

def keyword_sim(word1, word2, measure=0):
    if measure == 0:
        # returns random floats in the half open interval [0.0, 1.0)
        return np.random.random_sample()

    elif measure == 1:
        return 0.5

    else:
        return 0.5

def spacy_sim():
    import spacy

    nlp = spacy.load('en_core_web_md')

    print("Enter two space-separated words")
    words = input()

    tokens = nlp(words)

    for token in tokens:
        # Printing the following attributes of each token.
        # text: the word string, has_vector: if it contains
        # a vector representation in the model,
        # vector_norm: the algebraic norm of the vector,
        # is_oov: if the word is out of vocabulary.
        print(token.text, token.has_vector, token.vector_norm, token.is_oov)

    token1, token2 = tokens[0], tokens[1]

    print("Similarity:", token1.similarity(token2))


def google_sim():
    pass
