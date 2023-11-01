from rest_framework import serializers
from .models import Region, District, School, Student, RegionMonthlyResult, Month


class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = ['id', 'title', 'ball', 'result', 'month_result']


class MonthSerializer(serializers.ModelSerializer):

    class Meta:
        model = Month
        fields = ['id', 'title']


class RegionMonthlyResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = RegionMonthlyResult
        fields = ['id', 'region_name', 'month', 'result']


class DistrictSerializer(serializers.ModelSerializer):

    class Meta:
        model = District
        fields = ['id', 'title', 'result', 'region']


class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = ['id', 'title', 'result', 'district']


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id', 'full_name', 'percentage', 'ball', 'school']

