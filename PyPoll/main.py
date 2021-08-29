import csv
import os

total_votes = 0

#specifies directory for csv file
poll_data = os.path.join("Resources", "election_data.csv")

pol_dict= {}
#specifies directory for csv file
with open(poll_data, 'r', encoding= 'utf-8') as csvfile:

    #creates reader variable
    csvReader = csv.reader(csvfile, delimiter = ',')
    #ingores header
    header = next(csvReader)

    #iterates through csv file
    for row in csvReader:
        #counts every row
        total_votes+= 1
        #Builds dictionary. Adds key name if unique and sets value to 1.
        #If key value is contained in dictionary, key value is incremented
        if row[2] not in pol_dict:
            pol_dict[row[2]] = 1
        else:
            pol_dict[row[2]] += 1

    
#gets key of the max value in the dictionary
winner = max(pol_dict, key=pol_dict.get) if pol_dict else None

#specifies directory for output file
txt_file = os.path.join("analysis", "poll_data.txt")

#Prints values and gets the percentage of votes in one go
print("Election Results\n-------------------------\nTotal Votes: " + str(total_votes) + "\n-------------------------")
for k,v in pol_dict.items():
    print(k + ' ' + str(round((int(v)/total_votes * 100), 3)) + '% (' + str(v) + ') \n')
print('-------------------------\nWinner: '  + winner +'\n-------------------------')   

#writes values and gets the percentage of votes to a csv file
with open(txt_file, 'w', encoding= 'utf-8') as txtfile:
    txtfile.write("Election Results\n-------------------------\nTotal Votes: " + str(total_votes) + "\n-------------------------\n")
    for k,v in pol_dict.items():
        txtfile.write(k + ' ' + str(round((int(v)/total_votes * 100), 3)) + '% (' + str(v) + ') \n')
    txtfile.write('-------------------------\nWinner: '  + winner +'\n-------------------------')   

            
        
    
#pol_dict= {'Kahn': khan_vote, 'Correy': correy_vote, 'Li' :li_vote, "O'Tooley" : o_tooley_vote}

#sort_pol = sorted(pol_dict.items(), key=lambda x: x[1], reverse=True)

