import schedule
import time

def task():
    # Write your daily task code here
    print("Running the daily task at 9 AM...")

# Schedule the task to run every day at 9 AM
schedule.every().day.at("09:00").do(task)

# Keep the program running
while True:
    schedule.run_pending()
    time.sleep(1)
