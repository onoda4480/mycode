#jphacks

import schedule
import time

def job():
    print("Hello, World!")

schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

