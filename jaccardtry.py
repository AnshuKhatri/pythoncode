Python 2.7.9 (default, Dec 10 2014, 12:28:03) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import xlwt
>>> import xlrd
>>> import nltk
>>> import string
>>> from collections import Counter
>>> from nltk.corpus import stopwords
>>> book = xlwt.Workbook(encoding="utf-8")
>>> sheet1 = book.add_sheet("Sheet 1")
>>> bookrd = xlrd.open_workbook("dictionary.xls")
>>> print(bookrd.nsheets)
1
>>> sheetrd=bookrd.sheet_by_index(0)
>>> sheetrd.cell(1,1)
number:1.0
>>> for i in range(1,39):
	num=0
	for j in range(10,14):
		if(sheetrd.cell(j,i).value==0.0):
			num=num+1
	sheetd.write(2,i,3-num)

	

Traceback (most recent call last):
  File "<pyshell#13>", line 4, in <module>
    if(sheetrd.cell(j,i).value==0.0):
  File "C:\Python27\lib\site-packages\xlrd\sheet.py", line 401, in cell
    self._cell_types[rowx][colx],
IndexError: list index out of range
>>> for i in range(1,40):
	num=0
	for j in range(10,14):
		if(sheetrd.cell(j,i).value==0.0):
			num=num+1
	sheetd.write(3,i,3-num)

	

Traceback (most recent call last):
  File "<pyshell#15>", line 4, in <module>
    if(sheetrd.cell(j,i).value==0.0):
  File "C:\Python27\lib\site-packages\xlrd\sheet.py", line 401, in cell
    self._cell_types[rowx][colx],
IndexError: list index out of range
>>> for i in range(1,39):
	num=0
	for j in range(10,13):
		if(sheetrd.cell(j,i).value==0.0):
			num=num+1
	sheetd.write(3,i,3-num)

	

Traceback (most recent call last):
  File "<pyshell#17>", line 6, in <module>
    sheetd.write(3,i,3-num)
NameError: name 'sheetd' is not defined
>>> for i in range(1,39):
	num=0
	for j in range(10,14):
		if(sheetrd.cell(j,i).value==0.0):
			num=num+1
	sheet1.write(2,i,3-num)

	

Traceback (most recent call last):
  File "<pyshell#19>", line 4, in <module>
    if(sheetrd.cell(j,i).value==0.0):
  File "C:\Python27\lib\site-packages\xlrd\sheet.py", line 401, in cell
    self._cell_types[rowx][colx],
IndexError: list index out of range
>>> for i in range(1,39):
	num=0
	for j in range(10,13):
		if(sheetrd.cell(j,i).value==0.0):
			num=num+1
	sheet1.write(2,i,3-num)

	
>>> book.save("dct.xls")
>>> for i in range(1,40):
	num=0
	for j in range(10,13):
		if(sheetrd.cell(j,i).value==0.0):
			num=num+1
	sheet1.write(3,i,3-num)

	

Traceback (most recent call last):
  File "<pyshell#24>", line 4, in <module>
    if(sheetrd.cell(j,i).value==0.0):
  File "C:\Python27\lib\site-packages\xlrd\sheet.py", line 401, in cell
    self._cell_types[rowx][colx],
IndexError: array index out of range
>>> for i in range(1,39):
	num=0
	for j in range(10,13):
		num=num + sheetrd.cell(j,i).value
	sheet1.write(4,i,num)

	
