import csv

# Sample list of data
data = ['a', 's', 'd']

# Specify the file name for the CSV file
filename = 'data.csv'

# Column names
columns = ['Column1']

# Open the CSV file in write mode
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)

    # Write the column names as the first row
    csvwriter.writerow(columns)

    # Write each item in the list as a separate row
    for item in data:
        csvwriter.writerow([item])

print(f"CSV file '{filename}' has been created successfully!")
