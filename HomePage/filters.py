import django_filters
from .models import Timetable


class TimetableFilter(django_filters.FilterSet):
    from_airport = django_filters.CharFilter(field_name='from_airport')
    to_airport = django_filters.CharFilter(field_name='to_airport')
    departure_date = django_filters.DateTimeFilter(field_name='departure_date')
    return_date = django_filters.DateTimeFilter(field_name='return_date')


    class Meta:
        model = Timetable
        fields = ['from_airport', 'to_airport', 'departure_date', 'return_date']
