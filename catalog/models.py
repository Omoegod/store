from django.db import models

# Create your models here.
class House(models.Model):
    BUILDING_TYPE_CHOICES = [
        ('Сруб', 'Сруб'),
        ('Кирпичные дома', 'Кирпичные дома'),
        ('Каркасные дома', 'Каркасные дома'),
    ]
    name = models.CharField('Название дома', max_length=100)
    area = models.FloatField('Площадь дома')
    image = models.ImageField('Фото объекта', upload_to='image_house/')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    building_type = models.CharField('Тип постройки', max_length=100, choices=BUILDING_TYPE_CHOICES)
    floors = models.IntegerField('Этажи')
    rooms = models.IntegerField('Количество комнат')
    bathrooms = models.IntegerField('Санузлы')
    style = models.CharField('Стиль', max_length=100)
    description = models.TextField('Описание')
    location = models.CharField('Расположение объекта', max_length=100)

    def __str__(self):
        return self.name

class FloorPlan(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='floor_plans')
    name = models.CharField('Наименование', max_length=100)
    schema = models.ImageField('Схема этажа', upload_to='floor_plans/')
    description = models.TextField('Описание')

    def __str__(self):
        return self.name