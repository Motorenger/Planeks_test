import csv

from celery import shared_task

from django.conf import settings
from django.core.files.storage import default_storage

from faker import Faker

from data_sets.models import DataSet


faker = Faker()

@shared_task
def get_season_data(data_set_pk, columns, rows):
    faker_types = {
        "Full name": faker.name(),
        "Email": faker.email(),
        "Integer": faker.random_int(),
        "Company": faker.company(),
        "Job": faker.job(),
        "Phone number": faker.phone_number(),
        "Address": faker.address(),
    }
    path = f'/usr/src/app/media/data_set-{data_set_pk}-{rows}.csv'
    with open(path, 'w+') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([row["name"] for row in columns])
        for colunm in range(int(rows)):
            writer.writerow([faker_types[row["data_type"]] for row in columns])



        data_set = DataSet.objects.get(pk=data_set_pk)
        data_set.data_set_path = path 
        data_set.status = True 
        data_set.save()
