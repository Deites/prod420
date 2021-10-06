from django.db import models

class DataFromHub(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    surname = models.CharField(max_length=50, verbose_name='Surname')
    uuid = models.IntegerField(verbose_name='Uuid')
    date = models.DateTimeField(verbose_name='Date and Time')
    status = models.IntegerField(verbose_name='Status')
    type_passage = models.IntegerField(verbose_name='Type Passage')
    sync = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} -- {self.surname}'

class PlateNumber(models.Model):
    plate_number_datafromhub = models.OneToOneField(DataFromHub, on_delete=models.CASCADE)
    plate_number = models.CharField(max_length=50, verbose_name='Plate Number')

    def __str__(self):
        return f'{self.plate_number}'

class Group(models.Model):
    group_datafromhub = models.OneToOneField(DataFromHub, on_delete=models.CASCADE)
    group = models.CharField(max_length=50, verbose_name='Group')

    def __str__(self):
        return f'{self.group}'

class Direction(models.Model):
    direction_datafromhub = models.OneToOneField(DataFromHub, on_delete=models.CASCADE)
    direction = models.CharField(max_length=50, verbose_name='Direction')

    def __str__(self):
        return f'{self.direction}'

class Photo(models.Model):
    photo_datafromhub = models.OneToOneField(DataFromHub, on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name='Photo')

    def __str__(self):
        return f'{self.photo}'
