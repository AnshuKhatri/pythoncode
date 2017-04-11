Python 2.7.9 (default, Dec 10 2014, 12:28:03) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
import lshash

Traceback (most recent call last):
  File "<pyshell#0>", line 2, in <module>
    import lshash
ImportError: No module named lshash
>>> import lshash
>>> from lshash import LSHash
>>> lsh.index([1,2,3,4,5,6,7,8])

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    lsh.index([1,2,3,4,5,6,7,8])
NameError: name 'lsh' is not defined
>>> sh = LSHash(6, 8)
>>> lsh.index([1,2,3,4,5,6,7,8])lsh.index([2,3,4,5,6,7,8,9])
SyntaxError: invalid syntax
>>> lsh.index([1,2,3,4,5,6,7,8])

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    lsh.index([1,2,3,4,5,6,7,8])
NameError: name 'lsh' is not defined
>>> lsh = LSHash(6, 8)
>>> lsh.index([2,3,4,5,6,7,8,9])
>>> lsh.index([1,2,3,4,5,6,7,8])
>>> lsh.index([10,12,99,1,5,31,2,3])
>>> lsh.query([1,2,3,4,5,6,7,7])
[((1, 2, 3, 4, 5, 6, 7, 8), 1), ((2, 3, 4, 5, 6, 7, 8, 9), 11)]
>>> from hashlib import sha1
import numpy as np
from datasketch.minhash import MinHash
from datasketch.weighted_minhash import WeightedMinHashGenerator
from datasketch.lsh import WeightedMinHashLSH, MinHashLSH

data1 = ['minhash', 'is', 'a', 'probabilistic', 'data', 'structure', 'for',
        'estimating', 'the', 'similarity', 'between', 'datasets']
data2 = ['minhash', 'is', 'a', 'probability', 'data', 'structure', 'for',
        'estimating', 'the', 'similarity', 'between', 'documents']
data3 = ['minhash', 'is', 'probability', 'data', 'structure', 'for',
        'estimating', 'the', 'similarity', 'between', 'documents']

v1 = np.random.uniform(1, 10, 10)
v2 = np.random.uniform(1, 10, 10)
v3 = np.random.uniform(1, 10, 10)

def eg1():
    m1 = MinHash()
    m2 = MinHash()
    m3 = MinHash()
    for d in data1:
        m1.update(d.encode('utf8'))
    for d in data2:
        m2.update(d.encode('utf8'))
    for d in data3:
        m3.update(d.encode('utf8'))

    # Create LSH index
    lsh = MinHashLSH(threshold=0.5)
    lsh.insert("m2", m2)
    lsh.insert("m3", m3)
    result = lsh.query(m1)
    print("Approximate neighbours with Jaccard similarity > 0.5", result)

def eg2():
    mg = WeightedMinHashGenerator(10, 5)
    m1 = mg.minhash(v1)
    m2 = mg.minhash(v2)
    m3 = mg.minhash(v3)
    print("Estimated Jaccard m1, m2", m1.jaccard(m2))
    print("Estimated Jaccard m1, m3", m1.jaccard(m3))
    # Create LSH index
    lsh = WeightedMinHashLSH(threshold=0.1, sample_size=5)
    lsh.insert("m2", m2)
    lsh.insert("m3", m3)
    result = lsh.query(m1)
    print("Approximate neighbours with weighted Jaccard similarity > 0.1", result)

if __name__ == "__main__":
    eg1()
    eg2()

>>> 
>>> from datasketch import MinHash

data1 = ['minhash', 'is', 'a', 'probabilistic', 'data', 'structure', 'for',
        'estimating', 'the', 'similarity', 'between', 'datasets']
data2 = ['minhash', 'is', 'a', 'probability', 'data', 'structure', 'for',
        'estimating', 'the', 'similarity', 'between', 'documents']

m1, m2 = MinHash(), MinHash()
for d in data1:
    m1.update(d.encode('utf8'))
for d in data2:
    m2.update(d.encode('utf8'))
print("Estimated Jaccard for data1 and data2 is", m1.jaccard(m2))

s1 = set(data1)
s2 = set(data2)
actual_jaccard = float(len(s1.intersection(s2)))/float(len(s1.union(s2)))
print("Actual Jaccard for data1 and data2 is", actual_jaccard)
>>> 
>>> m = MinHash(num_perm=256)
>>> m.count()
0.0
>>> from sparselsh import LSH
from scipy.sparse import csr_matrix

X = csr_matrix( [
    [ 3, 0, 0, 0, 0, 0, -1],
    [ 0, 1, 0, 0, 0, 0,  1],
    [ 1, 1, 1, 1, 1, 1,  1] ])

# One class number for each input point
y = [ 0, 3, 10]

