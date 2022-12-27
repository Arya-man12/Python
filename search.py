Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> lst=eval("input("enter list"))
	 
SyntaxError: invalid syntax
>>> lst=eval(input("enter list"))
enter list45,67,56,89,90
>>> length=len(lst)
>>> ele=int(input("enter element to be searched for:")
	56
	
SyntaxError: invalid syntax
>>> ele=int(input("enter element to be searched for:"))
enter element to be searched for:56
>>> for i in range(0,length):
	if ele=lst[i]:
		
SyntaxError: invalid syntax
>>> > for i in range(0,length):
	if ele==lst[i]:
		
SyntaxError: invalid syntax
>>>  for i in range(0,length):
	if ele==lst[i]:
		
SyntaxError: unexpected indent
>>> for i in range(0,length):
	if ele==lst[i]:
		print(ele,"found at index",i)
		break
	else:
		print(ele,"not found in the given list")

		
56 not found in the given list
56 not found in the given list
56 found at index 2
>>> for i in range(0,length):
	if ele==lst[i]:
		print(ele,"found at index:",i)
		break
	else:
		print 