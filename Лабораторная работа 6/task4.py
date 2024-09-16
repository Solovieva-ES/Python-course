import json

INPUT_FILE = "input.csv"

def csv_to_json(csvFile):

    jsonArray = []
    csvReader = []

    with open(csvFile, encoding='utf-8') as csvf:

        result = csvf.readlines()
        headers = result[0].rstrip().split(sep=',')

        for row in result[1:]:
            csvReader.append(row.rstrip().split(sep=','))

        for row in csvReader:
            j={head: i for head, i in zip(headers, row) }
            jsonArray.append(j)

    return jsonArray

print(json.dumps(csv_to_json(INPUT_FILE), indent=4))
