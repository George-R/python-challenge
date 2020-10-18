import os 
import csv

filepath = os.path.join('Resources', 'election_data.csv')


with open(filepath, 'r') as file:

    
    dframe = csv.reader(file, delimiter = ',')
    dframe2 = next(dframe)

    totalvotes = len(list(dframe))
         

with open(filepath, 'r') as file:

    
    dframe = csv.reader(file, delimiter = ',')
    dframe2 = next(dframe)

    clist = []

    # traverse for all elements 
    for i in dframe: 
        name = i[2]

        if name not in clist: 
            clist.append(name) 
        

cand1 = clist[0]
cand2 = clist[1]
cand3 = clist[2]
cand4 = clist[3]


with open(filepath, 'r') as file:

    
    dframe = csv.reader(file, delimiter = ',')
    dframe2 = next(dframe)

    vote = 0
    candlist1 = []
    candlist2 = []
    candlist3 = []
    candlist4 = []

    # traverse for all elements 
    for i in dframe: 
        name = i[2]

        if name == cand1:
            candlist1.append(name)

        elif name == cand2:
            candlist2.append(name)

        elif name == cand3:
            candlist3.append(name)

        elif name == cand4:
            candlist4.append(name)

vote1 = len(list(candlist1))
vote2 = len(list(candlist2))
vote3 = len(list(candlist3))
vote4 = len(list(candlist4))

pvote1 = vote1/totalvotes * 100
pvote2 = vote2/totalvotes * 100
pvote3 = vote3/totalvotes * 100
pvote4 = vote4/totalvotes * 100

pvote11 = "{:.2f}".format(pvote1)
pvote22 = "{:.2f}".format(pvote2)
pvote33 = "{:.2f}".format(pvote3)
pvote44 = "{:.2f}".format(pvote4)

pvote1 = str(pvote11)
pvote2 = str(pvote22)
pvote3 = str(pvote33)
pvote4 = str(pvote44)

print(f"Total Votes: {totalvotes}")

print(f"{cand1}: {pvote1}% ({vote1})")
print(f"{cand2}: {pvote2}% ({vote2})")
print(f"{cand3}: {pvote3}% ({vote3})")
print(f"{cand4}: {pvote4}% ({vote4})")


if vote1 > vote2 and vote1 > vote3 and vote1 > vote4:
    print("Winner is " + cand1)
    winner = cand1

elif vote2 > vote1 and vote2 > vote3 and vote2 > vote4:
    print("Winner is " + cand2)
    winner = cand2

elif vote3 > vote1 and vote3 > vote1 and vote3 > vote4:
    print("Winner is " + cand3)
    winner = cand3

elif vote4 > vote1 and vote4 > vote3 and vote4 > vote2:
    print("Winner is " + cand4)
    winner = cand4

vote1 = str(vote1)
vote2 = str(vote2)
vote3 = str(vote3)
vote4 = str(vote4)
totalvotes = str(totalvotes)

file = open("results.txt", "a")
file.writelines("Election Results"+ "\n" + "\n" + "Total Votes: " + totalvotes + "\n" + "\n" + cand1 + ": " + pvote1 + "%" + " (" + vote1 + ")" + "\n" + cand2 + ": " + pvote2 + "%" + " (" + vote2 + ")" + "\n" + cand3 + ": " + pvote3 + "%" + " (" + vote3 + ")" + "\n" + cand4 + ": " + pvote4 + "%" + " (" + vote4 + ")" + "\n"+ "\n" + "Winner: " + winner) 
file.close()