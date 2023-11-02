from django.db import models

from django.db.models import F, Q, Count, Sum, Min, Max, Avg

from django.db.models.functions import Coalesce
import json


# class RegionBallManager(models.Manager):
#     def region_ball(self):
#         response = self.get_queryset().annotate(
#             total_ball=Coalesce(Sum('districts__schools__students__result_ball'), 0.0))
#
#         result = list()
#         for res in response:
#             result.append({"title": res.title, "ball": res.total_ball})
#         result = json.dumps(result)
#         return result


class Month(models.Model):
    """Oylar"""

    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Region(models.Model):
    """Viloyatlar"""

    title = models.CharField(max_length=255)
    ball = models.FloatField(null=True, blank=True)
    result = models.FloatField(null=True, blank=True, default=0)

    # objects = RegionBallManager()

    def __str__(self):
        return self.title

    def avg_result(self):
        result = Region.objects.annotate(results=Coalesce(Avg('districts__result'), 0.0))
        self.result = result
        self.save()


class RegionMonthlyResult(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    month = models.ForeignKey(Month, on_delete=models.CASCADE, related_name='regions')
    result = models.FloatField(null=True, blank=True, default=0)

    def __str__(self):
        return f"{self.region} - Month: {self.month} - result: {self.result}"

    @property
    def region_title(self):
        return self.region.title

    @property
    def month_title(self):
        return self.month.title


class District(models.Model):
    """Tumanlar"""

    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='districts')

    title = models.CharField(max_length=255)
    result = models.FloatField(null=True, blank=True, default=0)

    def __str__(self):
        return self.title

    def avg_result(self):
        result = District.objects.annotate(results=Coalesce(Avg('schools__result'), 0.0))
        self.result = result
        self.save()


class School(models.Model):
    """Maktablar"""

    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='schools')

    title = models.CharField(max_length=255)
    result = models.FloatField(null=True, blank=True, default=0)

    def __str__(self):
        return self.title

    def avg_result(self):
        result = School.objects.annotate(results=Coalesce(Avg('students__percentage'), 0.0))
        self.result = result
        self.save()


class Student(models.Model):
    """Maktab o'quvchilari"""

    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')
    full_name = models.CharField(max_length=255, null=True, blank=True)
    percentage = models.FloatField(null=True, blank=True)
    result_ball = models.FloatField(null=True, blank=True, default=0)

    def __str__(self):
        return self.full_name



    def student_ball(self):
        try:
            if self.percentage <= 100 and self.percentage >= 80:
                self.result_ball = 1
            elif self.percentage < 80 and self.percentage >= 50:
                self.result_ball = 0.5
            else:
                self.result_ball = 0
            self.save()
        except Exception as error:
            print(error)
            pass
