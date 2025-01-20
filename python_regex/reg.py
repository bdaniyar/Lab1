import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

#Example 2
"""
findall	Returns a list containing all matches
search	Returns a Match object if there is a match anywhere in the string
split	Returns a list where the string has been split at each match
sub	Replaces one or many matches with a string

"""
"""
[]	A set of characters	"[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	"\d"	
.	Any character (except newline character)	"he..o"	
^	Starts with	"^hello"	
$	Ends with	"planet$"	
*	Zero or more occurrences	"he.*o"	
+	One or more occurrences	"he.+o"	
?	Zero or one occurrences	"he.?o"	
{}	Exactly the specified number of occurrences	"he.{2}o"	
|	Either or	"falls|stays"	
()	Capture and group
"""

#Example 4
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
#Example 5
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

#Example 6
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

#Example 7
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

#Example 8
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
