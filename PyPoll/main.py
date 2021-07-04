
import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

# Establish our variables needed in this analysis 

total_votes = 0 
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0
candidate = set()

# Open the CSV we are working with 

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
   
    for row in csvreader:

# To get the total number of vote cast
        total_votes += 1

# Listing candidate who receive vote, where candidate is defined as a set so it can only appear once 
        candidate.add(row[2])

#When the name of a candidate is found, count the times it appears and put it in a list, this calculate toal number of vote each candidate won 
        if (row[2] == "Khan"):
            khan_votes += 1
        elif (row[2] == "Correy"):
            correy_votes += 1
        elif (row[2] == "Li"):
            li_votes += 1
        else:
            otooley_votes += 1

# store the vote count in the list belwo, so when we need to find who has highest numebr of vote it can be done

votes = [khan_votes, correy_votes,li_votes,otooley_votes]

# winner of the election based on popular vote, that is in our list "votes" above, whoever had the largest vote number is the election winner 

election_winner = max(votes)
winner_name = ""

if election_winner == khan_votes:  
    winner_name = "Khan"

elif election_winner == correy_votes:
    winner_name = "Correy"

elif election_winner == li_votes:   
    winner_name = "Li"

elif election_winner == otooley_votes:
    winner_name = "O'Tooley"

# percentage of votes each candidate won // initially did not float and returned 0, i have to float it for some reason to make it work 
khan_percent = round(float(khan_votes)/float(total_votes)*100)
correy_percent = round(float(correy_votes)/float(total_votes)*100)
li_percent = round(float(li_votes)/float(total_votes)*100)
otooley_percent = round(float(otooley_votes)/float(total_votes)*100)

# Print results to terminal

print("Total Votes: " + str(total_votes))
print("Khan: " + str(khan_percent) + "%" + " " + str(khan_votes))
print("Correy: " + str(correy_percent) + "%"+ " " + str(correy_votes))
print("Li: " + str(li_percent) + "%" + " " + str(li_votes))
print("O'Tooley: " + str(otooley_percent) + "%" + " " + str(otooley_votes))
print("The winning candidate is: " + winner_name)

# create text file with answers

with open('Pypoll_answers.txt', 'w') as f:
    f.write("Total Votes: " + str(total_votes) + "\n")
    f.write("Khan: " + str(khan_percent) + "%" + " " + str(khan_votes) + "\n")
    f.write("Correy: " + str(correy_percent) + "%"+ " " + str(correy_votes) + "\n")
    f.write("Li: " + str(li_percent) + "%" + " " + str(li_votes) + "\n")
    f.write("O'Tooley: " + str(otooley_percent) + "%" + " " + str(otooley_votes) + "\n")

    f.close() 
