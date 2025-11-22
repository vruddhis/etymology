from nltk.stem import WordNetLemmatizer

_lemmatizer = WordNetLemmatizer()

def get_root_form(word):

    word = word.lower().strip()

    root_verb = _lemmatizer.lemmatize(word, pos="v")
    if root_verb != word:
        return root_verb

    root_noun = _lemmatizer.lemmatize(word, pos="n")
    if root_noun != word:
        return root_noun

    return word
