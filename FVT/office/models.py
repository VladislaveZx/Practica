from django.db import models

# Create your models here.
class User(models.Model):
    telegram_id = models.IntegerField(verbose_name='ID пользователя', primary_key=True)
    username = models.CharField(verbose_name='Псевдоним пользователя', max_length=50, blank=True)
    full_name = models.CharField(verbose_name='Имя пользователя', max_length=50, blank=True)
    
class Stud(models.Model):
    id = models.ForeignKey(verbose_name='ID пользователя', to=User, on_delete=models.CASCADE)
    studnum = models.IntegerField(verbose_name='Номер студенческого билета', primary_key=True)
    studname = models.CharField(verbose_name='ФИО', max_length=70)
    studgroup = models.IntegerField(verbose_name='Номер группы')
    studyear = models.IntegerField(verbose_name='Год рождения')
    
class Requests(models.Model):
    user = models.ForeignKey(verbose_name='ID пользователя', to=User, on_delete=models.CASCADE)
    studnum = models.ForeignKey(verbose_name='Номер студенческого билета', to=Stud, on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Дата подачи заявления')
    destination = models.CharField(verbose_name='Название организации', max_length=50)
    status = models.BooleanField(verbose_name='Статус выполнения', default=False)

class StudGraph(models.Model):
    WEEKS_CHOICES = [
        ('chisl', 'Числитель'),
        ('znam', 'Знаменатель'),
    ]
    studcourse = models.IntegerField(verbose_name='Курс')
    studgroup = models.IntegerField(verbose_name='Номер группы')
    week = models.CharField(verbose_name='Неделя', max_length=12, choices=WEEKS_CHOICES)
    day = models.CharField(verbose_name='День недели', max_length=20)
    time_start = models.TimeField(verbose_name='Время начала')
    time_end = models.TimeField(verbose_name='Время завершения')
    lesson = models.CharField(verbose_name='Название дисциплины', max_length=40)
    cabinet = models.CharField(verbose_name='Номер кабинета', max_length=10, default=0)
    lesson_type = models.CharField(verbose_name='Тип занятия', max_length=10)
    teacher = models.CharField(verbose_name='Преподаватель', max_length=100)
