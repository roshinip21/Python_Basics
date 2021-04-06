
from collections import Counter
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])

#To determine how many items a dictionary has, use the len() function:
print(len(thisdict))

#The values in dictionary items can be of any data type:
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

#Get the value of the "model" key:
x = thisdict["model"]  # or same as  x = thisdict.get("model")

thisdict["color"] = "white"    #can update dict 

#The update() method will update the dictionary with the items from the given argument.
#The argument must be a dictionary, or an iterable object with key: value pairs.
thisdict.update({"year": 2020, "heu": 56})  # can be 1 or more key:value pairs

#The keys() method will return a list of all the keys in the dictionary.
x = thisdict.keys()
print(x)

#Get a list of the values:
y = thisdict.values()
print(y)

#Get a list of the key: value pairs
x = thisdict.items()

#To determine if a specified key is present in a dictionary use the in keyword:
if "model" in thisdict:   
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#The pop() method removes the item with the specified key name:
thisdict.pop("model")

#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead coz unordered):
thisdict.popitem()

#The del keyword removes the item with the specified key name:

del thisdict["model"]
print(thisdict)

del thisdict   # to delete entire dict
thisdict.clear() # clears the dict values and makes it empty

#----------------------------------------------------------------------------------------------------------------
# to find common leters/childs in both strings

def commonChild(s1, s2):
    a = Counter(s1)
    b = Counter(s2)
    common = a & b
    print(common)
    if len(common) > 0:
        return len(common)
    else:
        return(0)


a = "OUDFRMYMAW"
b = "AWHYFCCMQX"
print(commonChild(a, b))


#https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dictionaries-hashmaps&isFullScreen=true
# Dictionary and strings mix
'''Sample Input
2
hello
world
hi
world

Sample Output YES NO
Explanation We have 2 pairs to check: hello,world -  The substrings o and l are common to both strings. hi, world share no common substrings. '''
from collections import Counter
def twoStrings(s1, s2):
    a=Counter(s1)
    b=Counter(s2)
    if a==b:
        return("YES")
    
    x=a&b   
    
    if len(x)>0:
        return("YES")
    else:
        return("NO")    

q = int(input())           # multiple test cases
for q_itr in range(q):
    s1 = input()

    s2 = input()

    result = twoStrings(s1, s2)
    print(result)

#--------------------------------------------------------------------------------------------------------------------------
#DICT and STR Checking
# https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
''' 
Function must print "Yes" if the note can be formed using the magazine, or "No". 
Sample Input 6 4
give me one grand today night  #magazine array
give one grand today           #note array

Sample Output Yes '''


def checkMagazine(magazine, note):
    x=Counter(magazine)
    y=Counter(note)
    z=x&y            
    if z==y:
        print("Yes")
    else:
        print("No")


mn=input().split()
m=int(mn[0])
n=int(mn[1])
magazine=input().rstrip().split()     #returns list of magazine words
note=input().rstrip().split()         # '' '' '' of note words
checkMagazine(magazine, note)