X_sim = csr_matrix( [ [ 1, 1, 1, 1, 1, 1, 0]])

lsh = LSH( 4,
           X.shape[1],
           num_hashtables=1,
           storage_config={"dict":None})

for ix in xrange(X.shape[0]):
    x = X.getrow(ix)
    c = y[ix]
    lsh.index( x, extra_data=c)

# find points similar to X_sim
lsh.query(X_sim, num_results=1)

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    from sparselsh import LSH
ImportError: No module named sparselsh
>>> 
>>> 
>>> 
>>> import numpy as np
from lshash import LSHash

tenthclosest = []  # for each test, record distance to the 10th closest point for a random query
for D in range(2, 11):  # Run tests for 2D through 10D
    X = np.random.normal(size=(200000, D))  # Fill the N-D space with 200k random vectors
    lsh = LSHash(hash_size=int(64 / D) + D, input_dim=D, num_hashtables=D)

    # query vector
    q = np.random.normal(size=(D,))
    q /= np.linalg.norm(q)

    distances = []
    for x in X:
        lsh.index(x)
        x /= np.linalg.norm(x)  # topic vectors are typically normalized
        distances += [1 - np.sum(x * q)]  # keep track of all the cosine distances to double check

    distances = sorted(distances)
    closest = lsh.query(x, distance_func='cosine')
    N = len(closest)
    rank = min(10, N)
    tenthclosest += [[D, N - 1, closest[rank - 1][-1] if N else None, distances[rank - 1]]]
    print(tenthclosest[-1])
    
>>> tenthclosest

Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    tenthclosest
NameError: name 'tenthclosest' is not defined
>>> tenthclosest = []
>>> [2, 3489, 1.8829024561739516e-08, 1.1039843927918014e-08]
[3, 6233, 9.0466236206676598e-05, 6.2791611406209924e-05]
[4, 1699, 0.0018897028187802034, 0.0012634980225747494]
[5, 1952, 0.0075433762917371805, 0.0075524749444468853]
[6, 2900, 0.020745774741610101, 0.01665383250767416]
[7, 1609, 0.033809202929906634, 0.033843151772571578]
[8, 1727, 0.051644443418475849, 0.058447769337895084]
[9, 944, 0.063525165688066543, 0.0689438997942875]
[10, 571, 0.091584156715659337, 0.079468392777439334]
>>> from datasketch import MinHash

data1 = ['minhash', 'is', 'a', 'probabilistic', 'data', 'structure', 'for',
        'estimating', 'the', 'similarity', 'between', 'datasets']
data2 = ['minhash', 'is', 'a', 'probability', 'data', 'structure', 'for',
        'estimating', 'the', 'similarity', 'between', 'documents']

m1, m2 = MinHash(), MinHash()
for d in data1:
    m1.update(d.encode('utf8'))
for d in data2:
    m2.update(d.encode('utf8'))
print("Estimated Jaccard for data1 and data2 is", m1.jaccard(m2))

s1 = set(data1)
s2 = set(data2)
actual_jaccard = float(len(s1.intersection(s2)))/float(len(s1.union(s2)))
print("Actual Jaccard for data1 and data2 is", actual_jaccard)
>>> from datasketch import MinHash
>>> data1 = ['minhash', 'is', 'a', 'probabilistic', 'data', 'structure', 'for',
        'estimating', 'the', 'similarity', 'between', 'datasets']
>>> data2 = ['minhash', 'is', 'a', 'probability', 'data', 'structure', 'for',
        'estimating', 'the', 'similarity', 'between', 'documents']
>>> m1, m2 = MinHash(), MinHash()
>>> for d in data1:
    m1.update(d.encode('utf8'))

    
>>> for d in data2:
    m2.update(d.encode('utf8'))

    
>>> print("Estimated Jaccard for data1 and data2 is", m1.jaccard(m2))
('Estimated Jaccard for data1 and data2 is', 0.7421875)
>>> 
>>> s1 = set(data1)

>>> 
>>> ctual_jaccard = float(len(s1.intersection(s2)))/float(len(s1.union(s2)))

Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    ctual_jaccard = float(len(s1.intersection(s2)))/float(len(s1.union(s2)))
NameError: name 's2' is not defined
>>> s2 = set(data2)
>>> actual_jaccard = float(len(s1.intersection(s2)))/float(len(s1.union(s2)))
>>> print("Actual Jaccard for data1 and data2 is", actual_jaccard)
('Actual Jaccard for data1 and data2 is', 0.7142857142857143)
>>> from hashlib import sha1

>>> import numpy as np
>>> from datasketch.minhash import MinHash
>>> from datasketch.weighted_minhash import WeightedMinHashGenerator
>>> from datasketch.lsh import WeightedMinHashLSH, MinHashLSH
>>> data1 = ['minhash', 'is', 'a', 'probabilistic', 'data', 'structure', 'for',
        'estimating', 'the', 'similarity', 'between', 'datasets']
