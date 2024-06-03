import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import wikipedia

# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')
# nltk.download('punkt')
# nltk.download('omw-1.4')

text = wikipedia.page('Vegetables').content


lemmatizer = WordNetLemmatizer()

def lemma_me(sent):
    sentence_tokens = nltk.word_tokenize(sent.lower())
    pos_tags = nltk.pos_tag(sentence_tokens) #type of the words ( verb, noum, adverb, etc)

    sentence_lemmas = []

    for token, pos_tag in zip(sentence_tokens, pos_tags):
        if pos_tag[1][0].lower() in ['n', 'v', 'a','r']:
            lemma = lemmatizer.lemmatize(token, pos_tag[1][0].lower())
            sentence_lemmas.append(lemma)
            
    return sentence_lemmas

def process(text, question):
    sentence_tokens = nltk.sent_tokenize(text)
    sentence_tokens.append(question)

    tv = TfidfVectorizer(tokenizer = lemma_me )
    tf = tv.fit_transform(sentence_tokens)
    values = cosine_similarity(tf[-1], tf ) 
    index = values.argsort()[0][-2]
    values_flat = values.flatten()
    values_flat.sort()
    coeff = values_flat[-2]
    if coeff > 0.3:
        return sentence_tokens[index]


while True:
    question =  input("\033[93mHi, what do you want to know?\033[0m \n")
    output = process(text=text, question=question)
    print(f'\033[93m{output}\033[0m\n')
    if output:
        print(output)
    elif question == 'quit':
        break
    else:
        print("I don't know.")