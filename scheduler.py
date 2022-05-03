from datetime import datetime
import chat
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger

sched = BlockingScheduler()

# Schedule job_function to be called every one minute
sched.add_job(chat.send_msg,IntervalTrigger(),seconds=1)

sched.start()