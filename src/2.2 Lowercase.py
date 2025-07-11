#%%

sentence = "Her 22 cat's name is Luna"
print(sentence)

#%%

sentence = "Her 22 cat's name is Luna"
print(sentence.lower())

#%%

# Adding a larger sentence
long_sentence = "The quick brown fox jumps over the lazy dog while the magnificent rainbow stretches across the vast sky, creating a breathtaking spectacle that captivates all who witness its beauty."
print(long_sentence)
print(long_sentence.lower())

#%%

sentence_list = [
    "Hello World",
    "Goodbye World 1",
]
print([sentence.lower() for sentence in sentence_list])
# %%


#%%

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

english_stopwords = stopwords.words('english')
print( len(english_stopwords))

lowercase_sentence  = "The quick brown fox jumps over the lazy dog while the magnificent rainbow".lower()
print([word for word in lowercase_sentence.split() if word not in english_stopwords])


#%%
# %%