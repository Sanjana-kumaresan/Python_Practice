def get_coordinate(record):
    return record[1]

def convert_coordinate(coord):
    return (coord[0], coord[1])

def compare_records(azara_record, rui_record):
    azara_coord = convert_coordinate(get_coordinate(azara_record))
    rui_coord = rui_record[1]
    
    return azara_coord == rui_coord

def create_record(azara_record, rui_record):
    if compare_records(azara_record, rui_record):
        return (
            azara_record[0],
            azara_record[1],
            rui_record[0],
            rui_record[1],
            rui_record[2]
        )
    return "not a match"

def clean_up(combined_records):
    report = ""
    
    for record in combined_records:
        cleaned = (
            record[0],  # treasure
            record[2],  # location
            record[3],  # coordinate tuple
            record[4]   # quadrant
        )
        report += str(cleaned) + "\n"
    
    return report

clean_up((
    ('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'),
    ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange')
))
