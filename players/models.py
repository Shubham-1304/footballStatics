from django.db import models

class Player(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    nationality=models.CharField(max_length=100)
    overall=models.IntegerField()

    def __str__(self) -> str:
        return self.name


