from django.urls import path

from .views import RegionListView, DistrictListView, SchoolListView, StudentListView, RegionMonthlyResultListView, \
    RegionDistrictView, RegionMonthView, DistrictSchoolView

urlpatterns = [
    path('region/', RegionListView.as_view(), name='region'),
    path('district/', DistrictListView.as_view(), name='district'),
    path('school/', SchoolListView.as_view(), name='school'),
    path('student/', StudentListView.as_view(), name='student'),

    path('region/monthly-result/', RegionMonthlyResultListView.as_view(), name='region-monthly-result'),

    path('region-district/', RegionDistrictView.as_view(), name='region-district'),
    path('region-month/', RegionMonthView.as_view(), name='region-month'),
    path('district-school/', DistrictSchoolView.as_view(), name='district-school'),
]
