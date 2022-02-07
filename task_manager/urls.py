from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from tasks.models import Task
from tasks.views import (
    GenericAllTaskView,
    GenericCompletedTaskView,
    GenericTaskCompleteView,
    GenericTaskCreateView,
    GenericTaskDeleteView,
    GenericTaskDetailView,
    GenericTaskUpdateView,
    GenericTaskView,
    UserCreateView,
    UserLoginView,
    session_storage_view,
)

from tasks.apiviews import TaskHistoryViewSet, TaskListAPI

from rest_framework.routers import SimpleRouter

from tasks.apiviews import TaskViewSet

router = SimpleRouter()
router.register(prefix="api/tasks", viewset=TaskViewSet)
router.register(prefix="history/task", viewset=TaskHistoryViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("taskapi/", TaskListAPI.as_view()),
    # path("createtaskapi/", TaskCreateAPI.as_view()),
    path("tasks/", GenericTaskView.as_view()),
    path("create-task/", GenericTaskCreateView.as_view()),
    path("delete-task/<pk>/", GenericTaskDeleteView.as_view()),
    path("complete_task/<pk>/", GenericTaskCompleteView.as_view()),
    path("completed_tasks/", GenericCompletedTaskView.as_view()),
    path("all_tasks/", GenericAllTaskView.as_view()),
    path("update-task/<pk>", GenericTaskUpdateView.as_view()),
    path("detail-task/<pk>", GenericTaskDetailView.as_view()),
    path("sessiontest", session_storage_view),
    path("user/signup", UserCreateView.as_view()),
    path("user/login", UserLoginView.as_view()),
    path("user/logout", LogoutView.as_view()),
] + router.urls
