import csv

modelList = ["Porsche","BMW","Lexus","Audi"]
priceList = [60300,438230,39280,31450,]


def createDict(a, b):
    dict = {}
    for i in range(len(a)):
        dict[a[i]] = b[i]
    return dict


def createCSV(path, dict):
    writer = csv.writer(open(path, 'w', newline=''))
    for i in range(len(dict)):
        keys = list(dict.keys())
        values=list(dict.values())
        writer.writerow([keys[i], values[i]])



print(createDict(modelList, priceList))

createCSV('new.csv', createDict(modelList, priceList))
with open('new.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)