
import re


mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
no: +919926385540
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiinaiiiiiiiiiiiiai'''






'''Meta Characters
[]	A set of characters
\	Signals a special sequence (can also be used to escape special characters)
.	Any character (except newline character)
^	Starts with
$	Ends with
*	Zero or more occurrences
+	One or more occurrences
{}	Exactly the specified number of occurrences
|	Either or
()	Capture and group


Special Sequences
\A	Returns a match if the specified characters are at the beginning of the string
\b	Returns a match where the specified characters are at the beginning or at the end of a word 
\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
\d	Returns a match where the string contains digits (numbers from 0-9)
\D	Returns a match where the string DOES NOT contain digits
\s	Returns a match where the string contains a white space character
\S	Returns a match where the string DOES NOT contain a white space character
\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
\W	Returns a match where the string DOES NOT contain any word characters
\Z	Returns a match if the specified characters are at the end of the string'''



#..... SPECIAL CHARACTERS.....#



#patt = re.compile(r".map")
#patt = re.compile(r".north")
#patt = re.compile(r"^Tata")
#patt = re.compile(r"ii$")
#patt = re.compile(r"ai*")
#patt = re.compile(r"a*i*")
#patt = re.compile(r"ai+")
#patt = re.compile(r"Ta{1}")
#patt = re.compile(r"(ai){2}")
#patt = re.compile(r"ai{2}|t{1}")




#..... SPECIAL SEQUENCES.......#


#patt = re.compile(r"\ATata")
#patt = re.compile(r"\bTata")
#patt = re.compile(r"Tata\b")
#patt = re.compile(r"\Brica")
#patt = re.compile(r"\d78")
#patt = re.compile(r"\D{5}")
#patt = re.compile(r"\sTata")
#patt = re.compile(r"\Snorth")
#patt = re.compile(r"\wTata")
#patt = re.compile(r"\WTata")
#patt = re.compile(r"(ai){1}\Z")
#patt = re.compile(r"91\d{10}")




'''matches = patt.finditer(mystr)
for match in matches:
    print(match)'''
    
    

'''txt = "Thes rain in Spain"
x = re.findall("^T.*n$", txt)
print(x)'''






#Match object..
'''txt = "Thes rain in Spain"
x = re.search("a.*n",txt)
print(x.span(),x.string,"\n",x.group())'''



'''string = "The rain in Spain"
x = re.search("\s",string)
print("The first white-space character is located in position:", x.span())'''


'''string = "The rain in Spain"
x = re.split("a.n", string)
print(x)'''


'''string = "The rain in Spain"
x = re.sub("a.n","done", string,1)
print(x)'''



string = "The rain in Spain"
x = re.findall("[a-n]", string)
print(x)










    




