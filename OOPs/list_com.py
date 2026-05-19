# all numbers from 1-1000 that contains 3 

w = [a for a in range(1,1001) if "3" in str(a) ]
print(w)

# count the number of spaces in string
a = "this is a question count the number of spaces in string"
spac = [s for s in a if s==" "]
print(len(spac))

'''
Create a list of all the consonants in the string "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
'''
a = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
vowels = 'a,e,i,o,u," "'
lst = [cons for cons in a if cons not in  vowels ]
print(lst)

# result = [letter for letter in sentence if letter not in 'a,e,i,o,u, " "']

'''Get the index and the value as a tuple for items in the list 
“hi”, 4, 8.99, ‘apple’, (‘t,b’,’n’). Result would look like (index, value), (index, value)'''
w = "hi", 4, 8.99, "apple", ("t","b","n")
a = [(x,y) for x,y in enumerate(w)]
print(a)

'''Find the common numbers in two lists (without using a tuple or set)
list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5'''
lista = [1,2,3,4]
listb = [2,3,4,5]
w = [a for a in lista if a in listb]
print(w)

'''
Get only the numbers in a sentence like 'In 1984 there were 13 instances of a protest with
 over 1000 people attending'.  Result is a list of numbers like [3,4,5]
'''

# a ='In 1984 there were 13 instances of a protest with over 1000 people attending'
sentence = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
words = sentence.split()
result = [number for number in words if number.isdigit() ]
print(result)

'''
Given numbers = range(20), produce a list containing the word 'even' if a number in the numbers
 is even, and the word 'odd' if the number is odd.  Result would look like ['odd','odd', 'even']
'''
numbers = ['even' if n %2==0  else 'odd' for n in range(20)]
print(numbers)
