from django.db import models

# Users of bot
class Users(models.Model):
    telegram_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=30, blank=True)
    full_name = models.CharField(max_length=30, blank=True)


# Students of university
class Students(models.Model):
    studnum = models.IntegerField(verbose_name="Номер студенческого билета", primary_key=True)
    studname = models.CharField(verbose_name="ФИО", max_length=50)
    studgroup = models.IntegerField(verbose_name="Группа")
    studyear = models.IntegerField(verbose_name="Год рождения")
    
    def __str__(self):
        return f'{self.studname}\n{self.studgroup}'


# Requests for office
class Requests(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name="ID пользователя")
    studnum = models.ForeignKey(Students, on_delete=models.CASCADE, verbose_name="Номер студенческого билета")
    date = models.DateField(blank=True, verbose_name="Дата заявки")
    organisation = models.CharField(max_length=50, blank=False, verbose_name="Название организации")
    created = models.BooleanField(default=False, verbose_name="Состояние выполнения")
