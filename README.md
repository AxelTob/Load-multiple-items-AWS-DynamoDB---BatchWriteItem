# Load-multiple-items-AWS-DynamoDB---BatchWriteItem
BatchWriteItem allows you to load multiple items into DynamoDB. But has a request limit of 25 items. I used this small script to read from textfile -> jsonformat -> AWS Request. Sending batches of 25 items till the list is completed.

Need to install AWS CLI and configure.
First param for this script (change it to your need), is the input textfile and second existing table.
