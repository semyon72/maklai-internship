# IDE: PyCharm
# Project: maklai-internship
# Path: apps/test_task
# File: urls.py
# Contact: Semyon Mamonov <semyon.mamonov@gmail.com>
# Created by ox23 at 2023-04-29 (y-m-d) 10:04 PM
from django.urls import path

from apps.test_task.views import paraphrase_list

app_name = 'test_task'

urlpatterns = [
    path('paraphrase/', paraphrase_list, name='paraphrase'),
]