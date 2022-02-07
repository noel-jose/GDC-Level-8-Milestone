from .models import Task, TaskHistory
from django.db.models.signals import pre_save
from django.dispatch import receiver


@receiver(pre_save, sender=Task)
def create_taskhistory(sender, instance, **kwargs):
    if Task.objects.filter(id=instance.id).exists():
        prev_status = Task.objects.filter(id=instance.id).values_list("status")
        curr_status = instance.status
        history = TaskHistory(
            previous_status=prev_status, current_status=curr_status, task=instance
        )
        history.save()
        print(f"Successfully created a history for the task {instance.title}")
