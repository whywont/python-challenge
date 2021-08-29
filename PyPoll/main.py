import csv
import os

total_votes = 0
khan_vote = 0
correy_vote = 0
li_vote = 0
o_tooley_vote = 0



#specifies directory for csv file
poll_data = os.path.join("Resources", "election_data.csv")


#specifies directory for csv file
with open(poll_data, 'r', encoding= 'utf-8') as csvfile:

    #creates reader variable
    csvReader = csv.reader(csvfile, delimiter = ',')
    #ingores header
    header = next(csvReader)

    for row in csvReader:
        total_votes+= 1
        if row[2] == "Khan":
            khan_vote+= 1
        elif row[2] == "Correy":
            correy_vote+= 1
        elif row[2] == "Li":
            li_vote+= 1
        else:
            o_tooley_vote+=1
    
pol_dict= {'Kahn': khan_vote, 'Correy': correy_vote, 'Li' :li_vote, "O'Tooley" : o_tooley_vote}

sort_pol = sorted(pol_dict.items(), key=lambda x: x[1], reverse=True)

lis_win = [x[0] for x in sort_pol]

txt_file = os.path.join("analysis", "poll_data.txt")

#print(lis_win[0])

print("Election Results\n-------------------------\nTotal Votes: " + str(total_votes) + "\n-------------------------")
for i in sort_pol:
    print(i[0], str(round((int(i[1])/total_votes * 100), 3)) + '%', '(' + str(i[1]) + ')')
print('-------------------------\n Winner: ' + str(lis_win[0]) +'\n-------------------------')
 

#creates txt file with writer permisions and adds data
with open(txt_file, 'w', encoding= 'utf-8') as txtfile:
    txtfile.write("Election Results\n-------------------------\nTotal Votes: " + str(total_votes) + "\n-------------------------\n")
    for i in sort_pol:
        txtfile.write(str(i[0]) + ' ' + str(round((int(i[1])/total_votes * 100), 3)) + '% (' + str(i[1]) + ') \n')
    txtfile.write('-------------------------\n Winner: ' + str(lis_win[0]) +'\n-------------------------')
