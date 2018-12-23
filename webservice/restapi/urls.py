from django.urls import re_path
from restapi import views


urlpatterns = [
    re_path(r'^link-list/$', views.link_list, name='link-list'),
    # re_path(r'^link-list/$', views.AnswerView.as_view(), name=views.AnswerView.name),
]
