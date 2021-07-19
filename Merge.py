import csv 


dataset1=[]
dataset2=[]

with open("dataset_1.csv","r") as f:
    csvreader=csv.reader(f)
    for i in csvreader:
        dataset1.append(i)

with open("dataset_2_sorted.csv","r") as f:
    csvreader=csv.reader(f)
    for i in csvreader:
        dataset2.append(i)

header2=dataset2[0]
header1=dataset1[0]

planetdata2=dataset2[1:]
planetdata1=dataset1[1:]

headers=header1+header2

planetdata=[]

for index,datarow in enumerate(planetdata1):
    planetdata.append(planetdata1[index]+planetdata2[index])



with open("combined.csv","a+") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetdata)