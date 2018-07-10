from django.conf.urls import url, include
from django.contrib import admin
from . import views
from recruiter.views import CandidateList

urlpatterns = [
    url(r'^$', views.CandidateList.as_view(),name='candidate_list'),
    url(r'candidate/$', views.candidate,name='candidate'),
   ]
