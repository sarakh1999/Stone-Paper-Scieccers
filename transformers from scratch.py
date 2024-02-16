import math
import torch
import torch.nn as nn


class InputEmbeddings(nn.Module):
    def __int__(self, d_model: int, vocab_size: int):
        super().__init__()
        self.d_model = d_model
        self.vocab_size = vocab_size
        self.embedding = nn.Embedding(vocab_size, d_model)

    #embedding is dictionary kind of number that maps the words to some same numbers every time
    # embedding size = 512
    def forward(self,x):
        # based on the paper, the embeddings are multiplied by the sqrt of the d_model
        return self.embedding(x) * math.sqrt(self.d_model)


class PositionalEmbedding(nn.Module):
    def __init__(self, d_model:int, seq_len:int, dropout:float) ->None:
        super().__init__()
        self.d_model = d_model
        self.seq_len = seq_len
        self.dropout = dropout
    # by positional embedding, we map each word to a vector with d_model size vector with some fixed numbers
    # positional embedding size = 512
    def forward(self,x):
        return nn.Embedding(PositionalEmbedding, vocab_size, d_model)



# %%
