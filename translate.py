import urllib
import sys
#usage: python translate.py apple
#doc: http://code.google.com/apis/language/translate/v1/using_rest_translate.html
src="en" #source language
dst="tr" #destinasion language

try:
	word=sys.argv[1]
except:
	print '\n usage: python translate.py apple\n\tpython translate.py "what is this"\n'
	sys.exit()

response=urllib.urlopen("https://ajax.googleapis.com/ajax/services/language/translate?v=1.0&q="+word+"!&langpair="+src+"|"+dst).read()
response2=urllib.urlopen("https://ajax.googleapis.com/ajax/services/language/translate?v=1.0&q="+word+"!&langpair="+dst+"|"+src).read()
null=0
exec("d="+response) #response text olarak geliyor. response u dict yapiyorum.
exec("d2="+response2)
print response

print d['responseData']['translatedText']+" = "+d2['responseData']['translatedText']
