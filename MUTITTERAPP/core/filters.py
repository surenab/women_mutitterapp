from django_filters import FilterSet
from .models import Kling

class KlingFilter(FilterSet):
    class Meta:
        model=Kling

        fields=("title", "kling_category")