
# p = input().strip(' ').split()
#input      heyy op hii beth

# op    p = ['heyy', 'op', 'hii', 'beth']


#adding elements into list in 3 ways
l=[] 
l.append(1) #adds ele at last
l.extend([34,87,"YO","HEy","SUPP"])
print(l)
l.insert(3,"Rosh") #insert at pos 3 
l.extend(["XYZ",9090]) #extends list at last SPECIFY LIST ,or considered like append
print(l) 
p=[3,5,1,8]
l.extend(p)
print("List l :{0} \nList p:{1}".format(l,p))

#deleting elements

p.pop()     #deleting last ele
print(p)
p.pop(1)      # deleting by specifying pos
print(p)
l.remove(1)  # removes element 1 from list (Only first occurence)
print(l)
del p          #deleting entire list
try:
    print(p)
   
except (NameError):
    print("Not found p")    

try:
    print(l[100])             
except IndexError:
    print("Index error")


#list methods

sort_list=[4,76,90,43,56,21,87]
print(sort_list.index(90))  #to find index of element
sort_list1=[]
sort_list1.extend(sort_list)    #copying same list 
sort_list.sort()                # sorting in place usinf sort method

print("sort_list:",sort_list)            

op=sorted(sort_list1)           # using sorted function which does not affect original list
print("sort_list1:",sort_list1)
print("sorted list:",op)

op.sort(reverse=True)        #to get in descending order
print(op)

# to reverse list 
op.reverse() 
print(op)   

print(len(op))        #length of list


# to create a unique list without duplicates
def remdup(l):
    return(myremdup(l, []))


def myremdup(l, s):
    if l == []:
        return([])
    else:
        if l[0] in s:
            return(myremdup(l[1:], s))
        else:
            return([l[0]]+myremdup(l[1:], s+[l[0]]))


l = [1, 2, 4, 5, 2]
L1 = remdup(l)

print(L1)
