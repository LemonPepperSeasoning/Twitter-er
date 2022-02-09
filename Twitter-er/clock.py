from apscheduler.schedulers.blocking import BlockingScheduler
from main import make_one_tweet
sched = BlockingScheduler()

# @sched.scheduled_job('interval', minutes=3)
# def timed_job():
#     print('This job is run every three minutes.')

# @sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
# def scheduled_job():
#     print('This job is run every weekday at 5pm.')

sched.add_job(make_one_tweet, 'cron', day='*', jitter=120)

sched.start()