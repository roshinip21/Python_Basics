'''

how to take input and auto create list in py 

# p = input().strip(' ').split()
#input      heyy op hii beth

# output    p = ['heyy', 'op', 'hii', 'beth']

'''
in_name = input("enter a name:")
print(in_name[2:6])  #string slicing

sentence = "how are you rosh? Its a fun swell day"
count = 0
for letter in sentence:
    if letter == 'o':
        count+=1

print(count+"is the total no. of o's in the sentence")




# Python program to check if a string is palindrome or not
# can use s[::-1] and easily do w = x[::-1]

x = "malayalam"
w=""
 
for i in x:
  w = i + w
 
if (x == w):
    print("Yes")
else:
    print("No")
'''
	#C++ 
	int isPalindrome(string S)
	{
	    // Your code goes here
	    int flag;
	    int x=S.length();
	    for(int i=0;i<x;i++) {
	       if (S[i]!=S[x-i-1])
	           flag=1;}
	           
	       if (flag)
	         return 0;
	       else
	          return 1;
	                 
	}

'''
#Q Longest Palindromic Substring of a string [leetcode best ans]

#Given a string s, return the longest palindromic substring in s

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if (s==None or len(s) < 1):
            return ""
        #def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
           # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
        # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res 

# get the longest palindrome, l, r are the middle indexes
# from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1  
        return s[l+1:r]


'''Q1Given a String S, reverse the string without reversing its individual words. Words are separated by dots.
Example 1: Input:
S = i.like.this.program.very.much
Output: much.very.program.this.like.i
s="i.like.this.program.very.much" '''
# https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/1#_=_

from collections import Counter
def reverseWords(s):
    l=[]
    l=s.split('.')    # split str based on . to produce list
    print(l)
    l.reverse()        # reverse list using built in func, dont complicate using loops and slices

    #['much', 'very', 'program', 'this', 'like', 'i']

    x=".".join(l)         # take reversed list as iterable and join using .  to produce str output "join produces str as op"     
    print(x,end="")       #do end="" for single word testcase ex; s=abc
    return x

o="i.like.this.program.very.much"
reverseWords(o)
#----------------------------------------------------------------------------------------------------------------------
#Q ANAGRAM of two strings
# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
#Q  https://www.geeksforgeeks.org/using-counter-python-find-minimum-character-removal-make-two-strings-anagram/?ref=rp

#Print a single integer denoting the number of characters you must "delete" to make the two strings anagrams of each other.(Anagram-str having same chars and equal length strs)
#Sample Input cde abc
#Sample Output : 4


def makeAnagram(a, b):
    # make dictionaries from both strings
    # counter is a unordered subset of the class dict
    c1 = Counter(a)
    # it creates dict having chars as keys and count of char as val(unordered)
    c2 = Counter(b)

    # finding the common elements from both dictonary
    common = c1 & c2   # counter intersection operation
    value = 0

    # adding up the key from common dictionary in order
    # to get the total number of common elements
    for key in common:
        # common[key] gives dict val having count of chars
        value = value + common[key]
        print(common[key])

    # returning the number of elements to be
    # removed to form an anagram
    #return abs((max(len(a),len(b))-value))    This will not work for all testcases
    return (len(a)-2*value + len(b))  # apt sol formula


print("No. of deletions to make anagram are:", makeAnagram(
    "avvyh", "dcbba"))  # pass strings to func defn


# OR THIS TYPE  https://practice.geeksforgeeks.org/problems/anagram/0
# Python program to check whether two strings are
# anagrams of each other (Here just checking)


def Anagram(a, b):
    if (sorted(a) == sorted(b)):
        print("YES")
    else:
        print("NO")


T = int(input())
while(T > 0):  # for multiple testcases

    a, b = input().split()       # ex abcd abbcd  ,so split to assign each line

    Anagram(a, b)
    T -= 1

#OR little bigger version below


def areAnagram(str1, str2):

    # Get lengths of both strings

    n1 = len(str1)
    n2 = len(str2)
    # If length of both strings is not same, then
    # they cannot be anagram
    if n1 != n2:
        return 0

    # Sort both strings
    str1 = sorted(str1)
    str2 = sorted(str2)

    # Compare sorted strings
    for i in range(0, n1):
        if str1[i] != str2[i]:
            return 0
    return 1


# Driver program to test the above function
str1 = "test"
str2 = "ttew"

if areAnagram(str1, str2):
    print("The two strings are anagram of each other")
else:
    print("The two strings are not anagram of each other")

#---------------------------------------------------------------------------------------------------------------------

#Q https://practice.geeksforgeeks.org/problems/pangram-checking-1587115620/1/
#Given a string check if it is Pangram or not. A pangram is a sentence containing every letter in the English Alphabet.
#Example 1: Input:S = Bawds jog, flick quartz, vex nymph Output: 1

def pangram(s):
    s.strip("")
    s.strip(",")
    s.strip(".")
    l = list(s)
    l.sort()
    x = str(l)
    a = "abcdefghijklmnopqrstuvwxyz"
    if x in a:
        print("1")
    elif a in x:
        print("1")
    else:
        print("0")


