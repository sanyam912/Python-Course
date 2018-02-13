# A set is an unordered collection with no duplicate elements. Basic uses include membership,testing and eliminating duplicate entries.
# Set objects also support mathematical operations like union, intersection, difference and symmetric difference.
# Duplicacy removed

b = {'apple','orange','apple','pear','orange','banana'}
print (b)

print ('orange' not in b)              # fast membership testing

#Demonstrate set operations on unique letters from two  words

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
#letters in a but not in b
print(a-b)

#letters in either a or b
print(a|b)

#letters in both a and b
print(a&b)

#letters in a or b but not both
print(a ^ b)

#########################################################################################################################################################
