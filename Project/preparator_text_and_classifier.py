import pickle, re, simplemma, nltk
from nltk.corpus import stopwords

def preprocessing_text(text, stopwords_language):
    # rid off punctation
    text = re.sub(r'[^\w\s]', "", text)
    lematization = ''

    # lematization
    langdata = simplemma.load_data('de')
    for word in text.split():
        lematization += ' ' + simplemma.lemmatize(word, langdata)

    # rid off stopwords
    nltk.download('stopwords')
    stop = stopwords.words(stopwords_language)
    text_cleared = ''
    for word in lematization.split():
        if word not in stop:
            text_cleared += " " + word.lower()
    return text_cleared


def get_classifier(classifier):
    return pickle.load(open(f'{classifier}.pkl', 'rb'))


def get_TFIDF():
    return pickle.load(open(f'TFIDF.pkl', 'rb'))
