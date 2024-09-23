#palindronme
list1=[1,1,1]

copylist1=list1.copy()
copylist1.reverse()

if(copylist1==list1):
    print("palindrome list")
else:
    print("not palindrome")