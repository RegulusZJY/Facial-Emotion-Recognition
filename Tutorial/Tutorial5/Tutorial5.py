'''
    Zhang Junyan, 1129832
    Lin Qingxin, 1098238
'''
import re
string1 = "abb29ABCLK%lCnrDBCabbbb"
print('Question1:')
# Q1: produce
'''
    For regular expressions
    the numbers in curly braces {}
    represent the exact matching of n expressions
    so b{4} will be matched to bbbb
    Then, use "a" in front to limit the scope
    that is, start with a, followed by b{4}
    then we can get the correct match "abbbb"
'''
if re.search((r'a(b{4})',string1)[0],string1):
    # Group [0] used to find the first match.
    print('Found a match:',re.search(r'a(b{4})',string1)[0])
else:
    print('No match.')

print('\n''Question2:')
# Q2: re.search
'''
    The string described by the regular expression:
    [A-Z][a-z]+
    will contain one or more uppercase characters
    followed by one or more lowercase characters.
    Output is <re.Match object; span=(12, 15), match='Cnr'>
    Span = (12, 15) indicates that <string>
    finds the matching part: Cnr,
    which contains first uppercase character C
    and followed by and end by lowercase character nr
    Cabbbb is the second search so doesn't show this result
'''
print(re.search("[A-Z][a-z]+",string1))
# To check whether exist a match.
if re.search('[A-Z][a-z]', string1):
    # Group [0] used to find the first. If find it, print the first match
    print('Found a match:',re.search("[A-Z][a-z]+",string1)[0])
else:
    print('No match.')
