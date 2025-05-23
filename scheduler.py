from apscheduler.schedulers.background import BackgroundScheduler
def schedule_jobs():
    scheduler = BackgroundScheduler()
    scheduler.add_job(lambda: print("Retrain Triggered"), 'interval', hours=6)
    scheduler.add_job(lambda: print("Log Flushed"), 'cron', hour=23, minute=55)
    scheduler.start()
