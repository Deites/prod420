from django.contrib import admin
from django.contrib.admin import StackedInline

from . import models

class PlateNumberAdmin(StackedInline):
    model = models.PlateNumber
    extra = 0

class GroupAdmin(StackedInline):
    model = models.Group
    extra = 0

class DirectionAdmin(StackedInline):
    model = models.Direction
    extra = 0

class PhotoAdmin(StackedInline):
    model = models.Photo
    extra = 0

@admin.register(models.DataFromHub)
class DateFromHubAdmin(admin.ModelAdmin):
    inlines = [PlateNumberAdmin, GroupAdmin, DirectionAdmin, PhotoAdmin]


