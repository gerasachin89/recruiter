import django_filters
from recruiter.models import CandidateDetails, Skills, Location

class ContactFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    ctc_lte = django_filters.NumberFilter(name='ctc', lookup_expr='lte')
    ctc_gte = django_filters.NumberFilter(name='ctc', lookup_expr='gte')
    experience = django_filters.NumberFilter(name='experience', lookup_expr='lte')
    skills = django_filters.filters.ModelMultipleChoiceFilter(name='skills__skill',to_field_name='skill',queryset=Skills.objects.all(),)
    preferred_location = django_filters.filters.ModelMultipleChoiceFilter(name='preferred_location__city_name',to_field_name='city_name',queryset=Location.objects.all(),)
    class Meta:
        model = CandidateDetails
        fields = ['name', 'phone','email','current_location','ctc_lte','ctc_gte','experience','current_location','skills','preferred_location']
