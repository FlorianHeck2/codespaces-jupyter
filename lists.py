import re
Liste = [0,2,5,1,7,9,3 ]
Liste.sort()
min = Liste[0]
max = Liste[len(Liste)-1]
Liste=set(Liste)
Liste=list(Liste)

dict = {
    "brand":"Ford"

}
len(dict)
Brandname=dict["brand"]

dictionaries = []
diction=    {"date" : '2024-01-15', "amount" : 100, "income" : True }
diction2=    {"date" : '2024-01-15', "amount" : 50, "income" : False }
diction3=    {"date" : '2024-01-15', "amount" : 12, "income" : False }
diction4=    {"date" : '2024-01-14', "amount" : 100, "income" : True }

dictionaries.append(diction)
dictionaries.append(diction2)
dictionaries.append(diction3)
dictionaries.append(diction4)
def totalincome():
    earning =0
    for a in dictionaries():
        if dictionaries[a].get("income")==True:
            earning = earning + dictionaries[a].get("amount")
    return earning
def totalexpense():
    a=0
    expense =0
    for a in dictionaries():
        if dictionaries[a].get("income")==False:
            expense = expense + dictionaries[a].get("amount")
    return expense

def totaltransactions(datum):
    c=0
    for x in dictionaries():
        if x.get("date") == datum:
            c +=1
def find_all(category, value):
    retlist = []
    a=0
    for x in dictionaries:
        if value == dictionaries[a].get("date"):
            retlist.append(dictionaries[a])
        a +=1
    return retlist

def is_valid_date_format(date_string):
    stringpattern = r"\d{4}-\d{2}-\d{2}"
    pattern=re.compile( stringpattern)
    
    return bool(pattern.match(date_string))

#r'\d{4}\'
if is_valid_date_format("2024-15-02"):
    print("Valid format")
else:
    print("Use the format yyyy-mm-dd")
    
