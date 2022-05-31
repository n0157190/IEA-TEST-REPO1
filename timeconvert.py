# Timeconvert lab
from datetime import datetime
import sys
import time
#timestamp = 1545730073
timestamp = sys.argv[1]
answer = input('Would you like your timestamp in a fancy iso 8601 format? Y or N ')
time.sleep(2)
print('Ok')
if answer.lower() == 'n':
    dt_object = datetime.fromtimestamp(int(timestamp))
    print("dt_object =", dt_object)
else:
    dt = datetime.utcfromtimestamp(int(timestamp))
    iso_format = dt.isoformat() + 'Z'
    print(iso_format)