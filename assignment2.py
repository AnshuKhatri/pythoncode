Python 2.7.9 (default, Dec 10 2014, 12:28:03) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import nltk
im
>>> port string
SyntaxError: invalid syntax
>>> import string
>>> def get_tokens():
	with open("ds1.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    filtered = [w for w in tokens if not w in stopwords.words('english')]
NameError: name 'stopwords' is not defined
>>> from nltk.corpus import stopwords
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    count = Counter(filtered)
NameError: name 'Counter' is not defined
>>> from collections import Counter

>>> count = Counter(filtered)
>>> print count.most_common()
[('mobile', 18), ('ip', 13), ('home', 7), ('address', 7), ('node', 7), ('internet', 6), ('host', 5), ('location', 4), ('rfc', 4), ('network', 4), ('systems', 4), ('agent', 4), ('mobility', 3), ('associated', 3), ('users', 3), ('protocol', 2), ('permanent', 2), ('cellular', 2), ('ietf', 2), ('often', 2), ('current', 2), ('roaming', 2), ('care', 2), ('allows', 2), ('changes', 2), ('described', 2), ('seamless', 2), ('wireless', 2), ('datagrams', 2), ('tunnel', 2), ('provide', 2), ('connectivity', 2), ('designed', 2), ('data', 2), ('allow', 2), ('serving', 1), ('move', 1), ('tcp', 1), ('registers', 1), ('implementation', 1), ('local', 1), ('around', 1), ('effects', 1), ('domains', 1), ('maintaining', 1), ('disregarding', 1), ('identified', 1), ('communications', 1), ('underlying', 1), ('found', 1), ('identifies', 1), ('two', 1), ('specifies', 1), ('force', 1), ('tcpipto', 1), ('subnets', 1), ('generation', 1), ('packet', 1), ('static', 1), ('examples', 1), ('visiting', 1), ('away', 1), ('since', 1), ('4721', 1), ('routing', 1), ('cause', 1), ('across', 1), ('mechanisms', 1), ('use', 1), ('standard', 1), ('proxy', 1), ('change', 1), ('6275', 1), ('applications', 1), ('many', 1), ('connection', 1), ('extensions', 1), ('act', 1), ('routes', 1), ('moving', 1), ('addresses', 1), ('within', 1), ('environments', 1), ('one', 1), ('another', 1), ('carry', 1), ('reducing', 1), ('5944', 1), ('support', 1), ('next', 1), ('migrate', 1), ('however', 1), ('towers', 1), ('continuous', 1), ('overlapping', 1), ('correspondent', 1), ('link', 1), ('kind', 1), ('endpoint', 1), ('devices', 1), ('transparency', 1), ('problem', 1), ('layer', 1), ('defined', 1), ('middle', 1), ('engineering', 1), ('sudden', 1), ('need', 1), ('different', 1), ('goal', 1), ('handover', 1), ('without', 1), ('independent', 1), ('lan', 1), ('used', 1), ('multiple', 1), ('problems', 1), ('wired', 1), ('device', 1), ('man', 1), ('task', 1), ('required', 1), ('maintain', 1), ('solve', 1)]
>>> term=[]
>>> term.extend(count)
>>> len(term)
124
>>> def get_tokens():
	with open("ds2.txt") as shakes:
		text = shakes.read()
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> print count.most_common()
[]
>>> count
Counter()
>>> count = Counter(tokens)
>>> count
Counter()
>>> print count.most_common()
[]
>>> tokens
[]
>>> def get_tokens():
	with open("ds3.txt") as shakes:
		stext = shakes.read()
		cz

		
>>> 
>>> def get_tokens():
	with open("ds2.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> print count.most_common()
[('internet', 7), ('6', 6), ('protocol', 5), ('version', 5), ('ip', 5), ('several', 4), ('generation', 3), ('network', 3), ('service', 3), ('addresses', 3), ('addressing', 3), ('next', 3), ('also', 3), ('traffic', 3), ('switched', 2), ('qos', 2), ('4', 2), ('128', 2), ('packet', 2), ('computer', 2), ('computers', 2), ('quality', 2), ('networking', 2), ('therefore', 2), ('scheme', 2), ('information', 2), ('end', 2), ('provide', 2), ('data', 2), ('help', 1), ('bandwidth', 1), ('transporting', 1), ('consists', 1), ('label', 1), ('networks', 1), ('causes', 1), ('increase', 1), ('20', 1), ('knowledge', 1), ('field', 1), ('main', 1), ('sent', 1), ('2460', 1), ('possible', 1), ('number', 1), ('warranted', 1), ('every', 1), ('specificallycontains', 1), ('documented', 1), ('unique', 1), ('loss', 1), ('rfcs', 1), ('large', 1), ('benefit', 1), ('everyone', 1), ('connect', 1), ('best', 1), ('rfc', 1), ('space', 1), ('videoaudio', 1), ('current', 1), ('eliminate', 1), ('provides', 1), ('new', 1), ('power', 1), ('nature', 1), ('deliver', 1), ('flow', 1), ('expansion', 1), ('host', 1), ('advantages', 1), ('address', 1), ('refers', 1), ('route', 1), ('games', 1), ('concering', 1), ('implement', 1), ('one', 1), ('header', 1), ('addressed', 1), ('set', 1), ('another', 1), ('upgrades', 1), ('ecommerce', 1), ('ensures', 1), ('would', 1), ('addition', 1), ('support', 1), ('2', 1), ('bits', 1), ('exhaustion', 1), ('define', 1), ('bit', 1), ('brings', 1), ('ipng', 1), ('believe', 1), ('effort', 1), ('internetwe', 1), ('hope', 1), ('problem', 1), ('called', 1), ('interactive', 1), ('control', 1), ('layer', 1), ('required', 1), ('telephony', 1), ('substantial', 1), ('need', 1), ('aspects', 1), ('technology', 1), ('gathering', 1), ('guarantee', 1), ('marking', 1), ('whereas', 1), ('nat', 1), ('performance', 1), ('latency', 1), ('problemsin', 1), ('applications', 1), ('important', 1), ('designed', 1), ('requirements', 1), ('class', 1), ('sometimes', 1), ('packets', 1), ('starting', 1), ('order', 1)]
>>> term.extend(count)
>>> len(term)
251
>>> def get_tokens():
	with open("ds3.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> print count.most_common()
[('mobile', 23), ('ip', 12), ('6', 11), ('address', 9), ('node', 9), ('link', 9), ('home', 8), ('nodes', 7), ('network', 5), ('location', 3), ('auto', 3), ('necessary', 3), ('always', 3), ('connected', 3), ('standard', 3), ('configuration', 3), ('foreign', 3), ('need', 3), ('changing', 3), ('maintain', 3), ('fixedip', 2), ('uses', 2), ('connections', 2), ('care', 2), ('previously', 2), ('devices', 2), ('cant', 2), ('reachable', 2), ('used', 2), ('move', 1), ('mainly', 1), ('equally', 1), ('existing', 1), ('assigned', 1), ('regardless', 1), ('still', 1), ('features', 1), ('mobility', 1), ('capabilities', 1), ('wimax', 1), ('association', 1), ('ietf', 1), ('communicates', 1), ('applicable', 1), ('registrations', 1), ('specific', 1), ('benefit', 1), ('3775', 1), ('added', 1), ('operation', 1), ('rfc', 1), ('accomplish', 1), ('away', 1), ('denotes', 1), ('current', 1), ('version', 1), ('internet', 1), ('discovery', 1), ('terms', 1), ('targeted', 1), ('maintains', 1), ('stateful', 1), ('bwa', 1), ('although', 1), ('roaming', 1), ('change', 1), ('extension', 1), ('allows', 1), ('neighbor', 1), ('router', 1), ('major', 1), ('wlan', 1), ('addresses', 1), ('point', 1), ('environments', 1), ('one', 1), ('header', 1), ('logically', 1), ('another', 1), ('described', 1), ('signifies', 1), ('ipv6', 1), ('expected', 1), ('understand', 1), ('known', 1), ('made', 1), ('attached', 1), ('binding', 1), ('agent', 1), ('moves', 1), ('defines', 1), ('information', 1), ('detail', 1), ('also', 1), ('without', 1), ('attachment', 1), ('several', 1), ('wired', 1), ('types', 1), ('stateless', 1), ('correspondent', 1), ('whenever', 1)]
>>> term.extend(count)
>>> len(term)
353
>>> import xlwt
>>> book = xlwt.Workbook(encoding="utf-8")
>>> sheet1 = book.add_sheet("Sheet 1")
>>> sheet1.write(0, 0, "Doc1")
>>> i=1
>>> for n in term
SyntaxError: invalid syntax
>>> for n in term:
	sheet1.write(0,i,n)
	i=i+1

	

Traceback (most recent call last):
  File "<pyshell#83>", line 2, in <module>
    sheet1.write(0,i,n)
  File "C:\Python27\lib\site-packages\xlwt\Worksheet.py", line 1088, in write
    self.row(r).write(c, label, style)
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 236, in write
    self.__adjust_bound_col_idx(col)
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 79, in __adjust_bound_col_idx
    raise ValueError("column index (%r) not an int in range(256)" % arg)
ValueError: column index (256) not an int in range(256)
>>> term[255]
'existing'
>>> term
['serving', 'protocol', 'move', 'tcp', 'registers', 'implementation', 'permanent', 'location', 'local', 'around', 'effects', 'cellular', 'domains', 'maintaining', 'ietf', 'disregarding', 'identified', 'rfc', 'communications', 'underlying', 'found', 'identifies', 'two', 'specifies', 'force', 'often', 'tcpipto', 'subnets', 'generation', 'packet', 'static', 'examples', 'home', 'network', 'visiting', 'away', 'since', '4721', 'current', 'routing', 'internet', 'cause', 'across', 'mechanisms', 'use', 'standard', 'host', 'proxy', 'address', 'roaming', 'change', 'care', '6275', 'applications', 'many', 'allows', 'connection', 'extensions', 'act', 'routes', 'moving', 'changes', 'addresses', 'mobility', 'within', 'environments', 'one', 'another', 'carry', 'reducing', '5944', 'described', 'support', 'seamless', 'next', 'migrate', 'however', 'systems', 'towers', 'continuous', 'overlapping', 'wireless', 'datagrams', 'correspondent', 'link', 'kind', 'endpoint', 'tunnel', 'devices', 'transparency', 'problem', 'layer', 'associated', 'defined', 'ip', 'agent', 'middle', 'engineering', 'sudden', 'need', 'different', 'goal', 'provide', 'handover', 'without', 'node', 'independent', 'lan', 'used', 'multiple', 'users', 'problems', 'connectivity', 'wired', 'designed', 'device', 'data', 'man', 'task', 'mobile', 'required', 'maintain', 'solve', 'allow', 'protocol', 'help', 'switched', 'bandwidth', 'transporting', 'consists', 'qos', 'label', 'networks', 'causes', 'increase', '20', 'knowledge', 'field', '4', 'main', 'sent', '2460', 'possible', 'number', 'warranted', 'every', 'specificallycontains', '128', 'documented', 'unique', 'loss', 'rfcs', 'large', 'benefit', 'everyone', 'generation', 'packet', 'computer', 'connect', 'best', 'rfc', 'network', 'space', 'videoaudio', 'current', 'version', 'eliminate', 'provides', 'internet', 'new', 'power', 'nature', 'deliver', 'flow', 'expansion', 'host', 'advantages', 'address', 'refers', 'service', 'route', 'computers', 'games', 'concering', 'implement', 'addresses', 'addressing', 'one', 'header', 'addressed', 'set', 'another', 'upgrades', 'quality', 'ecommerce', 'ensures', 'networking', 'would', 'addition', 'support', 'next', '2', 'therefore', '6', 'scheme', 'bits', 'exhaustion', 'define', 'bit', 'brings', 'ipng', 'believe', 'effort', 'internetwe', 'hope', 'problem', 'called', 'interactive', 'control', 'layer', 'required', 'ip', 'telephony', 'substantial', 'need', 'aspects', 'technology', 'gathering', 'guarantee', 'information', 'marking', 'end', 'provide', 'whereas', 'also', 'nat', 'performance', 'several', 'latency', 'problemsin', 'applications', 'important', 'designed', 'requirements', 'data', 'class', 'sometimes', 'packets', 'traffic', 'starting', 'order', 'move', 'mainly', 'equally', 'fixedip', 'existing', 'assigned', 'regardless', 'still', 'features', 'mobility', 'capabilities', 'location', 'nodes', 'auto', 'wimax', 'association', 'necessary', 'ietf', 'always', 'communicates', 'applicable', 'registrations', 'specific', 'benefit', '3775', 'uses', 'connections', 'added', 'home', 'operation', 'rfc', 'accomplish', 'network', 'away', 'denotes', 'current', 'version', 'internet', 'connected', 'discovery', 'terms', 'targeted', 'maintains', 'standard', 'stateful', 'bwa', 'although', 'address', 'roaming', 'configuration', 'change', 'care', 'extension', 'allows', 'foreign', 'neighbor', 'router', 'major', 'wlan', 'addresses', 'point', 'previously', 'environments', 'one', 'header', 'logically', 'another', 'described', 'signifies', 'ipv6', 'expected', '6', 'understand', 'known', 'made', 'attached', 'devices', 'mobile', 'ip', 'binding', 'agent', 'cant', 'need', 'moves', 'defines', 'information', 'detail', 'also', 'without', 'reachable', 'attachment', 'several', 'node', 'used', 'wired', 'changing', 'types', 'stateless', 'correspondent', 'whenever', 'maintain', 'link']
>>> book.save("tf.idf.xls")
>>> def get_tokens():
	with open("ds1.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> print count.most_common()
[('mobile', 18), ('ip', 13), ('home', 7), ('address', 7), ('node', 7), ('internet', 6), ('host', 5), ('location', 4), ('network', 4), ('systems', 4), ('agent', 4), ('mobility', 3), ('associated', 3), ('users', 3), ('protocol', 2), ('permanent', 2), ('cellular', 2), ('ietf', 2), ('often', 2), ('current', 2), ('roaming', 2), ('care', 2), ('allows', 2), ('changes', 2), ('described', 2), ('seamless', 2), ('wireless', 2), ('datagrams', 2), ('tunnel', 2), ('provide', 2), ('connectivity', 2), ('designed', 2), ('data', 2), ('allow', 2), ('serving', 1), ('move', 1), ('tcp', 1), ('registers', 1), ('implementation', 1), ('local', 1), ('around', 1), ('effects', 1), ('domains', 1), ('maintaining', 1), ('disregarding', 1), ('identified', 1), ('rfc', 1), ('communications', 1), ('underlying', 1), ('found', 1), ('identifies', 1), ('two', 1), ('specifies', 1), ('force', 1), ('tcpipto', 1), ('subnets', 1), ('generation', 1), ('packet', 1), ('static', 1), ('examples', 1), ('visiting', 1), ('away', 1), ('since', 1), ('routing', 1), ('cause', 1), ('across', 1), ('mechanisms', 1), ('however', 1), ('standard', 1), ('proxy', 1), ('change', 1), ('applications', 1), ('many', 1), ('connection', 1), ('extensions', 1), ('act', 1), ('routes', 1), ('moving', 1), ('addresses', 1), ('within', 1), ('environments', 1), ('one', 1), ('another', 1), ('carry', 1), ('reducing', 1), ('use', 1), ('support', 1), ('next', 1), ('migrate', 1), ('towers', 1), ('continuous', 1), ('overlapping', 1), ('correspondent', 1), ('link', 1), ('kind', 1), ('endpoint', 1), ('devices', 1), ('transparency', 1), ('problem', 1), ('layer', 1), ('defined', 1), ('middle', 1), ('engineering', 1), ('sudden', 1), ('need', 1), ('different', 1), ('goal', 1), ('handover', 1), ('without', 1), ('independent', 1), ('lan', 1), ('used', 1), ('multiple', 1), ('problems', 1), ('wired', 1), ('device', 1), ('man', 1), ('task', 1), ('required', 1), ('maintain', 1), ('solve', 1)]
>>> term=[]
>>> term=count
>>> i=1
>>> book = xlwt.Workbook(encoding="utf-8")
>>> sheet = book.add_sheet("Sheet ")
>>> i=1
>>> for n in term:
	sheet.write(0,i,n)
	i=i+1

	
>>> book.save("try.xls")
>>> def get_tokens():
	with open("ds1.txt") as shakes:
		
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> def get_tokens():
	with open("ds2.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> i=1
>>> count
Counter({'internet': 7, 'protocol': 5, 'generation': 3, 'addressing': 3, 'next': 3, 'version': 3, 'several': 3, 'addresses': 2, 'switched': 2, 'scheme': 2, 'packet': 2, 'computer': 2, 'information': 2, 'network': 2, 'computers': 2, 'provide': 2, 'six': 2, 'also': 2, 'therefore': 2, 'end': 2, 'control': 1, 'layer': 1, 'everyone': 1, 'causes': 1, 'one': 1, 'four': 1, 'addressed': 1, 'connect': 1, 'another': 1, 'upgrades': 1, 'need': 1, 'technology': 1, 'networks': 1, 'gathering': 1, 'help': 1, 'networking': 1, 'would': 1, 'support': 1, 'current': 1, 'nat': 1, 'exhaustion': 1, 'sent': 1, 'define': 1, 'problemsin': 1, 'aspects': 1, 'nature': 1, 'addition': 1, 'possible': 1, 'expansion': 1, 'number': 1, 'warranted': 1, 'host': 1, 'important': 1, 'advantages': 1, 'designed': 1, 'address': 1, 'documented': 1, 'believe': 1, 'data': 1, 'knowledge': 1, 'main': 1, 'route': 1, 'sometimes': 1, 'packets': 1, 'space': 1, 'rfcs': 1, 'large': 1, 'internetwe': 1, 'benefit': 1, 'substantial': 1, 'eliminate': 1, 'hope': 1, 'ipng': 1, 'concering': 1, 'every': 1, 'problem': 1, 'increase': 1, 'starting': 1, 'called': 1, 'specificallycontains': 1})
>>> for n in count:
	sheet.write(1,i,n)
	i=i+!
	
SyntaxError: invalid syntax
>>> for n in count:
	sheet.write(1,i,n)
	i=i+1

	
>>> def get_tokens():
	with open("ds3.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> i=1
>>> count
Counter({'mobile': 18, 'ip': 9, 'link': 8, 'nodes': 6, 'network': 5, 'six': 5, 'address': 5, 'node': 4, 'need': 3, 'home': 3, 'maintain': 3, 'location': 3, 'changing': 3, 'necessary': 3, 'always': 3, 'foreign': 3, 'previously': 2, 'connections': 2, 'cant': 2, 'used': 2, 'reachable': 2, 'standard': 2, 'fixedip': 2, 'devices': 2, 'connected': 2, 'understand': 1, 'major': 1, 'wlan': 1, 'whenever': 1, 'point': 1, 'move': 1, 'mainly': 1, 'equally': 1, 'environments': 1, 'one': 1, 'ipv': 1, 'another': 1, 'still': 1, 'denotes': 1, 'defines': 1, 'information': 1, 'accomplish': 1, 'moves': 1, 'capabilities': 1, 'tis': 1, 'version': 1, 'attachment': 1, 'internet': 1, 'expected': 1, 'several': 1, 'added': 1, 'terms': 1, 'regardless': 1, 'targeted': 1, 'bwa': 1, 'wimax': 1, 'wired': 1, 'although': 1, 'roaming': 1, 'existing': 1, 'change': 1, 'care': 1, 'mobility': 1, 'assigned': 1, 'made': 1, 'allows': 1, 'applicable': 1, 'specific': 1, 'ietf': 1, 'benefit': 1, 'without': 1, 'attached': 1})
>>> for n in count:
	sheet.write(2,i,n)
	i=i+1

	
>>> count
Counter({'mobile': 18, 'ip': 9, 'link': 8, 'nodes': 6, 'network': 5, 'six': 5, 'address': 5, 'node': 4, 'need': 3, 'home': 3, 'maintain': 3, 'location': 3, 'changing': 3, 'necessary': 3, 'always': 3, 'foreign': 3, 'previously': 2, 'connections': 2, 'cant': 2, 'used': 2, 'reachable': 2, 'standard': 2, 'fixedip': 2, 'devices': 2, 'connected': 2, 'understand': 1, 'major': 1, 'wlan': 1, 'whenever': 1, 'point': 1, 'move': 1, 'mainly': 1, 'equally': 1, 'environments': 1, 'one': 1, 'ipv': 1, 'another': 1, 'still': 1, 'denotes': 1, 'defines': 1, 'information': 1, 'accomplish': 1, 'moves': 1, 'capabilities': 1, 'tis': 1, 'version': 1, 'attachment': 1, 'internet': 1, 'expected': 1, 'several': 1, 'added': 1, 'terms': 1, 'regardless': 1, 'targeted': 1, 'bwa': 1, 'wimax': 1, 'wired': 1, 'although': 1, 'roaming': 1, 'existing': 1, 'change': 1, 'care': 1, 'mobility': 1, 'assigned': 1, 'made': 1, 'allows': 1, 'applicable': 1, 'specific': 1, 'ietf': 1, 'benefit': 1, 'without': 1, 'attached': 1})
>>> term=[]
>>> term.extenc(count)

Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    term.extenc(count)
AttributeError: 'list' object has no attribute 'extenc'
>>> def get_tokens():
	with open("ds1.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> count
Counter({'mobile': 18, 'ip': 13, 'home': 7, 'address': 7, 'node': 7, 'internet': 6, 'host': 5, 'location': 4, 'network': 4, 'systems': 4, 'agent': 4, 'mobility': 3, 'associated': 3, 'users': 3, 'protocol': 2, 'permanent': 2, 'cellular': 2, 'ietf': 2, 'often': 2, 'current': 2, 'roaming': 2, 'care': 2, 'allows': 2, 'changes': 2, 'described': 2, 'seamless': 2, 'wireless': 2, 'datagrams': 2, 'tunnel': 2, 'provide': 2, 'connectivity': 2, 'designed': 2, 'data': 2, 'allow': 2, 'serving': 1, 'move': 1, 'tcp': 1, 'registers': 1, 'implementation': 1, 'local': 1, 'around': 1, 'effects': 1, 'domains': 1, 'maintaining': 1, 'disregarding': 1, 'identified': 1, 'rfc': 1, 'communications': 1, 'underlying': 1, 'found': 1, 'identifies': 1, 'two': 1, 'specifies': 1, 'force': 1, 'tcpipto': 1, 'subnets': 1, 'generation': 1, 'packet': 1, 'static': 1, 'examples': 1, 'visiting': 1, 'away': 1, 'since': 1, 'routing': 1, 'cause': 1, 'across': 1, 'mechanisms': 1, 'however': 1, 'standard': 1, 'proxy': 1, 'change': 1, 'applications': 1, 'many': 1, 'connection': 1, 'extensions': 1, 'act': 1, 'routes': 1, 'moving': 1, 'addresses': 1, 'within': 1, 'environments': 1, 'one': 1, 'another': 1, 'carry': 1, 'reducing': 1, 'use': 1, 'support': 1, 'next': 1, 'migrate': 1, 'towers': 1, 'continuous': 1, 'overlapping': 1, 'correspondent': 1, 'link': 1, 'kind': 1, 'endpoint': 1, 'devices': 1, 'transparency': 1, 'problem': 1, 'layer': 1, 'defined': 1, 'middle': 1, 'engineering': 1, 'sudden': 1, 'need': 1, 'different': 1, 'goal': 1, 'handover': 1, 'without': 1, 'independent': 1, 'lan': 1, 'used': 1, 'multiple': 1, 'problems': 1, 'wired': 1, 'device': 1, 'man': 1, 'task': 1, 'required': 1, 'maintain': 1, 'solve': 1})
>>> term=[]
>>> term.extend(count)
>>> len(term)
121
>>> def get_tokens():
	with open("ds2.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> count
Counter({'internet': 7, 'protocol': 5, 'generation': 3, 'addressing': 3, 'next': 3, 'version': 3, 'several': 3, 'addresses': 2, 'switched': 2, 'scheme': 2, 'packet': 2, 'computer': 2, 'information': 2, 'network': 2, 'computers': 2, 'provide': 2, 'six': 2, 'also': 2, 'therefore': 2, 'end': 2, 'control': 1, 'layer': 1, 'everyone': 1, 'causes': 1, 'one': 1, 'four': 1, 'addressed': 1, 'connect': 1, 'another': 1, 'upgrades': 1, 'need': 1, 'technology': 1, 'networks': 1, 'gathering': 1, 'help': 1, 'networking': 1, 'would': 1, 'support': 1, 'current': 1, 'nat': 1, 'exhaustion': 1, 'sent': 1, 'define': 1, 'problemsin': 1, 'aspects': 1, 'nature': 1, 'addition': 1, 'possible': 1, 'expansion': 1, 'number': 1, 'warranted': 1, 'host': 1, 'important': 1, 'advantages': 1, 'designed': 1, 'address': 1, 'documented': 1, 'believe': 1, 'data': 1, 'knowledge': 1, 'main': 1, 'route': 1, 'sometimes': 1, 'packets': 1, 'space': 1, 'rfcs': 1, 'large': 1, 'internetwe': 1, 'benefit': 1, 'substantial': 1, 'eliminate': 1, 'hope': 1, 'ipng': 1, 'concering': 1, 'every': 1, 'problem': 1, 'increase': 1, 'starting': 1, 'called': 1, 'specificallycontains': 1})
>>> term.extend(count)
>>> len9term)
SyntaxError: invalid syntax
>>> len(term)
201
>>> def get_tokens():
	with open("ds3.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> count
Counter({'mobile': 18, 'ip': 9, 'link': 8, 'nodes': 6, 'network': 5, 'six': 5, 'address': 5, 'node': 4, 'need': 3, 'home': 3, 'maintain': 3, 'location': 3, 'changing': 3, 'necessary': 3, 'always': 3, 'foreign': 3, 'previously': 2, 'connections': 2, 'cant': 2, 'used': 2, 'reachable': 2, 'standard': 2, 'fixedip': 2, 'devices': 2, 'connected': 2, 'understand': 1, 'major': 1, 'wlan': 1, 'whenever': 1, 'point': 1, 'move': 1, 'mainly': 1, 'equally': 1, 'environments': 1, 'one': 1, 'ipv': 1, 'another': 1, 'still': 1, 'denotes': 1, 'defines': 1, 'information': 1, 'accomplish': 1, 'moves': 1, 'capabilities': 1, 'tis': 1, 'version': 1, 'attachment': 1, 'internet': 1, 'expected': 1, 'several': 1, 'added': 1, 'terms': 1, 'regardless': 1, 'targeted': 1, 'bwa': 1, 'wimax': 1, 'wired': 1, 'although': 1, 'roaming': 1, 'existing': 1, 'change': 1, 'care': 1, 'mobility': 1, 'assigned': 1, 'made': 1, 'allows': 1, 'applicable': 1, 'specific': 1, 'ietf': 1, 'benefit': 1, 'without': 1, 'attached': 1})
>>> term.extend(count)
>>> term
['serving', 'protocol', 'move', 'tcp', 'registers', 'implementation', 'permanent', 'location', 'local', 'around', 'effects', 'cellular', 'domains', 'maintaining', 'ietf', 'disregarding', 'identified', 'rfc', 'communications', 'underlying', 'found', 'identifies', 'two', 'specifies', 'force', 'often', 'tcpipto', 'subnets', 'generation', 'packet', 'static', 'examples', 'home', 'network', 'visiting', 'away', 'since', 'current', 'routing', 'internet', 'cause', 'across', 'mechanisms', 'however', 'standard', 'host', 'proxy', 'address', 'roaming', 'change', 'care', 'applications', 'many', 'allows', 'connection', 'extensions', 'act', 'routes', 'moving', 'changes', 'addresses', 'mobility', 'within', 'environments', 'one', 'another', 'carry', 'reducing', 'use', 'described', 'support', 'seamless', 'next', 'migrate', 'systems', 'towers', 'continuous', 'overlapping', 'wireless', 'datagrams', 'correspondent', 'link', 'kind', 'endpoint', 'tunnel', 'devices', 'transparency', 'problem', 'layer', 'associated', 'defined', 'ip', 'agent', 'middle', 'engineering', 'sudden', 'need', 'different', 'goal', 'provide', 'handover', 'without', 'node', 'independent', 'lan', 'used', 'multiple', 'users', 'problems', 'connectivity', 'wired', 'designed', 'device', 'data', 'man', 'task', 'mobile', 'required', 'maintain', 'solve', 'allow', 'control', 'layer', 'everyone', 'protocol', 'addresses', 'switched', 'generation', 'scheme', 'causes', 'addressing', 'packet', 'one', 'four', 'addressed', 'computer', 'connect', 'another', 'upgrades', 'need', 'technology', 'networks', 'gathering', 'help', 'information', 'networking', 'network', 'would', 'computers', 'provide', 'support', 'six', 'next', 'current', 'also', 'version', 'therefore', 'nat', 'internet', 'exhaustion', 'several', 'sent', 'define', 'problemsin', 'aspects', 'nature', 'addition', 'possible', 'expansion', 'number', 'warranted', 'host', 'important', 'advantages', 'designed', 'address', 'end', 'documented', 'believe', 'data', 'knowledge', 'main', 'route', 'sometimes', 'packets', 'space', 'rfcs', 'large', 'internetwe', 'benefit', 'substantial', 'eliminate', 'hope', 'ipng', 'concering', 'every', 'problem', 'increase', 'starting', 'called', 'specificallycontains', 'understand', 'major', 'wlan', 'whenever', 'point', 'previously', 'ip', 'move', 'mainly', 'equally', 'environments', 'one', 'connections', 'cant', 'used', 'ipv', 'another', 'need', 'home', 'still', 'denotes', 'link', 'defines', 'information', 'accomplish', 'network', 'six', 'moves', 'capabilities', 'tis', 'version', 'reachable', 'attachment', 'internet', 'expected', 'nodes', 'several', 'maintain', 'location', 'node', 'added', 'terms', 'regardless', 'targeted', 'standard', 'bwa', 'wimax', 'wired', 'fixedip', 'although', 'address', 'changing', 'roaming', 'existing', 'change', 'care', 'mobility', 'assigned', 'made', 'necessary', 'mobile', 'always', 'allows', 'applicable', 'devices', 'foreign', 'specific', 'ietf', 'benefit', 'without', 'connected', 'attached']
>>> len(term)
273
>>> book = xlwt.Workbook(encoding="utf-8")
>>> sheet1 = book.add_sheet("Sheet 1")
>>> i=1
>>> for n in term:
	sheet1.write(0,i,n)
	i=i+1

	

Traceback (most recent call last):
  File "<pyshell#206>", line 2, in <module>
    sheet1.write(0,i,n)
  File "C:\Python27\lib\site-packages\xlwt\Worksheet.py", line 1088, in write
    self.row(r).write(c, label, style)
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 236, in write
    self.__adjust_bound_col_idx(col)
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 79, in __adjust_bound_col_idx
    raise ValueError("column index (%r) not an int in range(256)" % arg)
ValueError: column index (256) not an int in range(256)
>>> book.save("tfidf.xls")
>>> def get_tokens():
	with open("ds1.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> count = Counter(tokens)
>>> i=1
>>> for t in term:
	sheet1.write(1,i,count[t])
	i=i+1

	

Traceback (most recent call last):
  File "<pyshell#222>", line 2, in <module>
    sheet1.write(1,i,count[t])
  File "C:\Python27\lib\site-packages\xlwt\Worksheet.py", line 1088, in write
    self.row(r).write(c, label, style)
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 236, in write
    self.__adjust_bound_col_idx(col)
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 79, in __adjust_bound_col_idx
    raise ValueError("column index (%r) not an int in range(256)" % arg)
ValueError: column index (256) not an int in range(256)
>>> book.save("tfidf.xls")
>>> def get_tokens():
	with open("ds1.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> count = Counter(tokens)
>>> i=1
>>> for t in term:
	sheet1.write(2,i,count[t])
	i=i+1

	

Traceback (most recent call last):
  File "<pyshell#239>", line 2, in <module>
    sheet1.write(2,i,count[t])
  File "C:\Python27\lib\site-packages\xlwt\Worksheet.py", line 1088, in write
    self.row(r).write(c, label, style)
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 236, in write
    self.__adjust_bound_col_idx(col)
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 79, in __adjust_bound_col_idx
    raise ValueError("column index (%r) not an int in range(256)" % arg)
ValueError: column index (256) not an int in range(256)
>>> book.save("tfidf.xls")

Traceback (most recent call last):
  File "<pyshell#240>", line 1, in <module>
    book.save("tfidf.xls")
  File "C:\Python27\lib\site-packages\xlwt\Workbook.py", line 710, in save
    doc.save(filename_or_stream, self.get_biff_data())
  File "C:\Python27\lib\site-packages\xlwt\CompoundDoc.py", line 262, in save
    f = open(file_name_or_filelike_obj, 'w+b')
IOError: [Errno 13] Permission denied: 'tfidf.xls'
>>> book.save("tfidf.xls")
>>> def get_tokens():
	with open("ds1.txt") as shakes:
		text = shakes.read()
		dfc

		
>>> 
>>> def get_tokens():
	with open("ds2.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> i=1
>>> for t in term:
	sheet1.write(2,i,count[t])
	i=i+1

	

Traceback (most recent call last):
  File "<pyshell#262>", line 2, in <module>
    sheet1.write(2,i,count[t])
  File "C:\Python27\lib\site-packages\xlwt\Worksheet.py", line 1088, in write
    self.row(r).write(c, label, style)
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 248, in write
    self.insert_cell(col, NumberCell(self.__idx, col, style_index, label))
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 160, in insert_cell
    raise Exception(msg)
Exception: Attempt to overwrite cell: sheetname=u'Sheet 1' rowx=2 colx=1
>>> book.save("tfidf.xls")
>>> count
Counter({'internet': 7, 'protocol': 5, 'generation': 3, 'addressing': 3, 'next': 3, 'version': 3, 'several': 3, 'addresses': 2, 'switched': 2, 'scheme': 2, 'packet': 2, 'computer': 2, 'information': 2, 'network': 2, 'computers': 2, 'provide': 2, 'six': 2, 'also': 2, 'therefore': 2, 'end': 2, 'control': 1, 'layer': 1, 'everyone': 1, 'causes': 1, 'one': 1, 'four': 1, 'addressed': 1, 'connect': 1, 'another': 1, 'upgrades': 1, 'need': 1, 'technology': 1, 'networks': 1, 'gathering': 1, 'help': 1, 'networking': 1, 'would': 1, 'support': 1, 'current': 1, 'nat': 1, 'exhaustion': 1, 'sent': 1, 'define': 1, 'problemsin': 1, 'aspects': 1, 'nature': 1, 'addition': 1, 'possible': 1, 'expansion': 1, 'number': 1, 'warranted': 1, 'host': 1, 'important': 1, 'advantages': 1, 'designed': 1, 'address': 1, 'documented': 1, 'believe': 1, 'data': 1, 'knowledge': 1, 'main': 1, 'route': 1, 'sometimes': 1, 'packets': 1, 'space': 1, 'rfcs': 1, 'large': 1, 'internetwe': 1, 'benefit': 1, 'substantial': 1, 'eliminate': 1, 'hope': 1, 'ipng': 1, 'concering': 1, 'every': 1, 'problem': 1, 'increase': 1, 'starting': 1, 'called': 1, 'specificallycontains': 1})
>>> book = xlwt.Workbook(encoding="utf-8")
>>> sheet2 = book.add_sheet("Sheet 2")
>>> i=1
>>> for n in term:
	sheet2.write(0,i,n)
	i=i+1

	

Traceback (most recent call last):
  File "<pyshell#271>", line 2, in <module>
    sheet2.write(0,i,n)
  File "C:\Python27\lib\site-packages\xlwt\Worksheet.py", line 1088, in write
    self.row(r).write(c, label, style)
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 236, in write
    self.__adjust_bound_col_idx(col)
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 79, in __adjust_bound_col_idx
    raise ValueError("column index (%r) not an int in range(256)" % arg)
ValueError: column index (256) not an int in range(256)
>>> book.save("tfidf.xls")
>>> def get_tokens():
	ith open("ds1.txt") as shakes:
		
SyntaxError: invalid syntax
>>> def get_tokens():
	with open("ds1.txt") as shakes:
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
Counter({'mobile': 18, 'ip': 13, 'home': 7, 'address': 7, 'node': 7, 'internet': 6, 'host': 5, 'location': 4, 'network': 4, 'systems': 4, 'agent': 4, 'mobility': 3, 'associated': 3, 'users': 3, 'protocol': 2, 'permanent': 2, 'cellular': 2, 'ietf': 2, 'often': 2, 'current': 2, 'roaming': 2, 'care': 2, 'allows': 2, 'changes': 2, 'described': 2, 'seamless': 2, 'wireless': 2, 'datagrams': 2, 'tunnel': 2, 'provide': 2, 'connectivity': 2, 'designed': 2, 'data': 2, 'allow': 2, 'serving': 1, 'move': 1, 'tcp': 1, 'registers': 1, 'implementation': 1, 'local': 1, 'around': 1, 'effects': 1, 'domains': 1, 'maintaining': 1, 'disregarding': 1, 'identified': 1, 'rfc': 1, 'communications': 1, 'underlying': 1, 'found': 1, 'identifies': 1, 'two': 1, 'specifies': 1, 'force': 1, 'tcpipto': 1, 'subnets': 1, 'generation': 1, 'packet': 1, 'static': 1, 'examples': 1, 'visiting': 1, 'away': 1, 'since': 1, 'routing': 1, 'cause': 1, 'across': 1, 'mechanisms': 1, 'however': 1, 'standard': 1, 'proxy': 1, 'change': 1, 'applications': 1, 'many': 1, 'connection': 1, 'extensions': 1, 'act': 1, 'routes': 1, 'moving': 1, 'addresses': 1, 'within': 1, 'environments': 1, 'one': 1, 'another': 1, 'carry': 1, 'reducing': 1, 'use': 1, 'support': 1, 'next': 1, 'migrate': 1, 'towers': 1, 'continuous': 1, 'overlapping': 1, 'correspondent': 1, 'link': 1, 'kind': 1, 'endpoint': 1, 'devices': 1, 'transparency': 1, 'problem': 1, 'layer': 1, 'defined': 1, 'middle': 1, 'engineering': 1, 'sudden': 1, 'need': 1, 'different': 1, 'goal': 1, 'handover': 1, 'without': 1, 'independent': 1, 'lan': 1, 'used': 1, 'multiple': 1, 'problems': 1, 'wired': 1, 'device': 1, 'man': 1, 'task': 1, 'required': 1, 'maintain': 1, 'solve': 1})
>>> i=1
>>> for t in term:
	sheet2.write(1,i,count[t])
	i=i+1

	

Traceback (most recent call last):
  File "<pyshell#292>", line 2, in <module>
    sheet2.write(1,i,count[t])
  File "C:\Python27\lib\site-packages\xlwt\Worksheet.py", line 1088, in write
    self.row(r).write(c, label, style)
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 236, in write
    self.__adjust_bound_col_idx(col)
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 79, in __adjust_bound_col_idx
    raise ValueError("column index (%r) not an int in range(256)" % arg)
ValueError: column index (256) not an int in range(256)
>>> book.save("tfidf.xls")
>>> def get_tokens():
	with open("ds2.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> count
Counter({'internet': 7, 'protocol': 5, 'generation': 3, 'addressing': 3, 'next': 3, 'version': 3, 'several': 3, 'addresses': 2, 'switched': 2, 'scheme': 2, 'packet': 2, 'computer': 2, 'information': 2, 'network': 2, 'computers': 2, 'provide': 2, 'six': 2, 'also': 2, 'therefore': 2, 'end': 2, 'control': 1, 'layer': 1, 'everyone': 1, 'causes': 1, 'one': 1, 'four': 1, 'addressed': 1, 'connect': 1, 'another': 1, 'upgrades': 1, 'need': 1, 'technology': 1, 'networks': 1, 'gathering': 1, 'help': 1, 'networking': 1, 'would': 1, 'support': 1, 'current': 1, 'nat': 1, 'exhaustion': 1, 'sent': 1, 'define': 1, 'problemsin': 1, 'aspects': 1, 'nature': 1, 'addition': 1, 'possible': 1, 'expansion': 1, 'number': 1, 'warranted': 1, 'host': 1, 'important': 1, 'advantages': 1, 'designed': 1, 'address': 1, 'documented': 1, 'believe': 1, 'data': 1, 'knowledge': 1, 'main': 1, 'route': 1, 'sometimes': 1, 'packets': 1, 'space': 1, 'rfcs': 1, 'large': 1, 'internetwe': 1, 'benefit': 1, 'substantial': 1, 'eliminate': 1, 'hope': 1, 'ipng': 1, 'concering': 1, 'every': 1, 'problem': 1, 'increase': 1, 'starting': 1, 'called': 1, 'specificallycontains': 1})
>>> i=1
>>> for t in term:
	sheet2.write(2,i,count[t])
	i=i+1

	

Traceback (most recent call last):
  File "<pyshell#310>", line 2, in <module>
    sheet2.write(2,i,count[t])
  File "C:\Python27\lib\site-packages\xlwt\Worksheet.py", line 1088, in write
    self.row(r).write(c, label, style)
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 236, in write
    self.__adjust_bound_col_idx(col)
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 79, in __adjust_bound_col_idx
    raise ValueError("column index (%r) not an int in range(256)" % arg)
ValueError: column index (256) not an int in range(256)
>>> book.save("tfidf.xls")
>>> def get_tokens():
	with open("ds3.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> i=1
>>> for t in term:
	sheet2.write(3,i,count[t])
	i=i+1

	

Traceback (most recent call last):
  File "<pyshell#327>", line 2, in <module>
    sheet2.write(3,i,count[t])
  File "C:\Python27\lib\site-packages\xlwt\Worksheet.py", line 1088, in write
    self.row(r).write(c, label, style)
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 236, in write
    self.__adjust_bound_col_idx(col)
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 79, in __adjust_bound_col_idx
    raise ValueError("column index (%r) not an int in range(256)" % arg)
ValueError: column index (256) not an int in range(256)
>>> book.save("tfidf.xls")
>>> sheet2.write(4,0,"tf")
>>> sheet2.write(5,0,"idf")
>>> book.save("tfidf.xls")
>>> max(count)
'wlan'
>>> max(count.values())
18
>>> i=1
>>> for t in term:
	sheet2.write(10,i,count[t]/18)
	i=i+1

	

Traceback (most recent call last):
  File "<pyshell#338>", line 2, in <module>
    sheet2.write(10,i,count[t]/18)
  File "C:\Python27\lib\site-packages\xlwt\Worksheet.py", line 1088, in write
    self.row(r).write(c, label, style)
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 236, in write
    self.__adjust_bound_col_idx(col)
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 79, in __adjust_bound_col_idx
    raise ValueError("column index (%r) not an int in range(256)" % arg)
ValueError: column index (256) not an int in range(256)
>>> book.save
<bound method Workbook.save of <xlwt.Workbook.Workbook object at 0x0000000008BCA3C8>>
>>> book.save("tfidf.xls")
>>> i=1
>>> for t in term:
	sheet2.write(11,i,count[t]/18.0)
	i=i+1

	

Traceback (most recent call last):
  File "<pyshell#345>", line 2, in <module>
    sheet2.write(11,i,count[t]/18.0)
  File "C:\Python27\lib\site-packages\xlwt\Worksheet.py", line 1088, in write
    self.row(r).write(c, label, style)
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 236, in write
    self.__adjust_bound_col_idx(col)
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 79, in __adjust_bound_col_idx
    raise ValueError("column index (%r) not an int in range(256)" % arg)
ValueError: column index (256) not an int in range(256)
>>> book.save("tfidf.xls")

Traceback (most recent call last):
  File "<pyshell#346>", line 1, in <module>
    book.save("tfidf.xls")
  File "C:\Python27\lib\site-packages\xlwt\Workbook.py", line 710, in save
    doc.save(filename_or_stream, self.get_biff_data())
  File "C:\Python27\lib\site-packages\xlwt\CompoundDoc.py", line 262, in save
    f = open(file_name_or_filelike_obj, 'w+b')
IOError: [Errno 13] Permission denied: 'tfidf.xls'
>>> book.save("tfidf.xls")
>>> i=1
>>> for t in term:
	sheet2.write(7,i,count[t]/18.0)
	i=i+1

	

Traceback (most recent call last):
  File "<pyshell#352>", line 2, in <module>
    sheet2.write(7,i,count[t]/18.0)
  File "C:\Python27\lib\site-packages\xlwt\Worksheet.py", line 1088, in write
    self.row(r).write(c, label, style)
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 236, in write
    self.__adjust_bound_col_idx(col)
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 79, in __adjust_bound_col_idx
    raise ValueError("column index (%r) not an int in range(256)" % arg)
ValueError: column index (256) not an int in range(256)
>>> book.save("tfidf.xls")
>>> sheet2.write(7,0,"tf3")
>>> book.save("tfidf.xls")
>>> def get_tokens():
	with open("ds2.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> 
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> count
Counter({'internet': 7, 'protocol': 5, 'generation': 3, 'addressing': 3, 'next': 3, 'version': 3, 'several': 3, 'addresses': 2, 'switched': 2, 'scheme': 2, 'packet': 2, 'computer': 2, 'information': 2, 'network': 2, 'computers': 2, 'provide': 2, 'six': 2, 'also': 2, 'therefore': 2, 'end': 2, 'control': 1, 'layer': 1, 'everyone': 1, 'causes': 1, 'one': 1, 'four': 1, 'addressed': 1, 'connect': 1, 'another': 1, 'upgrades': 1, 'need': 1, 'technology': 1, 'networks': 1, 'gathering': 1, 'help': 1, 'networking': 1, 'would': 1, 'support': 1, 'current': 1, 'nat': 1, 'exhaustion': 1, 'sent': 1, 'define': 1, 'problemsin': 1, 'aspects': 1, 'nature': 1, 'addition': 1, 'possible': 1, 'expansion': 1, 'number': 1, 'warranted': 1, 'host': 1, 'important': 1, 'advantages': 1, 'designed': 1, 'address': 1, 'documented': 1, 'believe': 1, 'data': 1, 'knowledge': 1, 'main': 1, 'route': 1, 'sometimes': 1, 'packets': 1, 'space': 1, 'rfcs': 1, 'large': 1, 'internetwe': 1, 'benefit': 1, 'substantial': 1, 'eliminate': 1, 'hope': 1, 'ipng': 1, 'concering': 1, 'every': 1, 'problem': 1, 'increase': 1, 'starting': 1, 'called': 1, 'specificallycontains': 1})
>>> max(count)
'would'
>>> max(count.values())
7
>>> i=1
>>> for t in term
SyntaxError: invalid syntax
>>> for t in term:
	sheet2.write(6,i,count[t]/7.0)
	i=i+1

	

Traceback (most recent call last):
  File "<pyshell#376>", line 2, in <module>
    sheet2.write(6,i,count[t]/7.0)
  File "C:\Python27\lib\site-packages\xlwt\Worksheet.py", line 1088, in write
    self.row(r).write(c, label, style)
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 236, in write
    self.__adjust_bound_col_idx(col)
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 79, in __adjust_bound_col_idx
    raise ValueError("column index (%r) not an int in range(256)" % arg)
ValueError: column index (256) not an int in range(256)
>>> sheet2.write(6,0,"tf2")
>>> book.save("tfidf.xls")
>>> def get_tokens():
	with open("ds1.txt") as shakes:
		text = shakes.read()
		lowers = text.lower()
		no_punctuation = lowers.translate(None, string.punctuation)
		tokens = nltk.word_tokenize(no_punctuation)
		return tokens

	
>>> tokens = get_tokens()
>>> filtered = [w for w in tokens if not w in stopwords.words('english')]
>>> count = Counter(filtered)
>>> count
Counter({'mobile': 18, 'ip': 13, 'home': 7, 'address': 7, 'node': 7, 'internet': 6, 'host': 5, 'location': 4, 'network': 4, 'systems': 4, 'agent': 4, 'mobility': 3, 'associated': 3, 'users': 3, 'protocol': 2, 'permanent': 2, 'cellular': 2, 'ietf': 2, 'often': 2, 'current': 2, 'roaming': 2, 'care': 2, 'allows': 2, 'changes': 2, 'described': 2, 'seamless': 2, 'wireless': 2, 'datagrams': 2, 'tunnel': 2, 'provide': 2, 'connectivity': 2, 'designed': 2, 'data': 2, 'allow': 2, 'serving': 1, 'move': 1, 'tcp': 1, 'registers': 1, 'implementation': 1, 'local': 1, 'around': 1, 'effects': 1, 'domains': 1, 'maintaining': 1, 'disregarding': 1, 'identified': 1, 'rfc': 1, 'communications': 1, 'underlying': 1, 'found': 1, 'identifies': 1, 'two': 1, 'specifies': 1, 'force': 1, 'tcpipto': 1, 'subnets': 1, 'generation': 1, 'packet': 1, 'static': 1, 'examples': 1, 'visiting': 1, 'away': 1, 'since': 1, 'routing': 1, 'cause': 1, 'across': 1, 'mechanisms': 1, 'however': 1, 'standard': 1, 'proxy': 1, 'change': 1, 'applications': 1, 'many': 1, 'connection': 1, 'extensions': 1, 'act': 1, 'routes': 1, 'moving': 1, 'addresses': 1, 'within': 1, 'environments': 1, 'one': 1, 'another': 1, 'carry': 1, 'reducing': 1, 'use': 1, 'support': 1, 'next': 1, 'migrate': 1, 'towers': 1, 'continuous': 1, 'overlapping': 1, 'correspondent': 1, 'link': 1, 'kind': 1, 'endpoint': 1, 'devices': 1, 'transparency': 1, 'problem': 1, 'layer': 1, 'defined': 1, 'middle': 1, 'engineering': 1, 'sudden': 1, 'need': 1, 'different': 1, 'goal': 1, 'handover': 1, 'without': 1, 'independent': 1, 'lan': 1, 'used': 1, 'multiple': 1, 'problems': 1, 'wired': 1, 'device': 1, 'man': 1, 'task': 1, 'required': 1, 'maintain': 1, 'solve': 1})
>>> max(count.values())
18
>>> i=1
>>> for t in term:
	sheet2.write(4,i,count[t]/18.0)
	i=i+1

	

Traceback (most recent call last):
  File "<pyshell#396>", line 2, in <module>
    sheet2.write(4,i,count[t]/18.0)
  File "C:\Python27\lib\site-packages\xlwt\Worksheet.py", line 1088, in write
    self.row(r).write(c, label, style)
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 236, in write
    self.__adjust_bound_col_idx(col)
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 79, in __adjust_bound_col_idx
    raise ValueError("column index (%r) not an int in range(256)" % arg)
ValueError: column index (256) not an int in range(256)
>>> book.save("tfidf.xls")
>>> sheet2.cell(1,1).value

Traceback (most recent call last):
  File "<pyshell#398>", line 1, in <module>
    sheet2.cell(1,1).value
AttributeError: 'Worksheet' object has no attribute 'cell'
>>> import xlrd

Traceback (most recent call last):
  File "<pyshell#399>", line 1, in <module>
    import xlrd
ImportError: No module named xlrd
>>> sheet2[1][1]

Traceback (most recent call last):
  File "<pyshell#400>", line 1, in <module>
    sheet2[1][1]
TypeError: 'Worksheet' object does not support indexing
>>> pip

Traceback (most recent call last):
  File "<pyshell#401>", line 1, in <module>
    pip
NameError: name 'pip' is not defined
>>> import xlrt

Traceback (most recent call last):
  File "<pyshell#402>", line 1, in <module>
    import xlrt
ImportError: No module named xlrt
>>> import xlrd
>>> sheet2.cell(1,1)

Traceback (most recent call last):
  File "<pyshell#404>", line 1, in <module>
    sheet2.cell(1,1)
AttributeError: 'Worksheet' object has no attribute 'cell'
>>> sheet2.cell(2,2)

Traceback (most recent call last):
  File "<pyshell#405>", line 1, in <module>
    sheet2.cell(2,2)
AttributeError: 'Worksheet' object has no attribute 'cell'
>>> xl_workbook = xlrd.open_workbook("tfidf.xls")
>>> sheet_names = xl_workbook.sheet_names()
>>> print('Sheet Names', sheet_names)
('Sheet Names', [u'Sheet 2'])
>>> sheet.cell(2,2)

Traceback (most recent call last):
  File "<pyshell#409>", line 1, in <module>
    sheet.cell(2,2)
AttributeError: 'Worksheet' object has no attribute 'cell'
>>> sheet.row(0)
<xlwt.Row.Row object at 0x00000000084017D8>
>>> xl_sheet = xl_workbook.sheet_by_index(0)
>>> x1_sheet.cell(2,2)

Traceback (most recent call last):
  File "<pyshell#412>", line 1, in <module>
    x1_sheet.cell(2,2)
NameError: name 'x1_sheet' is not defined
>>> xl_sheet = xl_workbook.sheet_by_index(1)

Traceback (most recent call last):
  File "<pyshell#413>", line 1, in <module>
    xl_sheet = xl_workbook.sheet_by_index(1)
  File "C:\Python27\lib\site-packages\xlrd\book.py", line 432, in sheet_by_index
    return self._sheet_list[sheetx] or self.get_sheet(sheetx)
IndexError: list index out of range
>>> xl_sheet = xl_workbook.sheet_by_index(0)
>>> x1_sheet.row(0)

Traceback (most recent call last):
  File "<pyshell#415>", line 1, in <module>
    x1_sheet.row(0)
NameError: name 'x1_sheet' is not defined
>>> sheet=x1_workbook.get_sheet_by_name('Sheet2')

Traceback (most recent call last):
  File "<pyshell#416>", line 1, in <module>
    sheet=x1_workbook.get_sheet_by_name('Sheet2')
NameError: name 'x1_workbook' is not defined
>>> xl_workbook
<xlrd.book.Book object at 0x0000000008C2A9E8>
>>> xl_workbook.get_sheet_by_name('Sheet2')

Traceback (most recent call last):
  File "<pyshell#418>", line 1, in <module>
    xl_workbook.get_sheet_by_name('Sheet2')
AttributeError: 'Book' object has no attribute 'get_sheet_by_name'
>>> book = xlrd.open_workbook("tfidf.xls")
>>> print book.nsheets
1
>>> print book.sheet_names()
[u'Sheet 2']
>>> first_sheet = book.sheet_by_index(0)
>>> print first_sheet.row_values(0)
[u'', u'serving', u'protocol', u'move', u'tcp', u'registers', u'implementation', u'permanent', u'location', u'local', u'around', u'effects', u'cellular', u'domains', u'maintaining', u'ietf', u'disregarding', u'identified', u'rfc', u'communications', u'underlying', u'found', u'identifies', u'two', u'specifies', u'force', u'often', u'tcpipto', u'subnets', u'generation', u'packet', u'static', u'examples', u'home', u'network', u'visiting', u'away', u'since', u'current', u'routing', u'internet', u'cause', u'across', u'mechanisms', u'however', u'standard', u'host', u'proxy', u'address', u'roaming', u'change', u'care', u'applications', u'many', u'allows', u'connection', u'extensions', u'act', u'routes', u'moving', u'changes', u'addresses', u'mobility', u'within', u'environments', u'one', u'another', u'carry', u'reducing', u'use', u'described', u'support', u'seamless', u'next', u'migrate', u'systems', u'towers', u'continuous', u'overlapping', u'wireless', u'datagrams', u'correspondent', u'link', u'kind', u'endpoint', u'tunnel', u'devices', u'transparency', u'problem', u'layer', u'associated', u'defined', u'ip', u'agent', u'middle', u'engineering', u'sudden', u'need', u'different', u'goal', u'provide', u'handover', u'without', u'node', u'independent', u'lan', u'used', u'multiple', u'users', u'problems', u'connectivity', u'wired', u'designed', u'device', u'data', u'man', u'task', u'mobile', u'required', u'maintain', u'solve', u'allow', u'control', u'layer', u'everyone', u'protocol', u'addresses', u'switched', u'generation', u'scheme', u'causes', u'addressing', u'packet', u'one', u'four', u'addressed', u'computer', u'connect', u'another', u'upgrades', u'need', u'technology', u'networks', u'gathering', u'help', u'information', u'networking', u'network', u'would', u'computers', u'provide', u'support', u'six', u'next', u'current', u'also', u'version', u'therefore', u'nat', u'internet', u'exhaustion', u'several', u'sent', u'define', u'problemsin', u'aspects', u'nature', u'addition', u'possible', u'expansion', u'number', u'warranted', u'host', u'important', u'advantages', u'designed', u'address', u'end', u'documented', u'believe', u'data', u'knowledge', u'main', u'route', u'sometimes', u'packets', u'space', u'rfcs', u'large', u'internetwe', u'benefit', u'substantial', u'eliminate', u'hope', u'ipng', u'concering', u'every', u'problem', u'increase', u'starting', u'called', u'specificallycontains', u'understand', u'major', u'wlan', u'whenever', u'point', u'previously', u'ip', u'move', u'mainly', u'equally', u'environments', u'one', u'connections', u'cant', u'used', u'ipv', u'another', u'need', u'home', u'still', u'denotes', u'link', u'defines', u'information', u'accomplish', u'network', u'six', u'moves', u'capabilities', u'tis', u'version', u'reachable', u'attachment', u'internet', u'expected', u'nodes', u'several', u'maintain', u'location', u'node', u'added', u'terms', u'regardless', u'targeted', u'standard', u'bwa', u'wimax', u'wired', u'fixedip', u'although', u'address', u'changing', u'roaming', u'existing']
>>> 
KeyboardInterrupt
>>> cell = first_sheet.cell(1,1)
>>> print cell
number:1.0
>>> print cell.value
1.0
>>> print cell.value*9
9.0
>>> i=1
>>> j=1
>>> for i in 256:
	for j in 3:
		if cell.
		
SyntaxError: invalid syntax
>>> 
>>> i=1
>>> j=1
>>> c=0
>>> for i in 256:
	for j in 3:
		if first_sheet.cell(i,j)!= 0:
			c++
			
SyntaxError: invalid syntax
>>> c++
SyntaxError: invalid syntax
>>> i=1
>>> j=1
>>> c=0
>>> for i in 256:
	for j in 3:
		if first_sheet.cell(i,j)!= 0:
			c=c+1
			j=j+1

			

Traceback (most recent call last):
  File "<pyshell#450>", line 1, in <module>
    for i in 256:
TypeError: 'int' object is not iterable
>>> for i in 256:
	for j in 3:
		if first_sheet.cell(i,j)!= 0:
			c=c+1
			j=j+1

			sheet2.write(15,i,c/3.0)
			i=i+1

			

Traceback (most recent call last):
  File "<pyshell#453>", line 1, in <module>
    for i in 256:
TypeError: 'int' object is not iterable
>>> for i in range(256):
	for j in range(3):
		if first_sheet.cell(i,j)!= 0:
			c=c+1
			j=j+1

			sheet2.write(15,i,c/3.0)
			i=i+1

			

Traceback (most recent call last):
  File "<pyshell#455>", line 7, in <module>
    sheet2.write(15,i,c/3.0)
  File "C:\Python27\lib\site-packages\xlwt\Worksheet.py", line 1088, in write
    self.row(r).write(c, label, style)
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 248, in write
    self.insert_cell(col, NumberCell(self.__idx, col, style_index, label))
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 160, in insert_cell
    raise Exception(msg)
Exception: Attempt to overwrite cell: sheetname=u'Sheet 2' rowx=15 colx=1
>>> for i in range(256):
	for j in range(3):
		if first_sheet.cell(i,j)!= 0:
			c=c+1
			j=j+1

			sheet2.write(16,i,c/3.0)
			i=i+1


Traceback (most recent call last):
  File "<pyshell#456>", line 7, in <module>
    sheet2.write(16,i,c/3.0)
  File "C:\Python27\lib\site-packages\xlwt\Worksheet.py", line 1088, in write
    self.row(r).write(c, label, style)
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 248, in write
    self.insert_cell(col, NumberCell(self.__idx, col, style_index, label))
  File "C:\Python27\lib\site-packages\xlwt\Row.py", line 160, in insert_cell
    raise Exception(msg)
Exception: Attempt to overwrite cell: sheetname=u'Sheet 2' rowx=16 colx=1
>>> book.save("tfidf.xls")

Traceback (most recent call last):
  File "<pyshell#457>", line 1, in <module>
    book.save("tfidf.xls")
AttributeError: 'Book' object has no attribute 'save'
>>> 