#tough testcase q
q = "qghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvsrtkjprepggxrpnrvystmwcysyyc pevikeffmznimkkasvwsrenzkycxfxtlsgypsfadpooefxz coejuvpvaboygpoeylfpbnpljvrvipyamyehwqnqrqpmxujjloovaowuxwhmsncbxcoksfzkvatxdknlyjyhfixjswnkkufnux zrzbmnmgqooketlyhnkoaugzqrcddiuteiojwayyzpvscmpsajlfvgubfaaovlzylntrkdcpwsrtesjwhdizco zcnfwlqijtvdwvxhrcbldvgylw busbmborxtlhcsmpxohgmgnkeufdxotogbgxpeyanfetcukepzshkljugggekjdqzjenpevqgxiepjsrdzj zujllchhbfqmkimwzobiwybxd unfsksrsrtekmqdcyzjeeuhmsrqcozijipfioneeddpszrnavymmtatbdzqso muvnpppsuacbazuxm ecthlegrpunkdm ppweqtgjoparmo zdqyoxytjbbhawdydcprjbxphoohpkwqyuhrqzhnbnfuvqnqqlr jpxiogvliexdzuzosrkrusvojbrzmwzpowkjilefraamdigpnpuuhgxpqnjwjmwaxxmnsnhhlqqr udltfzotcjtnzxuglsdsmzcnockvfajfrmxothowkbjzwucwlj rimpmyhchzriwkbarxbgfcbceyhjugixwtbvtreh bcpxifbxvfbcgkcf ckcotzgkubmjrmbsztsshfroefwsjrxjhguzyupzwweiqurpixiqflduuve owqcudhnefnjhaimuczfskuiduburiswtbrecuykabfcvkdzeztoidukuhjzefczzzbfkqdpqzikfobucdhthxdjgkjelrl axamceroswitdptp clifkeljyti rcqaybnefxnxvgzedyyhngyc ru................."
pangram(q)

# EASIEST SOLUTION
def pangramsol(s):
    a = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(26):
        if a[i] not in s:
            return False

    return True


print(pangramsol(q))
 
#-------------------------------------------------------------------------------------------------------------
#Q https: // www.geeksforgeeks.org/program-print-substrings-given-string/
#Program to print all substrings of a given string
#Given a string as an input. We need to write a program that will print all non-empty substrings of that given string.

def subString(s, n):
    # Pick starting point in outer loop
    # and lengths of different strings for
    # a given starting point
    for i in range(n):
        for j in range(i+1, n+1):        # n+1 to print last Nth val of string
            # takes slice s[0:1] prints a, s[0:2] prints ab and so on
            print(s[i:j])

# Driver program to test above function
s = "abcd"
subString(s, len(s))


#  OR THIS SOLUTION Both EAsy
def printAllSubstrings(s, n):
 # Fix start index in outer loop.
    # Reveal new character in inner loop till end of string.
    # Print till-now-formed string.
    for i in range(n):
        temp = ""
        for j in range(i, n):
            # temp="" , later a , later a+b=ab , ab+c so on
            temp += s[j]
            print(temp)

# Driver program to test above function
s = "Geeky"
printAllSubstrings(s, len(s))

#------------------------------------------------------------------------------------------------------------------------------------
#Q Alternating ABAB or BABAB or A or B

# https: // www.hackerrank.com/challenges/alternating-characters/problem?h_l = interview & playlist_slugs % 5B % 5D = interview-preparation-kit & playlist_slugs % 5B % 5D = strings
#Input Format The first line contains an integer, the number of queries.
#The next lines each contain a string "s".
#Constraints --- Each string will consist only of characters A and B
#Output Format  --- For each query, print the minimum number of deletions required on a new line.

n = int(input())  # no. of iterations
for _ in range(n):
    count = 0
    word = input()  # input str
    for i in range(len(word) - 1):           # len(word)- 1 as if we do len(s or word) only it becomes out of index in if condition.
        if word[i] == word[i + 1]:              # so use len()-1 , as last char checked in i+1
            count += 1
    print(count)
#OR same as a function


def Alternate(s, n):
    count = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            count += 1
    return count


s = "ABABAAABBB"
x = Alternate(s, len(s))
print("No. of deletions reqd for s are:", x)


#--------------------------------------------------------------------------------------------------------------

#Q  https://practice.geeksforgeeks.org/problems/minimum-indexed-character-1587115620/1/
# Given a string str and another string patt. Find the character in patt that is present at the minimum index in str.
# If no character of patt is present in str then print ‘No character present’.
#Example 1:Input: str =geeksforgeeks patt =set  Output:e
# Explanation: e is the character which is present in given patt "geeksforgeeks"and is first found in str "set".

def minIndexChar(str, pat):
    #code here

    for i in str:
        if i in pat:
            return (str.index(i))

    return -1

#----------------------------------------------------------------------------------------------
#not sure about Q

def substrCount(n, s):
    count = 0

    prevprevChar, prevprevCount = None, 0
    prevChar, prevCount = None, 0
    currentChar, currentCount = None, 0

    for char in s:
        if char != currentChar:
            prevprevChar, prevprevCount = prevChar, prevCount
            prevChar, prevCount = currentChar, currentCount
            currentChar, currentCount = char, 0

        currentCount += 1
        count += currentCount

        if prevCount == 1 and prevprevChar == currentChar and currentCount <= prevprevCount:
            count += 1

    return count


def substrCount(n, s):

    count = n

    # tracks the last three sequences of unique characters
    # seqx = length of the sequence
    # seqx_c = character in that sequence
    seq3, seq3_c = 0, ""
    seq2, seq2_c = 0, ""
    seq1, seq1_c = 1, s[0]

    # note: because the slice starts at 1, i is one less than the index of char
    for i, char in enumerate(s[1:]):
        if char == s[i]:
            count += seq1
            seq1 += 1
        else:
            seq3, seq3_c = seq2, seq2_c
            seq2, seq2_c = seq1, seq1_c
            seq1, seq1_c = 1, char

        if seq2 == 1 and seq3 >= seq1 and seq3_c == seq1_c:
            count += 1

    return count
