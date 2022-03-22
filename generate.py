import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','firstcrud.settings')

import django
django.setup()

from crud.models import *
from faker import Faker
from random import *
faker = Faker()

def generate(n):
    for i in range(n):
        fsno = randint(100,999)
        fsname=faker.name()
        fsclass=randint(1,10)
        fsaddress=faker.name()
        std_record=Student.objects.get_or_create(sno=fsno,sname=fsname,sclass=fsclass,saddress=fsaddress)
generate(10)
