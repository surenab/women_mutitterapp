from django_filters import FilterSet, CharFilter
from django.db.models import Q
from .models import Kling

class KlingFilter(FilterSet):
    
    title_text = CharFilter(method='filter_title_text_search', label='Search by Title or Text')
    kling_category = CharFilter(lookup_expr='icontains', label='Search by Category')

    class Meta:
        model = Kling
        fields = ['kling_category', 'title_text']  # Specify the fields you want to filter on
    
    def filter_title_text_search(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) |
            Q(text__icontains=value)
        )
