# -*- coding: utf-8 -*-
#
from django.conf.urls import url
from adminpage.views import *

__author__ = "Epsirom"


urlpatterns = [
    url(r'^login/?$', AdminLogin.as_view()),
    url(r'^logout/?$', AdminLogout.as_view()),
    url(r'^activity/list/?$', ActivityList.as_view()),
    url(r'^activity/delete/?$', ActivityDelete.as_view()),
    url(r'^activity/create/?$', ActivityCreate.as_view()),
    url(r'^image/upload/?$', imageUpload.as_view()),
    url(r'^activity/detail/?$', ActivityDetail.as_view()),
    url(r'^activity/menu/?$', ActivityMenu.as_view()),
    url(r'^activity/checkin/?$', ActivityCheckin.as_view()),
]
