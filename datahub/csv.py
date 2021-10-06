import unicodecsv

from django.http import HttpResponse

from . import models

def data_csv(request):
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="dataset.csv"'},
    )

    writer = unicodecsv.writer(response, encoding='utf-8-sig')
    for d in models.DataFromHub.objects.all():
        writer.writerow([
            f'{d.name}',
            f'{d.surname}',
            f'{d.uuid}',
            f'{models.PlateNumber.objects.filter(plate_number_datafromhub=d).first()}',
            f'{models.Group.objects.filter(group_datafromhub=d).first()}',
            f'{d.date}',
            f'{models.Direction.objects.filter(direction_datafromhub=d).first()}',
            f'{d.status}',
            f'{d.type_passage}',
            f'{models.Photo.objects.filter(photo_datafromhub=d).first()}',
            f'{d.sync}',
        ])
    return response