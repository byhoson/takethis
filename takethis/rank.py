def build_career_sig(career):
    pass

def keyword_sim(word1, word2, measure=0):
    if measure == 0:
        return 0.5 #TODO make it random
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
