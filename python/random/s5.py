import re

input_file = open("blain.txt", "r")
output_file = open("bla.txt", "w")

for line in input_file:
    timestamp = line[:12]
    scrambled_line = line[12:].replace("IR1", "")
    curated_line = re.sub("[^0-9.,-]", "", scrambled_line)
    new_line = f"{timestamp},{curated_line}\n"
    output_file.write(new_line)

input_file.close()
output_file.close()
