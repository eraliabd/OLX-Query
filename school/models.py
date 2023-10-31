from django.db import models


class MonthNameChoices(models.TextChoices):
    """Oy nomlari"""

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
    """Viloyatlar"""

    title = models.CharField(max_length=255)
    ball = models.FloatField(null=True, blank=True)
    avg_result = models.FloatField()
    month_result = models.FloatField()

    month_choice = models.CharField(
        max_length=10, choices=MonthNameChoices, null=True, blank=True
    )

    def __str__(self):
        return self.title


class District(models.Model):
    """Tumanlar"""

    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='districts')

    title = models.CharField(max_length=255)
    result = models.FloatField()

    def __str__(self):
        return self.title


class School(models.Model):
    """Maktablar"""

    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='schools')

    title = models.CharField(max_length=255)
    result = models.FloatField()

    def __str__(self):
        return self.title


class Student(models.Model):
    """Maktab o'quvchilari"""

    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')
    full_name = models.CharField(max_length=255)
    percentage = models.FloatField()

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
