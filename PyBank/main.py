import csv
import os

finance = "Financial Anaylsis"
months = 0
total = 0
change = []
p_l = []
monthData = []


#specifies directory for csv file
bank_data = os.path.join("Resources", "budget_data.csv")

#Opens CSV file with reader permissions
with open(bank_data, 'r', encoding= 'utf-8') as csvfile:
    
    #creates reader variable
    csvReader = csv.reader(csvfile, delimiter = ',')
    #ingores header
    header = next(csvReader)
   
   #iterates through reader variable
    for row in csvReader:
        months+= 1 #counts rows or months
        total+= int(row[1]) #adds each cell in profits/losses
        p_l.append(int(row[1])) #appends integer value of each cell profits/losses to a list
        monthData.append(row[0]) #Appends string value of first coulmn. Could make this a dictionary and combine 
    
    #gets length of list to use in for loop
    length = len(p_l)
    #loops through entire list of integers
    for i in range(length-1):
        #adds the value of the next value - the previous value (all integers) to a list
        change.append(p_l[i+1]-p_l[i])

    #gets max value in list and coressponding index
    maxi = max(change)
    max_month_index = change.index(maxi)
    
    #gets min value in list and corresponding index
    mini = min(change)
    min_month_index = change.index(mini)

    #calculates average
    average = round(sum(change)/len(change),3)

#specifies directory for output   
txt_file = os.path.join("analysis", "bank_data.txt")

#creates txt file with writer permisions and adds data
with open(txt_file, 'w', encoding= 'utf-8') as txtfile:
    txtfile.write(finance + '\n----------------------------\n')
    txtfile.write('Total Months: ' + str(months) + '\n' + 'Total: ' + str(total) + '\nAverage Change: ' + str(average) + 
                    '\nGreatest Increase in Profits: ' + monthData[max_month_index + 1] + ' $' + str(maxi) + 
                    '\nGreatest Decrease in Profits: ' + monthData[min_month_index + 1] + ' $' + str(mini))

#prints values to console
print(finance + '\n----------------------------\n'
        'Total Months: ' + str(months) + '\n' + 'Total: ' + str(total) + '\nAverage Change: ' + str(average) + 
            '\nGreatest Increase in Profits: ' + monthData[max_month_index + 1] + ' $' + str(maxi) + 
                '\nGreatest Decrease in Profits: ' + monthData[min_month_index + 1] + ' $' + str(mini))
 
