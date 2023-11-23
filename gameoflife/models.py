from django.db import models

class Cell(models.Model):
    row = models.IntegerField()
    col = models.IntegerField()
    state = models.BooleanField(default=False)  # 0 for dead, 1 for alive
