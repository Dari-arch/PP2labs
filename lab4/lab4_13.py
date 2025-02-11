from datetime import datetime

def date_diff_in_seconds(date1, date2):
    datetime_format = "%Y-%m-%d %H:%M:%S"
    start = datetime.strptime(date1, datetime_format)
    end = datetime.strptime(date2, datetime_format)
    difference = end - start
    return difference.total_seconds()

# Example usage
date1 = input()
date2 = input()
print(f"Difference in seconds: {date_diff_in_seconds(date1, date2)}")