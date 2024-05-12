from faker import Faker
from django.contrib.auth.models import User
import csv

def generarCompanias():
    fake = Faker()

    with open('companies.csv','w',newline='') as file:
        writer = csv.writer(file)

        #Escribir titulos
        writer.writerow(['User','Email','Password'])

        #Escribir datos
        for i in range(0,100):
            user = fake.company().replace(" ","").strip()
            email = fake.email().strip()
            password = fake.password().strip()
            writer.writerow([user,email,password])
            # user = User.objects.create_user(user,email,password)

generarCompanias()