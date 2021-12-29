# use AWS to configure
# Done


import boto3
from boto3.dynamodb.conditions import Key
import json

# WORKS
def create_json(read_file, table_name):
    client = boto3.client("dynamodb")

    listw = []
    with open(read_file, "r") as text:

        for index, line in enumerate(text):
            if index % 25 == 0 and index != 0:
                client.batch_write_item(RequestItems={table_name: listw})
                listw = []

            data = {}
            line_split = line.strip().split(":")
            print(line_split)
            if line_split[0]:
                data["email"] = {"S": line_split[0]}
                data["password"] = {"S": line_split[1]}
                listw.append({"PutRequest": {"Item": data}})


create_json(read_file="file.txt", table_name="TableName")
