import csv
import boto3.dynamodb


def runner():

    with open('/users/jonathan/desktop/test.csv', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print('-'.join(row))

runner()