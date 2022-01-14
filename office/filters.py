from django.db.models import fields
import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class BookingFilter(django_filters.FilterSet):
    all_filter = CharFilter(field_name='HI_work_activity', lookup_expr='icontains')

#    start_date = DateFilter(field_name="date_created", lookup_expr="gte")

    class Meta:
        model = Booking
        fields = '__all__'
        exclude = [
            'applicant',
            'laboratory_code',
            'number_of_users',
            'date_created',
            'HI_work_activity',
            'HI_hazard',
            'HI_source',
            'RA_existing_risk_control',
            'RA_likelihood',
            'RA_severity',
            'RA_risk',
            'RC_countermeasure',
            'RC_PIC',
            'remarks',
        ]