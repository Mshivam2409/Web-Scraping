import pandas as pd
import re
pcsv = str(input("Enter the CSV file loccation:"))
pjson = str(input("Enter the JSON file loccation:"))
data = pd.read_csv(pcsv,index_col=0) 
data2 = pd.read_json(pjson)
def check_splcharacter(test):
    string_check= re.compile('[@_!#$%^&*()<>?/\|}{~:]-+=;,~')
    if(string_check.search(test) == None):
        return True 
    else: 
        return False
def is_lower_or_digit(test):
    flag = 0
    for ch in test:
        if ch.isdigit():
            return False
        if ch.isupper():
            flag = 1 
    if flag == 1:
        return True
    return False
def is_two_word(test):
    for ch in test:
        if ch==' ':
            return True
    return False   
print("The invalid names in CSV are : ")
for name in data.index:
    if(not(check_splcharacter(name) and is_lower_or_digit(name) and is_two_word(name))):
        print(name)
        data = data.drop(name,axis = 0)
data = data.reset_index()
print("------------------------------------")
print("The matched entries are:",end = "\n\n")
valid_names = []
i1 = []
i2 = []
index1 = 0
index2 = 0
for name in data['Person Name']:
    index2 = 0
    for nam in data2["n"]:
        if nam.split()==name.split():
            valid_names.append(name)
            i1.append(index1)
            i2.append(index2)
            break
        index2 = index2 + 1 
    index1 = index1 + 1   
for i in range(0,len(i1)):
    print("Person Name :",end = " ")
    print(data.loc[i1[i],"Person Name"])
    print("Project :",end = " ")
    print(data.loc[i1[i],"Project"])
    print("Organization :",end = " ")
    print(data.loc[i1[i],"Organization"])
    print("Department :",end = " ")
    print(data2.loc[i2[i],"d"])
    print("Roll No. :",end = " ")
    print(data2.loc[i2[i],"i"])
    print('--------')                        