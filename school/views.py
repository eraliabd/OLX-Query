from django.db.models import F, Q, Count, Sum, Min, Max

from rest_framework.generics import ListCreateAPIView

from .models import Region, District, School, Student, RegionMonthlyResult
from .serializers import RegionSerializer, DistrictSerializer, SchoolSerializer, StudentSerializer, \
    RegionMonthlyResultSerializer


class RegionListView(ListCreateAPIView):
    queryset = Region.objects.all()
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
