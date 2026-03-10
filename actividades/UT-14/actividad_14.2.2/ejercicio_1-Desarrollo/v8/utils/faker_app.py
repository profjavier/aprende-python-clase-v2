'''
pip install Faker
'''
import random
import sys

from dao.articulos_dao import ArticulosDao
from faker import Faker

fake = Faker("es_ES")

'''print(fake.name())
print(fake.email())
print(fake.address())
print(fake.phone_number())'''

def generar_articulo():
    return {
        "referencia": fake.bothify(text="???#####").upper(),
        #"descripcion": fake.word().capitalize(),
        "descripcion": fake.sentence().capitalize(),
        "precio": round(random.uniform(1, 200), 2),
        "stock": random.randint(0, 500),
        "observaciones": fake.sentence()
    }

#print(generar_articulo())
dao = ArticulosDao()
dao.delete_all()

total = 10000
for i in range(1, total + 1):
    articulo = generar_articulo()
    dao.save(articulo)
    '''porcentaje = (i / total) * 100
    print(f"Generando artículos: {i}/{total} ({porcentaje:.1f}%)",
          end="\r", flush=True)'''
    porcentaje = (i / total) * 100
    sys.stdout.write(f"\rGenerando artículos: {i}/{total} ({porcentaje:.1f}%)")
    sys.stdout.flush()