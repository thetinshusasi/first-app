#%%
import torch, transformers
from transformers.utils import logging as hf_logging
print(torch.__version__)
print(transformers.__version__)
from typing import Literal
from transformers import pipeline

# Silence HF warning noise during quick experiments
hf_logging.set_verbosity_error()


sentiment_pipeline = pipeline(
    task="sentiment-analysis",
    framework="pt",
)
#%%

#%%
sentence_1 = "i had a great time at the movie it was really funny"
sentence_2 = "i had a great time at the movie but the parking was terrible"
sentence_3 = "i had a great time at the movie but the parking wasn't great"
sentence_4 = "i went to see a movie"

#%%
print(sentence_1)
print(sentiment_pipeline(sentence_1))

#%%
print(sentence_2)
print(sentiment_pipeline(sentence_2))

#%%
print(sentence_3)
print(sentiment_pipeline(sentence_3))

#%%
print(sentence_4)
print(sentiment_pipeline(sentence_4))

#%%