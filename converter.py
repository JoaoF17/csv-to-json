import csv
import json

#data = json.loads("input.csv")
# open csv file 
with open("input.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # skip header
    next(csv_reader)

    # loop through rows in csv file and create dict for each row
    for row in csv_reader:
        data_dict = {
            'name': row[0],
            'image': row[1],
            'attributes': json.loads(row[2])
        }

        print(data_dict)

        # write each dictionary from csv rows as separate json files
        with open('{}.json'.format(data_dict["name"])[10:], 'w') as json_outfile:
            json.dump(data_dict, json_outfile)


