#Expected output:[1, 'h', 3, 'f', 5, 'd', 7, 'b']
#Given Input:
# a=[1,2,3,4,5,6,7,8,9,10]
# b='abcdefghi'
# c = a[0::2]
# d=b[::-1]
# e=d[1::2]  #'hfdb'
# def List(c, e):
#     return [sub[item] for item in range(len(e)) for sub in [c, e]]
# print(List(c, e))

#1**0=1
#0**1=0=0**+1
# x = [i**+1 for i in range(3)]; print(x);

#a=[i+j for i in "abc" for j in "def"]
#print(a)
#['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

# print([[i+j for i in "abc"] for j in "def"])
# [['ad', 'bd', 'cd'], ['ae', 'be', 'ce'], ['af', 'bf', 'cf']]

# my_string='hi all welcome'
# k = [i for i in my_string if i not in "aeiou"]
# print(k)

# my_string = "hello world"
# #create a tuple, in that convert all the elements into upper
# #and length of that perticular element(which is always 1)
# k = [(i.upper(), len(i)) for i in my_string]
# print(k)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = ['hello' for x in fruits]
# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x if x != "banana" else "orange" for x in fruits]
# print(newlist)

# letters = list(map(lambda x: x, 'human'))
# print(letters)

n= [ x for x in range(20) if x % 2 == 0]
print(n)