>>> data2 = ['minhash', 'is', 'a', 'probability', 'data', 'structure', 'for',
        'estimating', 'the', 'similarity', 'between', 'documents']
>>> data3 = ['minhash', 'is', 'probability', 'data', 'structure', 'for',
        'estimating', 'the', 'similarity', 'between', 'documents']
>>> v1 = np.random.uniform(1, 10, 10)
>>> v2 = np.random.uniform(1, 10, 10)
>>> v3 = np.random.uniform(1, 10, 10)
>>> def eg1():
    m1 = MinHash()
    m2 = MinHash()
    m3 = MinHash()
    for d in data1:
        m1.update(d.encode('utf8'))
    for d in data2:
        m2.update(d.encode('utf8'))
    for d in data3:
        m3.update(d.encode('utf8'))

    # Create LSH index
    lsh = MinHashLSH(threshold=0.5)
    lsh.insert("m2", m2)
    lsh.insert("m3", m3)
    result = lsh.query(m1)
    print("Approximate neighbours with Jaccard similarity > 0.5", result)

    
>>> eg1()
('Approximate neighbours with Jaccard similarity > 0.5', ['m3', 'm2'])
>>> import nltk
>>> import string
>>> from collections import Counter
>>> from nltk.corpus import stopwords
>>> def get_tokens():
	with open("s1.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> count = Counter(tokens)
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> count
Counter({'function': 1, 'use': 1, 'corresponding': 1, 'features': 1, 'parameters': 1, 'positive': 1, 'image': 1, 'update': 1, 'gaussian': 1, 'penalty': 1, 'negative': 1, 'example': 1, 'examples': 1, 'apply': 1, 'semantic': 1, 'similar': 1, 'class': 1})
>>> data1=[]
>>> data1.extend(count)
>>> data1
['function', 'use', 'corresponding', 'features', 'parameters', 'positive', 'image', 'update', 'gaussian', 'penalty', 'negative', 'example', 'examples', 'apply', 'semantic', 'similar', 'class']
>>> def get_tokens():
	with open("s2.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> count = Counter(tokens)
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> count
Counter({'features': 3, 'nonrelevant': 1, 'use': 1, 'relevant': 1, 'positive': 1, 'negative': 1, 'examples': 1, 'deemphasize': 1, 'emphasize': 1})
>>> data2=[]
>>> data2.extend(count)
>>> 
>>> data2
['nonrelevant', 'use', 'relevant', 'features', 'positive', 'negative', 'examples', 'deemphasize', 'emphasize']
>>> def get_tokens():
	with open("s3.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> count = Counter(tokens)
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> count
Counter({'use': 1, 'kinds': 1, 'positive': 1, 'decision': 1, 'negative': 1, 'two': 1, 'refine': 1, 'images': 1, 'semantic': 1, 'boundary': 1, 'classify': 1, 'examples': 1})
>>> data3=[]
>>> data3.extenc(count)

Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    data3.extenc(count)
AttributeError: 'list' object has no attribute 'extenc'
>>> data3.extend(count)
>>> data3
['use', 'kinds', 'positive', 'decision', 'negative', 'two', 'refine', 'images', 'semantic', 'boundary', 'classify', 'examples']
>>> eg1()
('Approximate neighbours with Jaccard similarity > 0.5', [])
>>> def eg1():
    m1 = MinHash()
    m2 = MinHash()
    m3 = MinHash()
    for d in data1:
        m1.update(d.encode('utf8'))
    for d in data2:
        m2.update(d.encode('utf8'))
    for d in data3:
        m3.update(d.encode('utf8'))

    # Create LSH index
    lsh = MinHashLSH(threshold=0.01)
    lsh.insert("m2", m2)
    lsh.insert("m3", m3)
    result = lsh.query(m1)
    print("Approximate neighbours with Jaccard similarity > 0.5", result)

    
>>> eg1()
('Approximate neighbours with Jaccard similarity > 0.5', ['m3', 'm2'])
>>> def eg1():
    m1 = MinHash()
    m2 = MinHash()
    m3 = MinHash()
    for d in data1:
        m1.update(d.encode('utf8'))
    for d in data2:
        m2.update(d.encode('utf8'))
    for d in data3:
        m3.update(d.encode('utf8'))

    # Create LSH index
    lsh = MinHashLSH(threshold=0.01)
    lsh.insert("m2", m2)
    lsh.insert("m3", m3)
    result = lsh.query(m1)
    print("Approximate neighbours with Jaccard similarity > 0.01", result)

    
>>> eg1()
('Approximate neighbours with Jaccard similarity > 0.01', ['m3', 'm2'])
>>> 






    





















    



