import os 
import csv

filepath = os.path.join('Resources', 'budget_data.csv')


with open(filepath, 'r') as file:

    
    dframe = csv.reader(file, delimiter = ',')
    dframe2 = next(dframe)

    month = len(list(dframe))
         
month = str(month) 
print(f"Total Months: {month}")

    
with open(filepath, 'r') as file:


    
    dframe = csv.reader(file, delimiter = ',')
    dframe2 = next(dframe)

    total=0
    tlist = []
    
    for i in dframe:
        amount = int(i[1])
        total = total + amount
        tlist.append(amount)
        total = sum(tlist)
        total2 = '${}'.format(total)

total = str(total2)
print(f"Total: {total}")


with open(filepath, 'r') as file:


    
    dframe = csv.reader(file, delimiter = ',')
    dframe2 = next(dframe)

    change=0
    clist = []
    
    for i in dframe:
        value = int(i[1])
        clist.append(value)
        
    clist2 = ([x - clist[j - 1] for j, x in enumerate(clist)][1:])
    divi = len(clist2)
    avg = sum(clist2)/divi
    avg2 = "{:.2f}".format(avg)

avg = str(avg2)
print(f"Average Change: ${avg}")


with open(filepath, 'r') as file:

    dframe = csv.reader(file, delimiter = ',')
    dframe2 = next(dframe)

    nlist = []
    dlist= []
    
    for i in dframe:
        record = int(i[1])
        drecord = i
        
        nlist.append(record)
        dlist.append(drecord)
        mini = min(nlist)
        maxim = max(nlist)

        index = nlist.index(mini)
        index2 = nlist.index(maxim)

        minidate = dlist[index]
        maximdate = dlist[index2]
      
minidate = str(minidate)
maximdate = str(maximdate)

print(f"Greatest Decrease in Profits: {minidate}")
print(f"Greatest Increase in Profits: {maximdate}")


file = open("results.txt", "a")
file.writelines("Financial Analysis" + "\n" + "\n" + "Total Months: " + month + "\n" + "Total: " + total + "\n" + "Average Change: $" + avg + "\n" + "Greatest Increase in Profits: " + maximdate + "\n" + "Greatest Decrease in Profits: " + minidate) 
file.close()





        