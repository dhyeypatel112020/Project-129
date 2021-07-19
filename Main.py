import csv 


data=[]
with open("dataset_2.csv","r") as f:
    csvreader=csv.reader(f)
    for i in csvreader:
        data.append(i)


header=data[0]

planetdata=data[1:]

for datapoint in planetdata:
    datapoint[2]=datapoint[2].lower()

planetdata.sort(key=lambda planetdata:planetdata[2])

with open("dataset_2_sorted.csv","a+") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(header)
    csvwriter.writerows(planetdata)