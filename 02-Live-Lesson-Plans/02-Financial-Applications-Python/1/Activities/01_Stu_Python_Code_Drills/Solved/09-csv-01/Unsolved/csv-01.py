# Import the necessary libraries for reading csv files
from pathlib import Path
import csv

# Set the path for the csv file
file_path = Path("../Resources/pokemon.csv")

# Create new lists to store data for heaviest and tallest Pokemon
heaviest = []
tallest = []

# Open the csv
with open(file_path, "r") as csv_content:

    csv_reader = csv.reader(csv_content, delimiter=",")
    header = next(csv_reader)
    print(header)
    counter = 0
    # Iterate through the data and search for the number the user inputted. Remember to skip the header of the CSV.
    for row in csv_reader:
        counter +=1
        # if counter>1:



        # Print the name of the Pokemon(identifier) and Pokedex number(species id) at that number. For example, "Pokemon No. 25 - Pikachu".
        # print("identifier", row[1])

        # Iterate through the data and search for Pokemon whose weight is greater than 3000. Append only the Pokemon's name and weight to the 'heaviest' list.
        if int(row[4]) > 3000:
            heaviest.append(row[1])

        # Iterate through the data and search for Pokemon whose height is greater than 50. Append only the Pokemon's name and height to the 'tallest' list.
        if int(row[3]) > 50:
            tallest.append(row[1])


# Print the list of heaviest and tallest pokemon
print("heaviest", heaviest)
print("tallest", tallest)