>>> book.save("dct.xls")
>>> book = xlwt.Workbook(encoding="utf-8")
>>> sheet1 = book.add_sheet("Sheet 1")
>>> def get_tokens():
	with open("d1.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> count
Counter({'school': 1, 'hard': 1, 'walking': 1, 'rain': 1, 'long': 1, 'way': 1})
>>> i=1
>>> for t in count:
	sheet1.write(0,i,t)
	i=i+1

	
>>> count.values()
[1, 1, 1, 1, 1, 1]
>>> i=1
>>> for t in count:
	print(count.values)
	i=i+1

	
<built-in method values of Counter object at 0x0000000005549A68>
<built-in method values of Counter object at 0x0000000005549A68>
<built-in method values of Counter object at 0x0000000005549A68>
<built-in method values of Counter object at 0x0000000005549A68>
<built-in method values of Counter object at 0x0000000005549A68>
<built-in method values of Counter object at 0x0000000005549A68>
>>> i=1
>>> for t in count:
	print(count.values())
	i=i+1

	
[1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1]
>>> i=1
>>>  for t in count:
	print(count[t].values())
	i=i+1
	
  File "<pyshell#47>", line 1
    for t in count:
    ^
IndentationError: unexpected indent
>>> for t in count:
	print(count[t].values())
	i=i+1

	

Traceback (most recent call last):
  File "<pyshell#49>", line 2, in <module>
    print(count[t].values())
AttributeError: 'int' object has no attribute 'values'
>>> for t in count:
	print(t.values())
	i=i+1

	

Traceback (most recent call last):
  File "<pyshell#51>", line 2, in <module>
    print(t.values())
AttributeError: 'str' object has no attribute 'values'
>>> i=1
>>>  for t in count:
	print(count[t])
	i=i+1
	
  File "<pyshell#53>", line 1
    for t in count:
    ^
IndentationError: unexpected indent
>>> for t in count:
	print(count[t])
	i=i+1

	
1
1
1
1
1
1
>>> i=1
>>> for t in count:
	sheet1.write(1,i(count[t]))
	i=i+1

	

Traceback (most recent call last):
  File "<pyshell#58>", line 2, in <module>
    sheet1.write(1,i(count[t]))
TypeError: 'int' object is not callable
>>> for t in count:
	sheet1.write(1,i,(count[t]))
	i=i+1

	
>>> book.save("jaccard.xls")
>>> def get_tokens():
	with open("d2.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> count
Counter({'school': 1, 'stopped': 1, 'days': 1, 'rain': 1, 'closed': 1})
>>> i=1
>>> for t in count:
	sheet1.write(3,i,t)
	i=i+1

	
>>> i=1
>>> for t in count:
	sheet1.write(4,i,(count[t]))
	i=i+1

	
>>> book.save("jaccard.xls")
>>> def get_tokens():
	with open("q.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> count
Counter({'school': 1, 'rain': 1, 'closed': 1})
>>> i=1
>>> for t in count:
	sheet1.write(5,i,t)
	i=i+1

	
>>> i=1
>>> for t in count:
	sheet1.write(6,i,(count[t]))
	i=i+1

	
>>> book.save("jaccard.xls")
>>> sheet1.write(0,0,"document1")
>>> sheet1.write(3,0,"document2")
>>> sheet1.write(5,0,"query")
>>> book.save("jaccard.xls")

Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    book.save("jaccard.xls")
  File "C:\Python27\lib\site-packages\xlwt\Workbook.py", line 710, in save
    doc.save(filename_or_stream, self.get_biff_data())
  File "C:\Python27\lib\site-packages\xlwt\CompoundDoc.py", line 262, in save
    f = open(file_name_or_filelike_obj, 'w+b')
IOError: [Errno 13] Permission denied: 'jaccard.xls'
>>> book.save("jaccard.xls")
>>> sheet1.write(7,0,"d1Q")
>>> sheet1.write(9,0,"d2Q")
>>> book.save("jaccard.xls")
>>> for i in range(1,7)
SyntaxError: invalid syntax
>>> for i in range(1,7):



	sax

	

Traceback (most recent call last):
  File "<pyshell#103>", line 5, in <module>
    sax
NameError: name 'sax' is not defined
>>> count
Counter({'school': 1, 'rain': 1, 'closed': 1})
>>> term=[]
>>> term.extend(count)
>>> term
['school', 'rain', 'closed']
>>> def get_tokens():
	with open("d1.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> count
Counter({'school': 1, 'hard': 1, 'walking': 1, 'rain': 1, 'long': 1, 'way': 1})
>>> num=0
>>> for t in term:
	if(count[t]):
		num=num+1

		
>>> num
2
>>> val

Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    val
NameError: name 'val' is not defined
>>> val=0
>>> len(count)
6
>>> len(term)
3
>>> val=num/(len(count)+len(term)-num)
>>> val
0
>>> num
2
>>> 2/7
0
>>> float(2/7)
0.0
>>> float(2/7.0)
0.2857142857142857
>>> val=num/7.0
>>> val
0.2857142857142857
>>> sheet1.write(7,1,val)
>>> book.save("jaccard.xls")
>>> num=0
>>>  def get_tokens():
	with open("d2.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens
	
  File "<pyshell#135>", line 1
    def get_tokens():
    ^
IndentationError: unexpected indent
>>> def get_tokens():
	with open("d2.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> count
Counter({'school': 1, 'stopped': 1, 'days': 1, 'rain': 1, 'closed': 1})
>>> num=0
>>> for t in term:
	if(count[t]):
		num=num+1

		
>>> num
3
>>> term
['school', 'rain', 'closed']
>>> val=0
>>> deno=len(count)+len(term)-num
>>> deno
5
>>> val=3/5.0
>>> val
0.6
>>> sheet1.write(9,1,val)
>>> book.save("jaccard.xls")
>>> sheet2 = book.add_sheet("Sheet 2")
>>> book.save("jaccard.xls")
>>> def get_tokens():
	with open("d1.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> count = Counter(tokens)
>>> count
Counter({'the': 3, 'and': 1, 'school': 1, 'is': 1, 'hard': 1, 'when': 1, 'walking': 1, 'long': 1, 'to': 1, 'rain': 1, 'way': 1, 'in': 1})
>>> i=1
>>> for t in count:
	sheet2.write(0,i,t)
	i=i+1

	
>>> sheet2.write(0,0,"document1")
>>> book.save("jaccard.xls")

Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    book.save("jaccard.xls")
  File "C:\Python27\lib\site-packages\xlwt\Workbook.py", line 710, in save
    doc.save(filename_or_stream, self.get_biff_data())
  File "C:\Python27\lib\site-packages\xlwt\CompoundDoc.py", line 262, in save
    f = open(file_name_or_filelike_obj, 'w+b')
IOError: [Errno 13] Permission denied: 'jaccard.xls'
>>> book.save("jaccard.xls")
>>> i=1
>>> for t in count:
	sheet2.write(1,i,(count[t]))
	i=i+1

	
>>> sheet2.write(1,0,"d1Q")
>>> num=0
>>> val=0
>>> term
['school', 'rain', 'closed']
>>> for t in term:
	if(count[t]):
		num=num+1

		
>>> num
2
>>> val=len(count)+len(term)-num
>>> val
13
>>> deno=2/13.0
>>> sheet2.write(2,0,"d1Q")
>>> sheet2.write(2,1,"d1Q")
>>> sheet2.write(2,1,deno)

Traceback (most recent call last):
  File "<pyshell#182>", line 1, in <module>
    sheet2.write(2,1,deno)
  File "C:\Python27\lib\site-packages\xlwt\Worksheet.py", line 1088, in write
    self.row(r).write(c, label, style)
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 248, in write
    self.insert_cell(col, NumberCell(self.__idx, col, style_index, label))
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 160, in insert_cell
    raise Exception(msg)
Exception: Attempt to overwrite cell: sheetname=u'Sheet 2' rowx=2 colx=1
>>> sheet2.write(2,2,deno)
>>> book.save("jaccard.xls")
>>> term
['school', 'rain', 'closed']
>>> def get_tokens():
	with open("d2.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> count = Counter(tokens)
>>> count
Counter({'the': 2, 'has': 2, 'and': 1, 'school': 1, 'days': 1, 'rain': 1, 'stopped': 1, 'closed': 1, 'in': 1, 'not': 1})
>>> val=0
>>> deno=0
>>> num=0
>>> i=0
>>> for t in count:
	sheet2.write(5,i,t)
	i=i+1

	
>>> i=0
>>> for t in count:
	sheet2.write(6,i,(count[t]))
	i=i+1

	
>>> sheet2.write(5,0,"document2")

Traceback (most recent call last):
  File "<pyshell#200>", line 1, in <module>
    sheet2.write(5,0,"document2")
  File "C:\Python27\lib\site-packages\xlwt\Worksheet.py", line 1088, in write
    self.row(r).write(c, label, style)
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 241, in write
    StrCell(self.__idx, col, style_index, self.__parent_wb.add_str(label))
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 160, in insert_cell
    raise Exception(msg)
Exception: Attempt to overwrite cell: sheetname=u'Sheet 2' rowx=5 colx=0
>>> book.save("jaccard.xls")
>>> sheet2.write(7,0,"d2Q")
>>> num
0
>>> for t in term:
	if(count[t]):
		num=num+1

		
>>> num
3
>>> val=len(count)+len(term)-num
>>> val
10
>>> deno=3/10.0
>>> sheet2.write(7,2,deno)
>>> book.save("jaccard.xls")
>>> import stem

Traceback (most recent call last):
  File "<pyshell#212>", line 1, in <module>
    import stem
ImportError: No module named stem
>>> import stem
>>> from stemming.porter2 import stem

Traceback (most recent call last):
  File "<pyshell#214>", line 1, in <module>
    from stemming.porter2 import stem
ImportError: No module named stemming.porter2
>>> from nltk import PorterStemmer
>>> PorterStemmer().stem_word('complications')

Traceback (most recent call last):
  File "<pyshell#216>", line 1, in <module>
    PorterStemmer().stem_word('complications')
AttributeError: 'PorterStemmer' object has no attribute 'stem_word'
>>> porter = PorterStemmer()
>>> porter.stem('running')
u'run'
>>> for t in term:
	print(porter.stem(t))

	
school
rain
close
>>> book = xlwt.Workbook(encoding="utf-8")
>>> sheet1 = book.add_sheet("Sheet 1")
>>> sheet1.write(0,0,"document1")
>>> sheet1.write(1,0,"perform stemming")
>>> sheet1.write(4,0,"document2")
>>> sheet1.write(5,0,"perform stemming")
>>> book.save("stem.xls")
>>> def get_tokens():
	with open("d1.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> count = Counter(tokens)
>>> count
Counter({'the': 3, 'and': 1, 'school': 1, 'is': 1, 'hard': 1, 'when': 1, 'walking': 1, 'long': 1, 'to': 1, 'rain': 1, 'way': 1, 'in': 1})
>>> i=1
>>> for t in count:
	sheet1.write(0,i,t)
	i=i+!
	
SyntaxError: invalid syntax
>>> for t in count:
	sheet1.write(0,i,t)
	i=i+1

	
>>> for t in porter.stem(t))
SyntaxError: invalid syntax
>>> i=1
>>> for t in count:
	sheet1.write(1,i,count[t])
	i=i+1

	
>>> book.save("stem.xls")
>>> i=1
>>> for t in count:
	sheet1.write(10,i,porter.stem(t))
	i=i+1

	
>>> book.save("stem.xls")
>>> i=1
>>> for t in count:
	sheet1.write(2,i,porter.stem(t))
	i=i+1

	
>>> book.save("stem.xls")
>>> def get_tokens():
	with open("d2.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> count = Counter(tokens)
>>> count
Counter({'the': 2, 'has': 2, 'and': 1, 'school': 1, 'days': 1, 'rain': 1, 'stopped': 1, 'closed': 1, 'in': 1, 'not': 1})
>>> i=1
>>> for t in count:
	sheet1.write(4,i,t)
	i=i+1

	
>>> i=1
>>> for t in count:
	sheet1.write(6,i,porter.stem(t))
	i=i+1

	
>>> book.save("stem.xls")
>>> book = xlwt.Workbook(encoding="utf-8")
>>> sheet1 = book.add_sheet("Sheet 1")
>>> def get_tokens():
	with open("d1.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> count
Counter({'school': 1, 'hard': 1, 'walking': 1, 'rain': 1, 'long': 1, 'way': 1})
>>> term=[]
>>> term=count
>>> term
Counter({'school': 1, 'hard': 1, 'walking': 1, 'rain': 1, 'long': 1, 'way': 1})
>>> def get_tokens():
	with open("d2.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> count
Counter({'school': 1, 'stopped': 1, 'days': 1, 'rain': 1, 'closed': 1})
>>> term.extend(count)

Traceback (most recent call last):
  File "<pyshell#283>", line 1, in <module>
    term.extend(count)
AttributeError: 'Counter' object has no attribute 'extend'
>>> def get_tokens():
	with open("d1.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens
	tokens = get_tokens()
	filtered = [w for w in tokens if not w in stopwords.words('english')]
	count = Counter(filtered)
	count

	
>>> 
>>> count
Counter({'school': 1, 'stopped': 1, 'days': 1, 'rain': 1, 'closed': 1})
>>> def get_tokens():
	with open("d1.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> count
Counter({'school': 1, 'hard': 1, 'walking': 1, 'rain': 1, 'long': 1, 'way': 1})
>>> term=[]
>>> term
[]
>>> term.extend(count)
>>> term
['school', 'hard', 'walking', 'rain', 'long', 'way']
>>> def get_tokens():
	with open("d2.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> count
Counter({'school': 1, 'stopped': 1, 'days': 1, 'rain': 1, 'closed': 1})
>>> term.extend(count)
>>> term
['school', 'hard', 'walking', 'rain', 'long', 'way', 'school', 'stopped', 'days', 'rain', 'closed']
>>> def get_tokens():
	with open("d2.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> def get_tokens():
	with open("q.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> count
Counter({'school': 1, 'rain': 1, 'closed': 1})
>>> term.extend(count)
>>> term
['school', 'hard', 'walking', 'rain', 'long', 'way', 'school', 'stopped', 'days', 'rain', 'closed', 'school', 'rain', 'closed']
>>> i=1
>>> for t in term:
	sheet1.write(0,i,t)
	i=i+1

	
>>> book.save("cosine.txt")
>>> book.save("cosine.xls")
>>> def get_tokens():
	with open("d1.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> count
Counter({'school': 1, 'hard': 1, 'walking': 1, 'rain': 1, 'long': 1, 'way': 1})
>>> i=1
>>> for t in term:
	sheet1.write(1,i,count[t])
	i=i+1

	
>>> book.save("cosine.xls")
>>> def get_tokens():
	with open("d2.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> count
Counter({'school': 1, 'stopped': 1, 'days': 1, 'rain': 1, 'closed': 1})
>>> i=1
>>> for t in term:
	sheet1.write(2,i,count[t])
	i=i+1

	
>>> def get_tokens():
	with open("q.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> count
Counter({'school': 1, 'rain': 1, 'closed': 1})
>>> i=1
>>> for t in term:
	sheet1.write(3,i,count[t])
	i=i+1

	
>>> book.save("cosine.xls")
>>> def get_tokens():
	with open("d1.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> count
Counter({'school': 1, 'hard': 1, 'walking': 1, 'rain': 1, 'long': 1, 'way': 1})
>>> term
['school', 'hard', 'walking', 'rain', 'long', 'way', 'school', 'stopped', 'days', 'rain', 'closed', 'school', 'rain', 'closed']
>>> max(count.values())
1
>>> book = xlwt.Workbook(encoding="utf-8")
>>> sheet1 = book.add_sheet("Sheet 1")
>>> bookrd = xlrd.open_workbook("cosine.xls")
>>> sheetrd=bookrd.sheet_by_index(0)
>>> sheetrd.cell(0,1)
text:u'school'
>>> for i in range(1,15)
SyntaxError: invalid syntax
>>> for i in range(1,15):
	print sheetrd.cell(0,i).value

	
school
hard
walking
rain
long
way
school
stopped
days
rain
closed
school
rain
closed
>>> for i in range(1,15):
	num=0
	for j in range(1,4):
		if(sheetrd.cell(j,i).value==0.0):
			num=num+1
	sheet1.write(21,i,(3-num)/3.0)

	
>>> book.save("file1.xls")
>>> bookrd = xlrd.open_workbook("cosine.xls")
>>> sheetrd=bookrd.sheet_by_index(0)
>>> sheetrd.cell(5,2).value
0.3333333333333333
>>> for i in range(1,15):
	val=sheetrd.cell(1,i).value*sheetrd.cell(5,i).value
	sheet1.write(25,i,val)

	
>>> for i in range(1,15):
	val=sheetrd.cell(2,i).value*sheetrd.cell(5,i).value
	sheet1.write(26,i,val)

	
>>> for i in range(1,15):
	val=sheetrd.cell(3,i).value*sheetrd.cell(5,i).value
	sheet1.write(27,i,val)

	
>>> book.save("file1.xls")
>>> bookrd = xlrd.open_workbook("cosine.xls")
>>> sheetrd=bookrd.sheet_by_index(0)
>>> sheetrd.cell(8,2).value
0.0
>>> sum=0
>>> sum
0
>>> 
for i in range(1,15):
	sum=sum+(sheetrd.cell(8,i).value*sheetrd.cell(10,i).value)
	sheet1.write(30,i,val)

	

Traceback (most recent call last):
  File "<pyshell#392>", line 3, in <module>
    sum=sum+(sheetrd.cell(8,i).value*sheetrd.cell(10,i).value)
  File "C:\Python27\lib\site-packages\xlrd\sheet.py", line 401, in cell
    self._cell_types[rowx][colx],
IndexError: list index out of range
>>> for i in range(1,15):
	sum=sum+(sheetrd.cell(8,i).value*sheetrd.cell(10,i).value)
	sheet1.write(30,i,val)

	

Traceback (most recent call last):
  File "<pyshell#394>", line 2, in <module>
    sum=sum+(sheetrd.cell(8,i).value*sheetrd.cell(10,i).value)
  File "C:\Python27\lib\site-packages\xlrd\sheet.py", line 401, in cell
    self._cell_types[rowx][colx],
IndexError: list index out of range
>>> sheetrd.cell(8,1).value*sheetrd.cell(10,1).value

Traceback (most recent call last):
  File "<pyshell#395>", line 1, in <module>
    sheetrd.cell(8,1).value*sheetrd.cell(10,1).value
  File "C:\Python27\lib\site-packages\xlrd\sheet.py", line 401, in cell
    self._cell_types[rowx][colx],
IndexError: list index out of range
>>> sheetrd.cell(7,1).value*sheetrd.cell(9,1).value
1.0
>>> for i in range(1,15):
	sum=sum+(sheetrd.cell(7,i).value*sheetrd.cell(9,i).value)
	sheet1.write(45,i,val)

	
>>> for i in range(1,15):
	sum=sum+(sheetrd.cell(8,i).value*sheetrd.cell(9,i).value)
	sheet1.write(46,i,val)

	
>>> book.save("file1.xls")
>>> sum=0
>>> for i in range(1,15):
	sum=sum+(sheetrd.cell(7,i).value*sheetrd.cell(9,i).value)
	sheet1.write(50,i,val)

	
>>> sum=0
>>> for i in range(1,15):
	sum=sum+(sheetrd.cell(8,i).value*sheetrd.cell(9,i).value)
	sheet1.write(51,i,val)

	
>>> book.save("file1.xls")
>>> sum=0
>>> or i in range(1,15):
	sum=sum+(sheetrd.cell(7,i).value*sheetrd.cell(9,i).value)
	
SyntaxError: invalid syntax
>>> for i in range(1,15):
	sum=sum+(sheetrd.cell(7,i).value*sheetrd.cell(9,i).value)

	
>>> sum
6.0
>>> sheet1.write(0,0,sum)
>>> for i in range(1,15):
	sum=sum+(sheetrd.cell(8,i).value*sheetrd.cell(9,i).value)

	
>>> sum
12.88888888888889
>>> sum=0
>>> for i in range(1,15):
	sum=sum+(sheetrd.cell(8,i).value*sheetrd.cell(9,i).value)

	
>>> sum
6.888888888888889
>>> sheet1.write(0,1,sum)
>>> 
>>> book.save("file1.xls")
>>> 
