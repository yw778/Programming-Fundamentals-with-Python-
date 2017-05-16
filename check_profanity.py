import urllib

def read_txt():
	quotes = open("/Users/yuwang/Desktop/daily notes/movie_quotes.txt")
	contents = quotes.read()
	print(contents)
	quotes.close()
	check_profanity(contents)

def check_profanity(contents):
	# mac terminal hard to jump over the firewall
	connetction = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + contents)
	# connetction = urllib.urlopen("http://www.baidu.com")
	response = connetction.read()
	if "true" in response: 
		print("curse words in query string")
	elif "false" in response:
		print("no curse words")
	else:
		print("defalut")
	connetction.close()


read_txt()