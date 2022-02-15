import time 

from django.contrib.auth.models import User
from django.core.mail import send_mail
from tasks.models import Task
from datetime import timedelta

from celery.decorators import periodic_task

from task_manager.celery import app

# @periodic_task(run_every = timedelta(seconds=10))
# def send_mail_reminder():
#     print("Starting to process emails")
#     for user in User.objects.all():
#         pending_qs = Task.objects.filter(user = user,completed = False,deleted = False)
#         email_content = f"You have {pending_qs.count()} Pending Tasks"
#         send_mail("Pending tasks from task manager",email_content,"task@task_manager.org",{user.email})
#         print(f"Completed Processing user {user.id}")

@app.task 
def test_background_jobs():
    print("This is from the bg")
    for i in range(10):
        time.sleep(1)
        print(i)



