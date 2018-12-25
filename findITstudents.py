#! python3
import re, pyperclip

#TODO:create a range match  for 30270-38641

nameRegex=re.compile(r'''
([3][0-8][2-6]\d\d)+
''',re.VERBOSE) # match object starts with 302

names=pyperclip.paste()  #paste the copied content from the clipboard

extratednumber=nameRegex.findall(names) #findall the matching strings from the copied content

I = extratednumber.index("30269") #set the index value where string will match the number before the actual starting number

allnumbers=[] #create an empty list to store the required list

while I!=extratednumber.index("38641"): #run while loop till the last elements is found
    I+=1
    allnumbers.append(extratednumber[I]) #append all the found elements into empty list allnumbers

total=len(allnumbers) #find the total number of matches

print("Total students for IT exam are" +str(total)) #print the same

ITEXAMNUMBER='|'.join(allnumbers) #get all the results in one string in proper format.

print(ITEXAMNUMBER) #print the string.
