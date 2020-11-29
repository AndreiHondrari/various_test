

import csv
import os

IN_DIR = "in"

for filename in os.listdir(IN_DIR):
    file_path = os.path.join(IN_DIR, filename)

    with open(file_path, 'r') as pf:
        csv_reader = csv.reader(pf)

        for r in csv_reader:
            print(r[9])
