from django.db import models

BUILDING_TYPE_CHOICES = [
        ('Сруб', 'Сруб'),
        ('Кирпичные дома', 'Кирпичные дома'),
        ('Каркасные дома', 'Каркасные дома'),
    ]

# Create your models here.
class House(models.Model):
    
    name = models.CharField('Название дома', max_length=100)
    area = models.FloatField('Площадь дома')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    building_type = models.CharField('Тип постройки', max_length=100, choices=BUILDING_TYPE_CHOICES)
    floors = models.IntegerField('Этажи')
    rooms = models.IntegerField('Количество комнат')
    bathrooms = models.IntegerField('Санузлы')
    style = models.CharField('Стиль', max_length=100)
    description = models.TextField('Описание')

    def __str__(self):
        return self.name
    
class HouseImage(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField('Изображение', upload_to='catalog/media/')

    def __str__(self):
        return f'Image for {self.house}'     

class Location(models.Model):
    house = models.OneToOneField(House, on_delete=models.CASCADE, related_name='location')
    country = models.CharField('Страна', max_length=100)
    city = models.CharField('Город', max_length=100)
    latitude = models.FloatField('Широта')
    longitude = models.FloatField('Долгота')

    def __str__(self):
        return f'{self.city}, {self.country}'

class FloorPlan(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='floor_plans')
    name = models.CharField('Наименование', max_length=100)
    schema = models.ImageField('Схема этажа', upload_to='catalog/media/')

    def __str__(self):
        return self.name
    
class FloorPlanImage(models.Model):
    floor_plan = models.ForeignKey(FloorPlan, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField('Изображение', upload_to='catalog/media/')

    def __str__(self):
        return f'Image for {self.floor_plan}'    
    
class Room(models.Model):
    floor_plan = models.ForeignKey(FloorPlan, on_delete=models.CASCADE, related_name='rooms')
    name = models.CharField('Название комнаты', max_length=100)
    area = models.FloatField('Количество квадратных метров')

    def __str__(self):
        return self.name    