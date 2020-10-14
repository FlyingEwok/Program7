#initiate variables
fname = "tragedy_of_darth_plagueis_the_wise.txt"
counter = 0

#Count the amount of 'the' in the text file
with open(fname) as openfile:
    for line in openfile:
        for part in line.split():
            if "the" in part:
                counter += 1

#Print a statemnt telling you how many 'the' are in text file
print("There is ", counter, " amount of 'the' in The Tragedy of Darth Plagueis the Wise.")


