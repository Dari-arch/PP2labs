from datetime import datetime
current_datetime = datetime.now()
print("Current datetime with microseconds:", current_datetime)
datetime_without_microseconds = current_datetime.replace(microsecond=0)
print("Datetime without microseconds:", datetime_without_microseconds)