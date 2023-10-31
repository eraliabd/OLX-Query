from django.db import models


class MonthNameChoices(models.TextChoices):
    january = "January"
    february = "February"
    march = "March"
    april = "April"
    may = "May"
    june = "June"
    july = "July"
    august = "August"
    september = "September"
    october = "October"
    november = "November"
    december = "December"


class Region(models.Model):
    title = models.CharField(max_length=255)
    ball = models.FloatField()
    result = models.FloatField()

    month_choice = models.CharField(max_length=10, choices=MonthNameChoices, default=MonthNameChoices.january)

    def __str__(self):
        return self.title


class District(models.Model):
    """Tumanlar"""

    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    result = models.FloatField()

    def __str__(self):
        return self.title


class School(models.Model):
    """Maktablar"""

    district = models.ForeignKey(District, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    result = models.FloatField()

    def __str__(self):
        return self.title


class Student(models.Model):
    """Maktab o'quvchilari"""

    school = models.ForeignKey(School, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    result = models.FloatField()

    def __str__(self):
        return self.title
