def isValid(self, s: str) -> bool:              #leetcode best ans
    bracket_map = {"(": ")", "[": "]",  "{": "}"}
    open_par = set(["(", "[", "{"])
    stack = []
    for i in s:
        if i in open_par:
            stack.append(i)
        elif stack and i == bracket_map[stack[-1]]:
            stack.pop()
        else:
            return False
    return stack == []


def isBalanced1(s):            #easy and better
    stack = []
    input1 = s
    Op_brk = ["(", "[", "{"]
    matches = [("(", ")"), ("[", "]"), ("{", "}")]
    Cl_brk=[")","]","}"]
    if input1 == "":
        return "YES"
    if len(input1) % 2 == 1:
        return "NO"

    for i in input1:
        if i in Op_brk:
            stack.append(i)
        if i in Cl_brk:
            if len(stack) == 0:
                return "NO"
            T = stack.pop()
            if (T, i) not in matches:
                return "NO"

    if len(stack) == 0:
        return "YES"
    else:
        return "NO"



def isBalanced(s):             # longer isbalanced func code
    stack=[]
    input1=s
    Op_brk=["(","[","{"]
    Cl_brk=[")","]","}"]
    if input1=="":
        return "YES"
    if len(input1)%2 == 1:
        return "NO" 
      
    for i in input1:
        if i in Op_brk:
            stack.append(i)            
        if i in Cl_brk:
            if len(stack)==0:
                return "NO"
            T=stack.pop() 
            if i == ")" and (T == "[" or T == "{"):  
                return "NO"
            if i == "]" and (T == "(" or T == "{"):  
                return "NO"
            if i == "}" and (T == "[" or T == "("):    
                return "NO"
               
    if len(stack)==0:
        return "YES"
    else: 
        return "NO"
 
if __name__ == '__main__':
    t = int(input())        #testcase no.
    for t_itr in range(t):
        s = input("Enter the input:") 
        result = isBalanced(s)
        print("It is valid-yes,not valid-no: ",result)
