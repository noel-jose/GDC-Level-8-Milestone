import time 

from django.contrib.auth.models import User
from django.core.mail import send_mail
from tasks.models import Task
from datetime import timedelta

from celery.decorators import periodic_task
from celery.schedules import crontab

from task_manager.celery import app

from tasks.models import Profile,STATUS_CHOICES


# @periodic_task(run_every=(crontab(minute='*')), name="send_mail_reminder", ignore_result=True)


def setReminder(minutes,hours,profile):
    print("Starting of the setReminder section")
    # @periodic_task(run_every=(crontab(hour = hours,minute = minutes)), ignore_result=True,args = profile)
    app.conf.beat_schedule = {
    "send_email":{
        "task": 'tasks.tasks.send_mail_reminder',
        "schedule":crontab(hour = hours,minute = minutes),
        "args":(profile)
        }
    }
        
@app.task
def send_mail_reminder(profile):
        print("Starting to process emails")
        user = profile.user
        
        pending_qs = Task.objects.filter(user = user,deleted = False,status = STATUS_CHOICES[0][0])
        inprogress_qs = Task.objects.filter(user = user,deleted = False,status = STATUS_CHOICES[1][0])
        completed_qs = Task.objects.filter(user = user,deleted = False,status = STATUS_CHOICES[2][0])
        cancelled_qs = Task.objects.filter(user = user,deleted = False,status = STATUS_CHOICES[3][0])
        email_content = f"""You have,
        {pending_qs.count()} Pending Tasks
        {inprogress_qs.count()} Inprogress Tasks
        {completed_qs.count()} Completed Tasks
        {cancelled_qs.count()} Cancelled Tasks
        """
        send_mail("Pending tasks from task manager",email_content,"task@task_manager.org",{user.email})
        print(f"Completed Processing user {user.id}")


# adding "send_mail_reminder" to the beat scheduler
# app.conf.beat_schedule = {
#     "send_email":{
#         "task":"send_mail_reminder",
#         "schedule":crontab(minute="*")
#     }
# }

@app.task 
def test_background_jobs():
    print("This is from the bg")
    for i in range(10):
        time.sleep(1)
        print(i)



