from django.urls import path , reverse
from .views import TaskList , TaskDetail , TaskCreate , TaskUpdate , TaskDelete , CustomLoginView , RegisterPage , JournalList , JournalCreate , JournalUpdate , JournalDelete
from django.contrib.auth.views import LogoutView


app_name="todo"

urlpatterns=[
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='todo:login'), name="logout"),
    path('register/', RegisterPage.as_view(), name="register"),
    path('', TaskList.as_view(), name="tasks"),
    path('task/<int:pk>/', TaskDetail.as_view(), name="task_detail"),
    path('task/create/', TaskCreate.as_view(), name="task_create"),
    path('task/update/<int:pk>', TaskUpdate.as_view(), name= "Edit"),
    path('task/delete/<int:pk>', TaskDelete.as_view(), name= "Delete"),
    path('journal/', JournalList.as_view(), name= "journal"),
    path('journal/create/', JournalCreate.as_view(), name= "journal_create"),
    path('journal/update/<int:pk>', JournalUpdate.as_view(), name= "journal_update"),
    path('journal/delete/<int:pk>', JournalDelete.as_view(), name= "journal_delete"),
]
