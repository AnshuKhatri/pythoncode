Python 2.7.9 (default, Dec 10 2014, 12:28:03) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import sys
>>> SHINGLE_SIZE = 5
>>> ef get_shingles(f, size):
    shingles = set()
    buf = f.read() # read entire file
    for i in range(0, len(buf)-size+1):
        yield buf[i:i+size]
        
SyntaxError: invalid syntax
>>> def get_shingles(f, size):
    shingles = set()
    buf = f.read() # read entire file
    for i in range(0, len(buf)-size+1):
        yield buf[i:i+size]

        
>>> def jaccard(set1, set2):
    x = len(set1.intersection(set2))
    y = len(set1.union(set2))
    return x / float(y)

>>> file1 = sys.argv[1]
file2 = sys.argv[2]

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    file1 = sys.argv[1]
IndexError: list index out of range
>>> file1 = sys.argv[1]

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    file1 = sys.argv[1]
IndexError: list index out of range
>>> file1="s1.txt"
>>> file2="s2.txt"
>>> file1
's1.txt'
>>> fil1="Use the features of the positive examples to update the parameters of the corresponding semantic Gaussian class. Apply penalty function to an image similar to a negative example."
>>> file1="Use the features of the positive examples to update the parameters of the corresponding semantic Gaussian class. Apply penalty function to an image similar to a negative example."
>>> file2="Use the features of the positive and negative examples to emphasize relevant features and de-emphasize the nonrelevant features."
>>> with open(file1) as f1, open(file2) as f2:
    shingles1 = set(get_shingles(f1, size=SHINGLE_SIZE))
    shingles2 = set(get_shingles(f2, size=SHINGLE_SIZE))

    

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    with open(file1) as f1, open(file2) as f2:
IOError: [Errno 2] No such file or directory: 'Use the features of the positive examples to update the parameters of the corresponding semantic Gaussian class. Apply penalty function to an image similar to a negative example.'
>>> shingles1 = set(get_shingles(file1, size=SHINGLE_SIZE))

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    shingles1 = set(get_shingles(file1, size=SHINGLE_SIZE))
  File "<pyshell#4>", line 3, in get_shingles
    buf = f.read() # read entire file
AttributeError: 'str' object has no attribute 'read'
>>> import string
>>> shingles1 = set(get_shingles(file1, size=SHINGLE_SIZE))

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    shingles1 = set(get_shingles(file1, size=SHINGLE_SIZE))
  File "<pyshell#4>", line 3, in get_shingles
    buf = f.read() # read entire file
AttributeError: 'str' object has no attribute 'read'
>>> theString = "the quick brown fox jumps over the lazy dog. now is the time for all good men to come to the aid of the party"
>>> shingleLength = 3
>>> tokens = theString.split()
>>> print [tokens[i:i+shingleLength] for i in range(len(tokens) - shingleLength + 1) if len(tokens[i]) < 4]
[['the', 'quick', 'brown'], ['fox', 'jumps', 'over'], ['the', 'lazy', 'dog.'], ['now', 'is', 'the'], ['is', 'the', 'time'], ['the', 'time', 'for'], ['for', 'all', 'good'], ['all', 'good', 'men'], ['men', 'to', 'come'], ['to', 'come', 'to'], ['to', 'the', 'aid'], ['the', 'aid', 'of'], ['aid', 'of', 'the'], ['of', 'the', 'party']]
>>> data1

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    data1
NameError: name 'data1' is not defined
>>> data1

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    data1
NameError: name 'data1' is not defined
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> str="Use the features of the positive examples to update the parameters of the corresponding semantic Gaussian class. Apply penalty function to an image similar to a negative example."
>>> shingleLength = 9
>>> tokens = theString.split()
>>> print [tokens[i:i+shingleLength] for i in range(len(tokens) - shingleLength + 1) if len(tokens[i]) < 10]
[['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.'], ['quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.', 'now'], ['brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.', 'now', 'is'], ['fox', 'jumps', 'over', 'the', 'lazy', 'dog.', 'now', 'is', 'the'], ['jumps', 'over', 'the', 'lazy', 'dog.', 'now', 'is', 'the', 'time'], ['over', 'the', 'lazy', 'dog.', 'now', 'is', 'the', 'time', 'for'], ['the', 'lazy', 'dog.', 'now', 'is', 'the', 'time', 'for', 'all'], ['lazy', 'dog.', 'now', 'is', 'the', 'time', 'for', 'all', 'good'], ['dog.', 'now', 'is', 'the', 'time', 'for', 'all', 'good', 'men'], ['now', 'is', 'the', 'time', 'for', 'all', 'good', 'men', 'to'], ['is', 'the', 'time', 'for', 'all', 'good', 'men', 'to', 'come'], ['the', 'time', 'for', 'all', 'good', 'men', 'to', 'come', 'to'], ['time', 'for', 'all', 'good', 'men', 'to', 'come', 'to', 'the'], ['for', 'all', 'good', 'men', 'to', 'come', 'to', 'the', 'aid'], ['all', 'good', 'men', 'to', 'come', 'to', 'the', 'aid', 'of'], ['good', 'men', 'to', 'come', 'to', 'the', 'aid', 'of', 'the'], ['men', 'to', 'come', 'to', 'the', 'aid', 'of', 'the', 'party']]
>>> 
