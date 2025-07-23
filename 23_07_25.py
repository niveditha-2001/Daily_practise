# arr=[10,50,20,40,30]
# n=int(input("enter the _largest number:"))
# arr_copy=arr.copy()
# for i in range(n-1):
#     max_value=max(arr_copy)
#     arr_copy.remove(max_value)
# nth_largest=max(arr_copy)
# print(nth_largest)

# def fact(n):
#     if n<=0:
#         return 1
#     return n*fact(n-1)
# print(fact(4))



# a="listen"
# print(sorted(a))
# b="silent"
# if sorted(a)==sorted(b):
#     print("anagram")
# else:
#     print("not")

# import re
# p=r'^((25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.){3}(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})$'
# # p=r'^((25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.){3}(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})$'
# i=input("enter the ipaddress")
# if re.match(p,i):
#     print("Valid")
# else:
#     print("invalid")
#
# p=r'^((25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.){3}(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})$'
# p=r'^((25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.){3}(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})$'
# arr=[10,50,40,20,60]
# n=int(input("enter the _ largest number"))
# arr_copy=arr.copy()
# for i in range(n-1):
#     max_val=max(arr_copy)
#     arr_copy.remove(max_val)
# nth_largest=max(arr_copy)
# print(nth_largest)

# import random
# import string
# def generate_string(length):
#     return ''.join(random.choices(string.ascii_lowercase,k=length))
# text=generate_string(5)
# print("system generated string",text)
# if text==text[::-1]:
#     print("palindrome")
# else:
#     print("not")

# l=[1,2,3,5]
# out=[]
# c=0
# for i in range(0,len(l)+1):
#     out+=[l[0]+c]
#     c+=1
# print(out)
#
# def anagram(str1,str2):
#     if len(str1)!=len(str2):
#         return False
#     d={}


#     for i in str1:
#         d[i]=d.get(i,0)+1
#     print(d)
#     for i in str2:
#         if i not in d or d[i]==0:
#             return False
#         d[i] -= 1
#     return True
# print(anagram("listen", "silent"))

# def sam(str1,str2):
#     if len(str1)!=len(str2):
#         return False
#     d={}
#     for i in str1:
#         d[i]=d.get(i,0)+1
#     print(d)
#     for i in str2:
#         if i not in d or d[i]==0:
#             return False
#         d[i]-=1
#     return True
# print(sam("listen", "silent"))

# import re
# p=r'[6-9][0-9]{9}'
# i=input('enter the string')
# if re.fullmatch(p,i):
#     print("valid")
# else:
#     print("invalid")

# import re
# p=r'^((25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.){3}(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})$'
# # p=r'^((25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.){3}(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})$'
# # # p=r'^((25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.){3}(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})$'
# # p=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z]+\.[a-zA-Z]{2,}$'
# p=r'[a-zA-z0-9]+@[a-zA-z]{5}\.[a-zA-z]{3}'
# i=input("enter the ipaddress")
# if re.match(p,i):
#     print("Valid")
# else:
#     print("invalid")

# p=nivedithanivi992@gmail.com
# p=r'[a-zA-z0-9]+@[a-zA-z]\.[a-zA-z]{3}'

# import random
# def generate_number(length):
#     first_di=str(random.randint(1,9))
#     remain_di=''.join(str(random.randint(0,9))for i in range(length-1))
#     return int(first_di+remain_di)
# num=generate_number(5)
# print("system generated number",num)
# if str(num)==str(num)[::-1]:
#     print("palindrome")
# else:
#     print("not")


# p=r'^((25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.){3}(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})$'

# def anagram(str1,str2):
#     if len(str1)!=len(str2):
#         return False
#     d={}
#     for i in str1:
#         d[i]=d.get(i,0)+1
#     print(d)
#     for i in str2:
#         if i not in d or d[i]==0:
#             return False
#         d[i]-=1
#     return True
# print(anagram('listen','silent'))

# def check_pal(s, low=0, high=0):
#     while low < high:
#         if s[low] != s[high]:
#             return False
#         low += 1
#         high -= 1
#     return True
# print(check_pal("babad)"))

# from collections import Counter
# def majority_element(l):
#     count = Counter(l)  #{3:2,2:3}
#     n = len(l) // 2  #5//2
#     for num, freq in count.items():
#         if freq > n:
#             return num
# print(majority_element([3, 2, 3,2,2]))

# def fibonacci(n):
#     a=0
#     b=1
#     if n<0:
#         print("invalid")
#     elif n==0:
#         return 0
#     else:
#         print(a, end=' ')
#         for i in range(1,n+1):
#             c=a+b
#             a=b
#             b=c
#             print(a,end=' ')
# fibonacci(10)

# def fibonacci():
#     a,b=0,1
#     while b<=20000:
#         a,b=b,a+b
#     while True:
#         print(b)
#         a,b=b,a+b
# fibonacci()

