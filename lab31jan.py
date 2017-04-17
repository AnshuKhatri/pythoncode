Python 2.7.9 (default, Dec 10 2014, 12:28:03) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import nltk
>>> import string
>>> import xlwt
i
>>> import xlrd
>>> from collections import Counter
>>> from nltk.corpus import stopwords
>>> book = xlwt.Workbook(encoding="utf-8")
>>> sheet1 = book.add_sheet("Sheet 1")
>>> book.close()

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    book.close()
AttributeError: 'Workbook' object has no attribute 'close'
>>> def  minEditDistR(target, source):
   """ Minimum edit distance. Straight from the recurrence. """

   i = len(target); j = len(source)

   if i == 0:  return j
   elif j == 0: return i

   return(min(minEditDistR(target[:i-1],source)+1,
              minEditDistR(target, source[:j-1])+1,
              minEditDistR(target[:i-1], source[:j-1])+substCost(source[j-1], target[i-1])))

>>> 
>>> def substCost(x,y):
    if x == y: return 0
    else: return 2

    
>>> 
>>> ref1="kitten"
>>> ref1
'kitten'
>>> ref2="sitting"
>>> ref2
'sitting'
>>> minEditDistR(ref1, ref2)
5
>>> ref1 = "intention"
>>> ref2 = "execution"
>>> minEditDistR(ref1, ref2)
8

>>> def  minEditDist(target, source):
    ''' Computes the min edit distance from target to source. Figure 3.25 '''
    
    n = len(target)
    m = len(source)

    distance = [[0 for i in range(m+1)] for j in range(n+1)]

    for i in range(1,n+1):
        distance[i][0] = distance[i-1][0] + insertCost(target[i-1])

    for j in range(1,m+1):
        distance[0][j] = distance[0][j-1] + deleteCost(source[j-1])

    for i in range(1,n+1):
        for j in range(1,m+1):
           distance[i][j] = min(distance[i-1][j]+1,
                                distance[i][j-1]+1,
                                distance[i-1][j-1]+substCost(source[j-1],target[i-1]))
    return distance[n][m]

>>> minEditDistR(ref1, ref2)
8
>>> ref1="kitten"
>>> ref2="sitting"
>>> minEditDistR(ref1, ref2)
5
>>> def levenshtein_distance(first, second):
    """Find the Levenshtein distance between two strings."""
    if len(first) > len(second):
        first, second = second, first
    if len(second) == 0:
        return len(first)
    first_length = len(first) + 1
    second_length = len(second) + 1
    distance_matrix = [[0] * second_length for x in range(first_length)]
    for i in range(first_length):
       distance_matrix[i][0] = i
    for j in range(second_length):
       distance_matrix[0][j]=j
    for i in xrange(1, first_length):
        for j in range(1, second_length):
            deletion = distance_matrix[i-1][j] + 1
            insertion = distance_matrix[i][j-1] + 1
            substitution = distance_matrix[i-1][j-1]
            if first[i-1] != second[j-1]:
                substitution += 1
            distance_matrix[i][j] = min(insertion, deletion, substitution)
    return distance_matrix[first_length-1][second_length-1]

