from .models import Task, TaskHistory
from django.db.models.signals import pre_save
from django.dispatch import receiver


@receiver(pre_save, sender=Task)
def create_taskhistory(sender, instance, update_fields, **kwargs):
    print("The update fields are ", update_fields)
    # if Task.objects.filter(id=instance.id).exists():
    #     prev_status = Task.objects.filter(id=instance.id).values_list("status")
    #     curr_status = instance.status
    #     if prev_status != curr_status:
    #         history = TaskHistory(
    #             previous_status=prev_status, current_status=curr_status, task=instance
    #         )
    #         history.save()
    #         print(f"Successfully created a history for the task {instance.title}")

    if instance.id is None:
        pass
    else:
        prev_status = Task.objects.get(id=instance.id).status
        curr_status = instance.status
        if curr_status != prev_status:
            history = TaskHistory(
                previous_status=prev_status, current_status=curr_status, task=instance
            )
            history.save()
            print(
                f"Successfully created a new history for the change {prev_status} --> {curr_status}"
            )
