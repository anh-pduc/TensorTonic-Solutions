import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    word2idx = {item: i for i, item in enumerate(vocab)}
    indices = [word2idx[token] for token in tokens if token in word2idx]
    out = np.bincount(indices, minlength = len(vocab))
    return out
            
    pass