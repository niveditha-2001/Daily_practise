# a=open("deepthi.txt",'w+')
# for i in range(10):
#     a.write('line %d\r\n'%(i+1))
# a.close()

# f=open("deepthi.txt", "a+")
# for i in range(2):
#     f.write("appended %d\r\n" % (i+1))
# f.close()


# import calendar
# year = 2025
# for month in range(1, 13):
#     cal = calendar.monthcalendar(year, month)
#     first_monday = cal[0][calendar.MONDAY] or cal[1][calendar.MONDAY]
#     print(f"First Monday in {calendar.month_name[month]} {year} is on {month}/{first_monday}/{year}")


# import calendar
# #a=calendar.TextCalendar(calendar.SUNDAY)
# for i in range(1,12):
#     a=calendar.monthcalendar(2019,i)
#     week1=a[0]
#     week2=a[1]
#     if week1[calendar.FRIDAY] !=0:
#         temple=week1[calendar.FRIDAY]
#     else:
#         temple=week2[calendar.FRIDAY]
#
#     print(calendar.month_name[i],temple)


# f=open("deepthi.txt", "r")
# if f.mode=='r':
#     contents=f.read()
#     print(contents)

# to prevent the operating system from having too many open files
# from os import path
# print(path.exists("deepthi.txt"))
# print(path.isfile("deepthi.txt"))
# print(path.isdir("deepthi.txt"))

#pathlib

# import pathlib
# a=pathlib.Path("deepthi.txt")
# if a.exists():
#     print("file exists")
# else:
#     print("file not exist")


#Write line and read line
# file1 = open("myfile.txt", "w")
# L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
# file1.write("Hello \n")
# file1.writelines(L)
# file1.close()
# #
# file1 = open("myfile.txt", "r+")
# print("Output of Read function is ")
# print(file1.read())
# print()

# seek(n) takes the file handle to the nth
# bite from the beginning.

# file1 = open("myfile.txt", "r+")
# file1.seek(1)
# print("Output of Readline function is ")
# print(file1.readline())
#readline will read line by line
#readlines will read in the form of list
# print()

file1 = open("myfile.txt", "r+")
file1.seek(0)
# To show difference between read and readline
print("Output of Read(9) function is ")
print(file1.read(9))
#read(starts with 1 and reads till that position-1)
file1.seek(0)





