from rest_framework import serializers
from .models import Region, District, School, Student, RegionMonthlyResult, Month


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'title', 'ball', 'result']


class MonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Month
        fields = ['title']


class RegionMonthlyResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegionMonthlyResult
        fields = ['region_title', 'result']


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['title', 'result']


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['title', 'result']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'full_name', 'percentage', 'student_ball', 'school', 'result_ball']


class RegionDistrictSerializer(serializers.ModelSerializer):
    """Regions Districts'ining o'rtacha natijasi"""

    district = DistrictSerializer(source='districts', many=True, read_only=True)

    class Meta:
        model = Region
        fields = ['id', 'title', 'district']


class RegionMonthSerializer(serializers.ModelSerializer):
    """Regions'ning oylari kesimidagi o'rtacha ko'rsatkichi"""

    region = RegionMonthlyResultSerializer(source='regions', many=True, read_only=True)

    class Meta:
        model = Month
        fields = ['title', 'region']


class DistrictSchoolSerializer(serializers.ModelSerializer):
    """Districts'ning schools kesimidagi o'rtacha ko'rsatkichi"""

    school = SchoolSerializer(source='schools', many=True, read_only=True)

    class Meta:
        model = District
        fields = ['title', 'school']
