

x = [
    "FTSE",
    "FT",
    "TS",
    "SE",
    "TSE"
    "FTSE"
]

names = []
for _ in range(5000):
    names += x

detected_positions = {}


for i in range(len(names)-1):
    current_name = names[i]

    if current_name in detected_positions:
        continue

    detected_positions[current_name] = i

    for j in range(i+1, len(names)):

        secondary_name = names[j]

        if secondary_name in detected_positions:
            continue

        detected_positions[secondary_name] = j

        print(f"{current_name}, {secondary_name}")



print("------ DONE -------")
