from django.http import HttpResponse
from django.views import View

from django.http.response import JsonResponse
from django.shortcuts import render

from tasks.models import STATUS_CHOICES, Task

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework.serializers import ModelSerializer

from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User

from django_filters.rest_framework import (
    DjangoFilterBackend,
    FilterSet,
    CharFilter,
    ChoiceFilter,
    BooleanFilter,
)


class TaskFilter(FilterSet):
    title = CharFilter(lookup_expr="icontains")
    status = ChoiceFilter(choices=STATUS_CHOICES)
    completed = BooleanFilter()


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username"]


class TaskSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ["title", "description", "priority", "completed", "user", "status"]


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    permission_classes = (IsAuthenticated,)

    filter_backends = (DjangoFilterBackend,)
    filterset_class = TaskFilter

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user, deleted=False)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskListAPI(APIView):
    def get(self, request):
        tasks = Task.objects.filter(deleted=False)
        data = TaskSerializer(tasks, many=True).data

        return Response(
            {"tasks": data},
        )


# class TaskListAPI(View):
#     def get(self, request):
#         tasks = Task.objects.filter(deleted=False)
#         data = []
#         for task in tasks:
#             data.append({"title": task.title})
#         return JsonResponse({"tasks": data})


# class TaskCreateAPI(View):
#     def get(self, request):
#         return render(request, "form.html")

#     def post(self, request):
#         print(request.POST)
#         task = Task(
#             title=request.POST.get("title"),
#             priority=request.POST.get("priority"),
#             description=request.POST.get("description"),
#         )
#         task.save()
#         return HttpResponse("Successfully stored the task")
