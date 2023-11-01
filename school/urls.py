from django.urls import path

from .views import RegionListView, DistrictListView, SchoolListView, StudentListView, RegionMonthlyResultListView

urlpatterns = [
    path('region/', RegionListView.as_view(), name='region'),
    path('district/', DistrictListView.as_view(), name='district'),
    path('school/', SchoolListView.as_view(), name='school'),
    path('student/', StudentListView.as_view(), name='student'),
    path('region/monthly-result/', RegionMonthlyResultListView.as_view(), name='region-monthly-result'),
]
