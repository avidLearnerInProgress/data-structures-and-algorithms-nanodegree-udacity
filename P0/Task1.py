"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
in_call_records = [number[0] for number in calls]
out_call_records = [number[1] for number in calls]
in_text_records = [number[0] for number in texts]
out_text_records = [number[1] for number in texts]

total_call_records = list(set(list(in_call_records + out_call_records + in_text_records + out_text_records)))
count = len(total_call_records)

print(f"There are {count} different telephone numbers in the records.")