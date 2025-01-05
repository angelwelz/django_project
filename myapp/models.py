from django.db import models

class Calculation(models.Model):
    expression = models.CharField(max_length=255)
    result = models.IntegerField()
    def __str__(self):
        return f"{self.expression} = {self.result}"

class Expression(models.Model):
    content = models.TextField()
    def __str__(self):
        return self.content