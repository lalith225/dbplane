orginalList, sortedList = [], []
limit = int(input("Enter the limit of the list\n"))

for i in range(limit):
    tempvalue =  int(input("Enter the value to add in list\n"))
    orginalList.insert(i,tempvalue)

for i in range(len(orginalList)):
    sortedList.insert(i,orginalList[i])

for i in range(limit - 1):
    for j in range(limit):
        if sortedList[i] > sortedList[i+1]:
            temp = sortedList[i]
            sortedList[i] = sortedList[i+1]
            sortedList[i+1] = temp


print("\nOrginal List is")
for i in range(limit):
    print(orginalList[i])

print("\nSorted List is")
for i in range(limit):
    print(sortedList[i])