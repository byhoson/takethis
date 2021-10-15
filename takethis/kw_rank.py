import json
import os
import numpy as np

from apiclient.discovery import build

# paths
PROJECT_HOME = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
GLOSSARY_PATH = os.path.join(PROJECT_HOME, 'course/glossary.txt')
KW_CACHE_PATH = os.path.join(PROJECT_HOME, '.cache/keywords_google.json')
API_KEY_PATH = os.path.join(PROJECT_HOME, 'takethis/.api_keys')

cache_keywords_set = None
cache_keywords_google = None
flag_cache_keywords_google_update = False

credentials_index = 0
credentials = None

def get_rank(career):
    global cache_keywords_set

    if cache_keywords_set == None:
        cache_keywords_set = set()
        with open(GLOSSARY_PATH) as f:
            cache_keywords_set = set(f.read().splitlines())

    result = dict()
    for keyword in cache_keywords_set:
        result.update({keyword:keyword_sim(keyword, career, measure=2)})

    return result

def keyword_sim(word1, word2, measure=0):
    if measure == 0:
        # returns random floats in the half open interval [0.0, 1.0)
        return np.random.random_sample()

    elif measure == 1:
        return 0.5

    else:
        return google_sim(word1, word2)

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


def get_google_query(query):
    global cache_keywords_google
    global flag_cache_keywords_google_update
    if cache_keywords_google == None:
        try:
            with open(KW_CACHE_PATH, 'r') as json_cache:
                cache_keywords_google = json.load(json_cache)
        except:
            cache_keywords_google = dict()

    
    if query in cache_keywords_google:
        # Cache hit
        return cache_keywords_google[query]
    else:
        # Cache miss
        flag_cache_keywords_google_update = True

        if len(api_key_list) == 0:
            try:
                with open(API_KEY_PATH, 'r') as json_cache:
                    credentials = json.load(json_cache)
            except:
                print('*** Failed to get api keys for google search ***')
                freq = 1

        else:
            api_key_index = (api_key_index + 1) % len(api_key_list)
            resource = build('customsearch', 'v1', developerKey=credentials['api_key']).cse()
            result = resource.list(q=query, cx=credentials['search_engine_id']).execute()
            freq = result['queries']['totalResults']

        cache_keywords_google[query] = freq
        return cache_keywords_google[query]
        

def google_sim(word1, word2):
    EPSILON = 1e-7
    g_word1 = get_google_query(word1)
    g_word2 = get_google_query(word2)
    g_word1_and_word2 = get_google_query(word1 + ' AND ' + word2)
    return g_word1_and_word2 / (g_word1 + g_word2 + EPSILON)


def update_cache_google_keywords():
    assert cache_keywords_google != None
    with open(KW_CACHE_PATH, 'w') as json_cache:
        json.dump(cache_keywords_google, json_cache)


