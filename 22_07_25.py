# 1.Reverse the num without converting into string?
# def sam(n,res=0):
#     while n>0:
#         l=n%10
#         res=res*10+l
#         n=n//10
#     print(res)
# sam(12345)
# -----------------------------------------------------------
# 2.Find the First Non-Repeating Character. input="swiss"
# def sam(s,d={}):
#     for i in s:
#         if i not in d:
#             d[i]=1
#         else:
#             d[i]+=1
#     print(d)
#     for j,k in d.items():
#         if k==1:
#             return j
# print(sam('swiss'))
# -------------------------------------------------------------
# 3.Find the Missing Number in an Array.input=[1, 2, 3, 5]
# def sam(l,c=0,out=[]):
#     for i in range(0,len(l)+1):
#         out+=[l[0]+c]
#         c+=1
#     return out
# print(sam([1, 2, 3, 5]))
# ----------------------------------------------------------------
# 4.Find Duplicate Number (Array of n+1 Integers). input=[3, 1, 3, 4, 2,2]
# def sam(l,d={}):
#     for i in l:
#         if i not in d:
#             d[i]=1
#         else:
#             d[i]+=1
#     print(d)
#     for key,value in d.items():
#         if value>1:
#             print(key)
# sam([1,2,3,4,2,3,3])
# -----------------------------------------------------------
# 5. Check if Two Strings are Anagrams.
# def sam(s1,s2):
#     if len(s1)!=len(s2):
#         return False
#     d={}
#     for i in s1:
#         d[i]=d.get(i,0)+1
#     print(d)
#     for i in s2:
#         if i not in d or d[i]==0:
#             return False
#         d[i]-=1
#     return True
# print(sam('listen','silent'))
# print(sam('apple','pale'))
# print(sam('hello','world'))
# ---------------------------------------------------------
# 6. Check if a Number is Power of Two.
# def power(n):
#     if n<=0:
#         return False
#     while n%2==0:
#         n=n//2
#     return n==1
# num=int(input('enter the num'))
# if power(num):
#     print(f"{num} is power of two")
# else:
#     print(f"{num} is not power of two")
# ----------------------------------------------------
# 7. Find the Majority Element (Appears More than n/2 times). input=[3, 2, 3]
# def sam(l):
#     d={}
#     for i in l:
#         if i not in d:
#             d[i]=1
#         else:
#             d[i]+=1
#     print(d)
#     n=len(l)//2
#     for k,v in d.items():
#         if v>=n:
#             return k
# res=sam([1,2,3,4,3])
# print(res)
# ------------------------------------------------------
# n1=int(input('enter the num'))
# n2=int(input('enter the num'))
# choice=int(input('enter the choice'))
# if choice==1:
#     print(n1+n2)
# elif choice==2:
#     print(n1-n2)
# elif choice==3:
#     print(n1*n2)
# elif choice==4:
#     print(n1/n2)
# else:
#     print(n1//n2)
# -----------------------------------------------------------
# simple calculator program
# def calculator(exp):
#     return eval(exp)
# print(calculator(('3+2*5')))
# ----------------------------------------------------------
# l=['flite','flow','flower','flask']
# out={}
# for i in l:
#     for j in range(0,len(i)):
#         if i[j] not in out:
#             out[i[j]]=1
#         else:
#             out[i[j]]+=1
# print(out)
# for k,v in out.items():
#     if v==len(l):
#         print(k,end="")
# -----------------------------------------------------------
# 8..Find All Subsets of an Array.input= [1, 2, 3]
# Output: [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]

# def subsets(l):
#     res=[[]]
#     for num in l:
#         res+=[i+[num] for i in res]
#     return res
# print(subsets([1,2,3]))
# --------------------------------------------------------------