>>> minEditDistR(ref1, ref2)
5
>>> 
book = xlwt.Workbook(encoding="utf-8")
>>> sheet1 = book.add_sheet("Sheet 1")
>>> def get_tokens():
	with open("s1.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()

>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> tern=[]
>>> term=[]
>>> term
[]
>>> count = Counter(filtered)
>>> count
Counter({'function': 1, 'use': 1, 'corresponding': 1, 'features': 1, 'parameters': 1, 'positive': 1, 'image': 1, 'update': 1, 'gaussian': 1, 'penalty': 1, 'negative': 1, 'example': 1, 'examples': 1, 'apply': 1, 'semantic': 1, 'similar': 1, 'class': 1})
>>> def get_tokens():
	with open("jand1.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> 
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> term=[]
>>> term
[]
>>> 
>>> count = Counter(filtered)
>>> count
Counter({'new': 1, 'york': 1, 'times': 1})
>>> term.extend(count)
>>> term
['new', 'york', 'times']
>>> def get_tokens():
	with open("jand2.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> count
Counter({'new': 1, 'post': 1, 'york': 1})
>>> term.extend(count)
>>> term
['new', 'york', 'times', 'new', 'post', 'york']
>>> def get_tokens():
	with open("jand3.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> count
Counter({'angeles': 1, 'los': 1, 'times': 1})
>>> term.extend(count)
>>> term
['new', 'york', 'times', 'new', 'post', 'york', 'angeles', 'los', 'times']
>>> def get_tokens():
	with open("qlab.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> count
Counter({'new': 2, 'times': 1})
>>> term.extend(count)
>>> term
['new', 'york', 'times', 'new', 'post', 'york', 'angeles', 'los', 'times', 'new', 'times']
>>> i=1
>>> for t in term:
	sheet1.write(0,i,t)
	i=i+1

	
>>> book.save("lab2.xls")
>>> 
>>> def get_tokens():
	with open("jand1.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> count
Counter({'new': 1, 'york': 1, 'times': 1})
>>> i=1
>>> term
['new', 'york', 'times', 'new', 'post', 'york', 'angeles', 'los', 'times', 'new', 'times']
>>> i
1
>>> for t in term:
	sheet1.write(1,i,count[t])
	i=i+1

	
>>> def get_tokens():
	with open("jand2.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> count
Counter({'new': 1, 'post': 1, 'york': 1})
>>> i=1
>>> i
1
>>> for t in term:
	sheet1.write(2,i,count[t])
	i=i+1

	
>>> def get_tokens():
	with open("jand3.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> count
Counter({'angeles': 1, 'los': 1, 'times': 1})
>>> i=1
>>> i
1
>>> for t in term:
	sheet1.write(3,i,count[t])
	i=i+1

	
>>> def get_tokens():
	with open("qlab.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> count
Counter({'new': 2, 'times': 1})
>>> i=1
>>> for t in term:
	sheet1.write(4,i,count[t])
	i=i+1

	
>>> book.save("lab2.xls")
>>> def get_tokens():
	with open("jand1.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> count
Counter({'new': 1, 'york': 1, 'times': 1})
>>> max(count.values())
1
>>> bookrd = xlrd.open_workbook("lab2.xls")
>>> sheetrd=bookrd.sheet_by_index(0)
>>> sheetrd.cell(4,1).value
2.0
>>> bookwt = xlwt.Workbook(encoding="utf-8")
>>> sheetwt = book.add_sheet("Sheet wt")
>>> term
['new', 'york', 'times', 'new', 'post', 'york', 'angeles', 'los', 'times', 'new', 'times']
>>> max(count.values())
1
>>> for i in range(1,7)
SyntaxError: invalid syntax
>>> for i in range(1,7):
	sheetwt.write(0,i,count[t]/1)

	
>>> bookwt.save("feb20")

Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    bookwt.save("feb20")
  File "C:\Python27\lib\site-packages\xlwt\Workbook.py", line 710, in save
    doc.save(filename_or_stream, self.get_biff_data())
  File "C:\Python27\lib\site-packages\xlwt\Workbook.py", line 680, in get_biff_data
    self.__worksheets[self.__active_sheet].selected = True
IndexError: list index out of range
>>> for t in range(1,7):
	sheetwt.write(0,i,count[t]/1)

	

Traceback (most recent call last):
  File "<pyshell#145>", line 2, in <module>
    sheetwt.write(0,i,count[t]/1)
  File "C:\Python27\lib\site-packages\xlwt\Worksheet.py", line 1088, in write
    self.row(r).write(c, label, style)
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 248, in write
    self.insert_cell(col, NumberCell(self.__idx, col, style_index, label))
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 160, in insert_cell
    raise Exception(msg)
Exception: Attempt to overwrite cell: sheetname=u'Sheet wt' rowx=0 colx=6
>>> for t in range(1,7):
	sheetwt.write(2,i,count[t]/1)

	

Traceback (most recent call last):
  File "<pyshell#147>", line 2, in <module>
    sheetwt.write(2,i,count[t]/1)
  File "C:\Python27\lib\site-packages\xlwt\Worksheet.py", line 1088, in write
    self.row(r).write(c, label, style)
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 248, in write
    self.insert_cell(col, NumberCell(self.__idx, col, style_index, label))
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 160, in insert_cell
    raise Exception(msg)
Exception: Attempt to overwrite cell: sheetname=u'Sheet wt' rowx=2 colx=6
>>> for t in range(1,7):
	sheetwt.write(11,i,count[t]/1)

	

Traceback (most recent call last):
  File "<pyshell#149>", line 2, in <module>
    sheetwt.write(11,i,count[t]/1)
  File "C:\Python27\lib\site-packages\xlwt\Worksheet.py", line 1088, in write
    self.row(r).write(c, label, style)
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 248, in write
    self.insert_cell(col, NumberCell(self.__idx, col, style_index, label))
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 160, in insert_cell
    raise Exception(msg)
Exception: Attempt to overwrite cell: sheetname=u'Sheet wt' rowx=11 colx=6
>>> 
