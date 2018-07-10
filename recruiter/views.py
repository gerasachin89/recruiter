# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from recruiter.models import CandidateDetails
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.urlresolvers import reverse
from django.db.models import Q
from recruiter.filters import ContactFilter
import csv

# Create your views here.
def candidate(request):
    """
    This method give the list of candidates after and before filtering the data.
    filter can be done by-
    candidate name, phone, email, current location, CTC less than or equal to, CTC greater than or equal to, work experience less than or equal to.
    skill (can be given multiple), prefered location (can be given multiple)

    Methods Allowed:
      GET
      POST

    Results:
      GET:
        On Success:
          Returns: List of filtered candidate

      POST
        On Success:
          Returns: Export Candidate data as CSV
    """
    object_list = CandidateDetails.objects.all()
    f = ContactFilter(request.GET, queryset=object_list)
    if request.method == "POST":
        opts = f.qs.model._meta
        model = f.qs.model
        response = HttpResponse(content_type='text/csv')
        # force download.
        response['Content-Disposition'] = 'attachment;filename=export.csv'
        # the csv writer
        writer = csv.writer(response)
        field_names = [field.name for field in opts.fields]
        # Write a first row with header information
        writer.writerow(field_names)
        # Write data rows
        for obj in f.qs:
            writer.writerow([getattr(obj, field) for field in field_names])
        return response
    return render(request, "candidate_list.html",{'filter': f})


class CandidateList(ListView):
    """
    This method give the list of candidates after and before filtering the data.

    Methods Allowed:
      GET

    Results:
      GET:
        On Success:
          Returns: List of filtered candidate
    """
    model = CandidateDetails
    filter_set = ContactFilter
    template_name = 'candidate_list.html'
    #paginate_by = 10  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super(CandidateList,self).get_context_data(**kwargs)
        object_list = CandidateDetails.objects.all()
        paginator = Paginator(object_list, 5) # Show 25 contacts per page

        page = self.request.GET.get('page')
        try:
            candidate = paginator.page(page)
        except PageNotAnInteger:
            candidate = paginator.page(1)
        except EmptyPage:
            candidate = paginator.page(paginator.num_pages)
        context['total_count'] = object_list.count()
        context['object_list'] = candidate
        return context
