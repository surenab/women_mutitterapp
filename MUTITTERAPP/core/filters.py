from django_filters import FilterSet, CharFilter
from django.db.models import Q
from .models import Kling

class KlingFilter(FilterSet):
    
    title = CharFilter(lookup_expr='icontains', label='Search by Title')
    kling_category = CharFilter(lookup_expr='icontains', label='Search by Category')
    text = CharFilter(lookup_expr='icontains', method='filter_text_search', label='Search by Text')

    class Meta:
        model = Kling
        fields = []
    
    def filter_text_search(self, queryset, value):
       return queryset.filter(
        Q(title__icontains=value) |
        Q(kling_category__icontains=value) |
        Q(text__icontains=value) 
        )
    
    
