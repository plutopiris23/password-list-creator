#password list creator for brute forcing v.1.0 
from termcolor import colored

name = "Password list Creator for Bruteforcing"
lengte = len(name) + 6
dotname = "-" * lengte
print (" ")
print(colored(dotname , 'red'))
print(colored(".:: ", 'blue') + colored(name , 'green') + colored(" ::.", 'blue'))
print(colored(dotname , 'red'))




print(colored('This tool is for educational purposes only.\n', 'red'), colored('created by "https://t.me/Maneth_M".\n', 'blue'), colored('#if you are featuring this tool in a video or somewhere please give credits# \n \n ', 'yellow'))




## Variable lists

lst1 = []
lst2 = ['fist name', 'second name', 'last name', 'nick name', 'birth year', 'birth month', 'birth date', 'school or workplace']
lst3 = []

## First Input

print(colored('enter everything you know about the victim. all in simple \n \n \n \n ', 'blue'))

for i in lst2:
   x=input(str(colored('Enter --> ' + i + '\n :- ' , 'green')))
   if x != '':
     lst1.append(str(x))
   else:
     continue
     
## Second Input 



print(colored('''you can add any possible word or number or symbol. such as favorite song, favorite colour, family members' names... Depends on your information gathering skills. don't keep spaces between inputs.''', 'red'))
w = input(str(colored('Enter any more word,number or symbol possibilities if you have. seperated with a comma. (ex:- john,newyork,@,23,#) \n :- ', 'green')))


## Adding Second input to the list
if w != '':
 lst3 = w.split(",")
 lst1 = lst1+lst3

## Making everything Lowercase 

for i in range(len(lst1)):
  lst1[i]=lst1[i].lower()
lst3.clear()

## Combining words togeather

for i in lst1:
  l = 0
  while l < len(lst1):
    x = i + lst1[l]
    lst3.append(str(x))
    l = l+1

lst3 = lst3+lst1
lst1.clear()

## Adding all upper lowert mixed combinations

d = input('do you wanna try every posibility with lower case and upper case (not recommended. time consuming)? yes(y) or no(n) \n :- ''')

if d == 'yes' or d == 'y':

  for i in lst3:
      import itertools
      x=map(''.join, itertools.product(*((c.upper(), c.lower()) for c in i)))
      lst1 = lst1 + list(x)   
##  x = list(x)

elif d == 'no' or d == 'n':
  s = input(colored('Do you wanna make the first letter upper case (lower case words will also remain)? yes(y) or no(n) \n :- ', 'blue'))
  
  if s == 'yes' or s == 'y':
    x = []
    for i in lst3:
      x.append(i.capitalize())
    
  lst1 = lst3 + x
      
 
lst3.clear()





##Replacing Same looking letters and Numbers 

z = input(colored('Do you wanna replace letters with same looking numbers and symbols? (ex:- A --> 4, S --> 5) yes(y) or no(n) \n :- ', 'blue'))

if z == 'yes' or z == 'y':
 n = 0
 m = len(lst1)
 for i in (lst1):
  n=n+1
  lst1.append(i.replace('a', '4'))
  if n==m:
    break
    
 n = 0
 m = len(lst1)
 for i in (lst1):
  n=n+1
  lst1.append(i.replace('s', '5'))
  if n==m:
    break  
     
 n = 0
 m = len(lst1)
 for i in (lst1):
  n=n+1
  lst1.append(i.replace('e', '3'))
  if n==m:
    break    
 
 n = 0
 m = len(lst1)
 for i in (lst1):
  n=n+1
  lst1.append(i.replace('i', '1'))
  if n==m:
    break    


elif z == 'no' or z == 'n':
 print('')
else:
 print('invalid input')

## Removing Duplicates

lst1 = list(set(lst1))

k = input(colored('''what's the minimum length of the password? \n :- ''',  'yellow'))

for i in lst1:
  if len(i) < int(k):
    lst1.remove(i)   
    
h = input(colored('''what's the maximum length of the password? \n :- ''', 'yellow'))

for i in lst1:
  if len(i) > int(h):
    lst1.remove(i) 

MyFile=open('password.txt','w')

for element in lst1:
     MyFile.write(element)
     MyFile.write('\n')
MyFile.close()


print(str(len(lst1)) + 'passwords have been created in passwords.txt')



print("This code sucks")