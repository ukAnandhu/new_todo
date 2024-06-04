from django.urls import path 
from . import views 


urlpatterns = [

    path("", views.tasks, name="tasks"),
    path("task_list/", views.task_list, name="task_list"),

    path("task_list/<int:id>/task_update", views.task_update, name="task_update"),
    path("task_list/<int:id>/task_delete", views.task_delete, name="task_delete")
    
]
