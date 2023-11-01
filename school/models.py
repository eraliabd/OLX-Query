from django.db import models


# class MonthNameChoices(models.TextChoices):
#     """Oy nomlari"""
#
#     january = "January"
#     february = "February"
#     march = "March"
#     april = "April"
#     may = "May"
#     june = "June"
#     july = "July"
#     august = "August"
#     september = "September"
#     october = "October"
#     november = "November"
#     december = "December"


class Month(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Region(models.Model):
    """Viloyatlar"""

    title = models.CharField(max_length=255)
    ball = models.FloatField(null=True, blank=True)
    result = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title


class RegionMonthlyResult(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='regions')
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    result = models.FloatField(null=True, blank=True, default=0)

    def __str__(self):
        return f"{self.region} - result: {self.result}"

    @property
    def region_name(self):
        return self.region.title


class District(models.Model):
    """Tumanlar"""

    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='districts')

    title = models.CharField(max_length=255)
    result = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title


class School(models.Model):
    """Maktablar"""

    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='schools')

    title = models.CharField(max_length=255)
    result = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title


class Student(models.Model):
    """Maktab o'quvchilari"""

    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')
    full_name = models.CharField(max_length=255, null=True, blank=True)
    percentage = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.full_name

    @property
    def ball(self):
        if self.percentage <= 100 and self.percentage >= 80:
            return 1
        elif self.percentage < 80 and self.percentage >= 50:
            return 0.5
        else:
            return 0
