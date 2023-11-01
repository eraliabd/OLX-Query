# annotate(ball=Sum('regions__districts__schools__students__ball'))
# Region.objects.all().filter(districts__schools__students__ball__lst=1)

from django.db.models import F, Q, Count, Sum, Min, Max, Aggregate

from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from .models import Region, District, School, Student, RegionMonthlyResult, Month
from .serializers import RegionSerializer, DistrictSerializer, SchoolSerializer, StudentSerializer, \
    RegionMonthlyResultSerializer, RegionDistrictSerializer, RegionMonthSerializer, DistrictSchoolSerializer


class RegionListView(ListCreateAPIView):
    queryset = Region.objects.region_ball()
    serializer_class = RegionSerializer


class RegionMonthlyResultListView(ListCreateAPIView):
    queryset = RegionMonthlyResult.objects.all()
    serializer_class = RegionMonthlyResultSerializer


class DistrictListView(ListCreateAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer


class SchoolListView(ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class StudentListView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class RegionDistrictView(ListCreateAPIView):
    queryset = Region.objects.order_by('-districts__result')
    serializer_class = RegionDistrictSerializer


class RegionMonthView(ListCreateAPIView):
    queryset = Month.objects.all()
    serializer_class = RegionMonthSerializer


class DistrictSchoolView(ListCreateAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSchoolSerializer


# .filter(districts__result__gte=Region.objects.aggregate(Min('districts__result')))
