import nltk
text= "This is Andrew's text, isn't it?"
tokenizer = nltk.tokenize.WhitespaceTokenizer()
tt = tokenizer.tokenize(text)
print(tt)

tokenizer = nltk.tokenize.TreebankWordTokenizer()
tt = tokenizer.tokenize(text)
print(tt)

tokenizer  = nltk.tokenize.WordPunctTokenizer()
tt = tokenizer.tokenize(text)
print(tt)

text = "feet cats wolves talked"
tokenizer = nltk.tokenize.TreebankWordTokenizer()
tokens = tokenizer.tokenize(text)
stemmer = nltk.stem.PorterStemmer()
tt = " ".join(stemmer.stem(token) for token in tokens)
print(tt)

stemmer = nltk.stem.WordNetLemmatizer()
tt = " ".join(stemmer.lemmatize(token) for token in tokens)
print(tt)