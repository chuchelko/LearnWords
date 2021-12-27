from django.db import models

class Word(models.Model):
    first_language = models.CharField(max_length=20, default='')
    second_language = models.CharField(max_length=30, default='')
    image = models.ImageField(null=True, blank=True, upload_to='img/words/')
    user = models.ForeignKey("User", on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.first_language} - {self.second_language}"

class User(models.Model):
    name = models.CharField("Имя", max_length=20)
    email = models.EmailField("Почта", default='')
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    
    def __str__(self):
        return self.name