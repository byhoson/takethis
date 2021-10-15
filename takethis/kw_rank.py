import json
import os
import numpy as np

from apiclient.discovery import build

# paths
PROJECT_HOME = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
GLOSSARY_PATH = os.path.join(PROJECT_HOME, 'course/sample-glossary.txt')
CACHE_GLOSSARY_PATH = os.path.join(PROJECT_HOME, '.cache/cache_glossary.json')

API_KEY="AIzaSyCZUjk1AQaJE77rbhPntW9ILbVOMy9jvvI"

keywords = None
cache_glossary = None
cache_career = None
g_career = None # google, total result for career 

def get_rank(career):
    global cache_glossary
    global cache_career
    global keywords
    global g_career

    cache_career = None 

    if cache_glossary == None:
        try:
            with open(CACHE_GLOSSARY_PATH, 'r') as json_file:
                cache_glossary = json.load(json_file)
        except:
            print('[kw_rank]: missing cache_glossary error')
            exit(1)


    if keywords is None:
        with open(GLOSSARY_PATH) as txt_file:
            keywords = txt_file.read().splitlines()

    career_filename = career.replace(' ', '_')

    try:
        with open(os.path.join(PROJECT_HOME, '.cache/' + career_filename + '.json'), 'r') as json_file:
            cache_career = json.load(json_file)
    except:
        print('[cache miss!]: creating an new one for ' + career)
        # CACHE MISS!
        # BUILD cache_[career] FOR NEW CAREER
        # json dump
        cache_career = dict()

        for keyword in keywords:
            cache_career[keyword] = google_query(keyword + ' AND ' + career)

        career_filename = career.replace(' ', '_')
        with open(os.path.join(PROJECT_HOME, '.cache/' + career_filename + '.json'), 'w') as json_file:
            json.dump(cache_career, json_file)

    # ASSERT (CACHE_CAREER != NONE)
    g_career = google_query(career)

    result = dict()

    for keyword in keywords:
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



def google_query(query_string):
    # TODO call API
    # ret: total number of results

    resource = build("customsearch", 'v1', developerKey=API_KEY).cse()
    result = resource.list(q=query_string, cx='009557628044748784875:5lejfe73wrw').execute()

    if result == None:
        print('*** API CALL ERROR ***')
        exit(-1)

    return int(result['searchInformation']['totalResults'])


def google_sim(keyword, career):
    global cache_glossary
    global cache_career
    global g_career

    EPSILON = 1e-7
    g_keyword = cache_glossary[keyword]
    return cache_career[keyword] / (g_keyword + g_career - cache_career[keyword] + EPSILON)


if __name__ == '__main__':
    career = input()
    result = get_rank(career)
    print(result)
