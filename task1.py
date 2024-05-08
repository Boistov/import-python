from datetime import datetime, timedelta

def convert(minutes):


    time_string = f"00:{minutes:02}:00,000"
    pt = datetime.strptime(time_string, '%H:%M:%S,%f')
    total_seconds = pt.second + pt.minute * 60 + pt.hour * 3600
    return total_seconds

