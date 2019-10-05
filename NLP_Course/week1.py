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