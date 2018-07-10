# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Location(models.Model):
    city_name = models.CharField(max_length=255, null=True,blank=True, verbose_name="City Name")

    def __unicode__(self):
        return self.city_name

class Skills(models.Model):
    skill = models.CharField(max_length=255, null=True,blank=True, verbose_name="Skill Name")

    def __unicode__(self):
        return self.skill


class CandidateDetails(models.Model):
    serial_number = models.IntegerField(default=1,null=True,blank=True, verbose_name="Serial Number")
    resume = models.BooleanField(default=False,blank=True, verbose_name="Is having Resume")
    name = models.CharField(max_length=255, null=True,blank=True, verbose_name="Candidate Name")
    phone = models.CharField(max_length=15, null=True,blank=True, verbose_name="Phone")
    email = models.CharField(max_length=255, null=True,blank=True, verbose_name="Candidate Email")
    experience = models.IntegerField(default=0,null=True, blank=True, verbose_name="Work experience")
    analytics_experience = models.CharField(max_length=255,null=True, blank=True, verbose_name="Analytics in Experience")
    current_location = models.CharField(max_length=255, null=True,blank=True, verbose_name="current location")
    corrected_location = models.CharField(max_length=255, null=True,blank=True, verbose_name="corrected location")
    nearest_city = models.CharField(max_length=255, null=True,blank=True, verbose_name="nearest city")
    preferred_location = models.ManyToManyField("Location", blank=True, related_name="city")
    ctc = models.IntegerField(default=0,null=True, blank=True, verbose_name="CTC")
    current_employer = models.CharField(max_length=255, null=True,blank=True, verbose_name="current employer")
    current_designation = models.CharField(max_length=255, null=True,blank=True, verbose_name="current employer")
    skills = models.ManyToManyField("Skills", blank=True, related_name="city")
    ug = models.CharField(max_length=255, null=True,blank=True, verbose_name="UG courses")
    ug_inst = models.CharField(max_length=255, null=True,blank=True, verbose_name="UG institution name")
    ug_year = models.CharField(max_length=255, null=True,blank=True, verbose_name="UG year of Passing")

    def __unicode__(self):
        return self.name
