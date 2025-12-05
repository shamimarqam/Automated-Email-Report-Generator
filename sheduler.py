import schedule
import time
import subprocess

def run_job():
    subprocess.run(["python3", "main.py"])

schedule.every().day.at("09:00").do(run_job)

while True:
    schedule.run_pending()
    time.sleep(1)