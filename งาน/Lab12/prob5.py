import csv


def calculate_average(row):
    return sum(row) / len(row)

initial_data = [
    [2, 4, 6],
    [3, 7, 5],
    [8, 9, 7]
]

with open('numbers.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in initial_data:
        writer.writerow(row)

output_data = []
with open('numbers.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        swapped_row = [row[2], row[1], row[0], calculate_average([float(x) for x in row])]
        output_data.append(swapped_row)

with open('numbers2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in output_data:
        print(row)
        writer.writerow(row)