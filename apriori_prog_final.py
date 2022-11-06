from cgi import print_form


listOfStringOfitems=[]
with open('dataset_in_text.txt') as doc_itemset:
    for itemset in doc_itemset:
        listOfStringOfitems.append(itemset.lower().strip())
        print(listOfStringOfitems)
def string2list(string1):
    return string1.split(',')

print('\nItemsets.................')
listOfListOfitems=[]
for itemset in listOfStringOfitems:
    listOfListOfitems.append(string2list(itemset))

for i in range(len(listOfListOfitems)):
    print('T',i+1,':',listOfListOfitems[i])
uniqueSetOfItems={}
uniqueSetOfItems=set().union(*listOfListOfitems)

#minimum support
minsup=int(input('Enter minimum support : '))

#dictionary to keep records of frequent itemsets
frequent_items={}
#printing C1
dict_c1={}
for item in uniqueSetOfItems:
    dict_c1[item]=0
    for listofitems in listOfListOfitems:
        if item in listofitems:
            dict_c1[item]+=1
print('\n\tC1')
for i in dict_c1:
    print(i,':',dict_c1[i])

#printing L1
newUniqueListOfItems=[]
print('\n\tL1')
for i in dict_c1:
    if dict_c1[i] >= minsup:
        print(i,':',dict_c1[i])
        frequent_items[i]=dict_c1[i]
        newUniqueListOfItems.append(i)

def strings2list(string1):
    return string1.split()
itemsAsList=[]
for item in newUniqueListOfItems:
    itemsAsList.append(strings2list(item))
#converting list of lists of strings as as list of lists of lists

def appendLists(item1,item2):
    return set(item1+item2)

#checking the subset
def isSubset(list1,list2):
    count=0
    for item1 in list1:
        for item2 in list2:
            if item1==item2:
                count+=1
    if count==len(list1):
        return True
    else:
        return False
#loop for generating further Ci's and Li's
k=2
while True:
    newList=[]
    for i in range(len(itemsAsList)):
        for j in range(i+1,len(itemsAsList)):
            newList.append(appendLists(itemsAsList[i],itemsAsList[j]))
    dict_ci={}
    for item in newList:
        dict_ci[tuple(item)]=0
        for itemset in listOfListOfitems:
            if isSubset(item,itemset):
                dict_ci[tuple(item)]+=1
    print('\n\tC',k)
    for i in dict_ci:
        if len(i)==k:
            print(i,':',dict_ci[i])
    list34=[]
    print('\n\tL',k)
    for i in dict_ci:
        if dict_ci[i]>=minsup and len(i)==k:
            print(i,':',dict_ci[i])
            frequent_items[i]=dict_ci[i]
            list34.append(list(i))
    if len(list34)==0:
        print('\n\tL',k,' is empty')
        break
    itemsAsList=list34
    k+=1
print('\n\tFrequent Items')
#picking out the frequent items with max support count
max_size=0
for i in frequent_items:
    if type(i)==str:
        max_size=1
    else:
        if len(i)>max_size:
            max_size=len(i)

#printing the frequent items with maximum support
for i in frequent_items:
    if len(i)==max_size:
        print(i,':',frequent_items[i])
