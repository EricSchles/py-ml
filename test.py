from gensim.test.utils import common_texts
from gensim.sklearn_api import W2VTransformer
import code

# Create a model to represent each word by a 10 dimensional vector.
model = W2VTransformer(size=10, min_count=1, seed=1)

# What is the vector representation of the word 'graph'?
wordvecs = model.fit(common_texts).transform(['graph', 'system'])
assert wordvecs.shape == (2, 10)
code.interact(local=locals())
