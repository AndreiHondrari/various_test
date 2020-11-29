at_set = {'AT1', 'AT2', 'AT3'}  #<--The records that will be read should contain 1 of these characters.


def location_token(r):
    if len(r) > 22:
        location_data = r[22]
        for token in mp:
            if token in location_data:
                return token
    return None


def filter_row(r):
    condition_1 = set(row).intersection(at_set) #<-- check if any index of any row contains a character mentioned in at_set
    condition_2 = r[9].isdigit() if len(r) > 9 else True  #<-- index 9 should contain just numbers
    condition_3 = any(token in r[22] for token in meetposten) if len(r) > 22 else True #<-- index 22 just contain a character which is mentioned in mp (this is a list with characters)
    return condition_1 and condition_2 and condition_3


def timestamp_to_columns(timestamp):
    date_object = datetime.datetime.fromisoformat(timestamp)
    time_tuple = date_object.timetuple()
    return [*time_tuple[:6], int(date_object.utcoffset().seconds / 3600)] #<--- this function is pulling apart the datetime in YMDHMSZ


def output_record(vehicle_loc_list):   #<--- this function is making the output
    first_sighting = vehicle_loc_list[0]  #<-- the first time a vehicle is seen
    last_sighting = vehicle_loc_list[-1] #<-- the last time a vehicle is seen
    vehicle_id = first_sighting[9] #<-- the vehicle ID
    location_id = first_sighting[22] #<-- the location ID
    short_location = location_token(first_sighting) #<-- The name of the location shortened
    full_location = pplg_verkortingen[short_location] #<-- the name of the location complete
    number_of_sightings = len(vehicle_loc_list) #<-- amount of times a row has been spotted
    begin_or_end = 'BEGIN' if number_of_sightings == 1 else 'END'#<-- if a row has been spotted just once then add BEGIN else END
    first_time_spotted = timestamp_to_columns(first_sighting[6]) #<--- the first time the vehicle has been first time spotted
    last_time_spotted = timestamp_to_columns(last_sighting[6])  #<-- the last time the vehicle has been first time spotted
    comando_1 = first_sighting[5]
    comando_2 = last_sighting[5] if begin_or_end == 'END' else ' '
    return [
        vehicle_id,
        begin_or_end,
        location_id,
        *first_time_spotted,
        *last_time_spotted,
        number_of_sightings,
        full_location,
        short_location,
        comando_1,
        comando_2
    ]


def group_records(vehicle_loc_list):  #<-- stick the records together of the vehicles that has been spotted more then once or the vehicle
    result = [ [] ]
    last_time = datetime.datetime.fromisoformat(vehicle_loc_list[0][6])

    for record in vehicle_loc_list:
        next_time = datetime.datetime.fromisoformat(record[6])
        if next_time - last_time < datetime.timedelta(hours=6):
            result[-1].append(record)
        else:
            result.append([record])
        last_time = next_time
    return result


vehicle_loc_dict = collections.defaultdict(list)
for file in os.listdir(zipped_trots_files):
     file_path = os.path.join(zipped_trots_files, file)
     with open(file_path, 'r') as my_file:
         reader = csv.reader(my_file, delimiter = ',')
         next(reader)
         for row in reader:
             if filter_row(row):
                 vehicle_loc_dict[(row[9], location_token(row))].append(row)


 with open(tr_files + '\\' + 'DFile', 'w') as output:
     writer = csv.writer(output, delimiter = '\t')
     for vehicle_loc_list in vehicle_loc_dict.values():
         for record_group in group_records(vehicle_loc_list):
             writer.writerow(output_record(record_group))

             
