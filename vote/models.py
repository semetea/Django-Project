from tkinter import CASCADE
from django.db import models
from acc.models import User

# Create your models here.
class Topic(models.Model) :
    subject = models.CharField(max_length=100)
    maker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="maker") # related_name은 User의 역참조 지시자
    content = models.TextField()
    voter = models.ManyToManyField(User, blank=True, related_name="voter")

    def __str__(self) :
        return self.subject

    def summary(self) :
        if len(self.content) > 20 :
            return f"{self.content[:10]}..."

class Sel(models.Model) :
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    sname = models.CharField(max_length=100)
    spic = models.ImageField(upload_to="vote/%y/%m")
    scon = models.TextField()
    choicer = models.ManyToManyField(User, blank=True)

    def __str__(self) -> str:
        return f"{self.topic}_{self.sname}"