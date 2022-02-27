from select import select
import time 

from django.contrib.auth.models import User
from django.core.mail import send_mail
from tasks.models import Task
from datetime import timedelta

from celery.decorators import periodic_task
from celery.schedules import crontab

from task_manager.celery import app

from tasks.models import Profile,STATUS_CHOICES

from datetime import datetime
import pytz

        
@periodic_task(run_every=timedelta(seconds=60))
def send_mail_reminder():
        print("==================================================!")
        current_time = datetime.now(pytz.timezone("UTC"))
        print("Current time "+str(current_time))
        for profile in Profile.objects.filter(next_update__lt = current_time):
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
            profile.next_update = profile.next_update + timedelta(days=1)
            profile.save(update_fields=['next_update'])
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