# def fibonacci_after_20000(n):
#     a, b = 0, 1
#     while b <= 20000:
#         a, b = b, a + b  # keep generating until we pass 20000
#     c=0
#     while c<n:
#         print(b)
#         a, b = b, a + b   # print next Fibonacci numbers after 20000
#         c+=1
# fibonacci_after_20000(10)

# def arm(n):
#     res=0
#     digit=len(str(n))
#     for i in str(n):
#         res+=int(i)**digit
#     return res==n
# def find(a,b):
#     for i in range(a,b+1):
#         if arm(i)==True:
#             print(i)
# find(1,1000)

# def fac(n):
#     res=1
#     for i in range(1,n+1):
#         res=res*i
#     return res
# # print(fac(4))
# def strong(n):
#     s=0
#     for i in str(n):
#         s+=fac(int(i))
#     return s==n
# def find(a,b):
#     for i in range(a,b+1):
#         if strong(i)==True:
#             print(i)
# find(1,10000)

# def per(n):
#     s=0
#     for i in range(1,n):
#         if n%i==0:
#             s+=i
#     return s==n
# print(per(6))
# def find(a,b):
#     for i in range(a,b+1):
#         if per(i)==True:
#             print(i)
# find(1,100)

# def fact(n):
#     if n<=0:
#         return 1
#     return n*fact(n-1)
# print(fact(5))

# import random
# import string
# def generate_string(length):
#     return ''.join(random.choices(string.ascii_lowercase,k=length))
# text=generate_string(5)
# print("system generated string",text)
# if text==text[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")

# import random
# def generate_num(length):
#     first_dig=str(random.randint(1,9))
#     remain_dig=''.join(str(random.randint(0,9))for i in range(length-1))
#     return int(first_dig+remain_dig)
# num=generate_num(5)
# print("System generated numbers",num)
# if str(num)==str(num)[::-1]:
#     print("palindrome")
# else:
#     print("not")

# arr=[30,20,60,40,10]
# n=int(input("enter the _ largest number"))
# arr_copy=arr.copy()
# for i in range(n-1):
#     max_value=max(arr_copy)
#     arr_copy.remove(max_value)
# nth_largest=max(arr_copy)
# print(nth_largest)

# def anagram(str1,str2):
#     if len(str1)!=len(str2):
#         return False
#     d={}
#     for i in str1:
#         d[i]=d.get(i,0)+1
#     print(d)
#     for i in str2:
#         if i not in d or d[i]==0:
#             return False
#         d[i]-=1
#     return True
# print(anagram('listen','silent'))

# def fibonacci(n):
#     a=0
#     b=1
#     if n<0:
#         return "invalid"
#     elif n==0:
#         return "0"
#     else:
#         print(a)
#         for i in range(1,n):
#             c=a+b
#             a=b
#             b=c
#             print(a)
# fibonacci(10)

# def fibonacci(n):
#     a=0
#     b=1
#     while b<=20000:
#         a,b=b,a+b
#     c=0
#     while c<n:
#         print(b)
#         a,b=b,a+b
#         c+=1
# fibonacci(10)

# abcabcbb
# s="abcabcbb"
# out=''
# for i in s:
#     if i not in s:
#         if

# import random
# def generate_prime(num):
#     return ''.join(random.randint()for i in range(2,num))
# num=generate_prime()
# print("system generated number",num)


# import random
# def generate_prime(num):
#     if num<2:
#         return False
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     return True
# def sam(start=2,end=50):
#     while True:
#         n=random.randint(start,end)
#         if generate_prime(n):
#             return n
# print(sam())

# s="abcabcbb"
# out=''
# for i in s:
#     if i not in out:
#         out+=i
# print(len(out))

# Sort a Dictionary by Value
# d={'hi':10,'hello':60,'how':40,'are':20,'you':30}
# out={}
# for i in range(0,len(d)):
#     if d[i]<d[i+1]:
#         out[i]=d[i]
# print(out)

# Input: "hello world" → Output: "world hello"
# s="hello world"
# l=s.split()
# rev=''
# out=[]
# for i in l[1]:
#     rev=i+rev
# out+=[rev]+[l[0]]
# print(' '.join(out))

# s="hello world"
# l=s.split()
# rev=''
# for i in l:
#     rev=i+' '+rev
# print(rev)

# def balanced(expression):
#     l=[]
#     d={')':'(','}':'{',']':'['}
#     for i in expression:
#         if i in '({[':
#             l.append(i)
#         elif i in ']})':
#             if

# n=1214
# res=0
# while n>0:
#     ld=n%10
#     res=res*10+ld
#     n//=10
# print(res)
# if res==n:
#     print("palindrome")
# else:
#     print('not')

# var="Hello, Neha!\nWelcome to Python revision."
# with open('file111.txt','w') as var:
#     var.write("Hello, Neha!\nWelcome to Python revision.")

# with open('file111.txt','r') as v:
#     res=v.readlines()
#     print(len(res))
#     print(res)
#     out=''.join(res)
#     # print(out)
#     # l=out.split()
#     # print(l)
#     # print(len(l))
#     c=0
#     for i in out:
#         print(i)
#         c+=1
#     print(c)



