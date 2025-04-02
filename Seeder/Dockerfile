FROM python:3.9-alpine

WORKDIR /Seeder

#dependance
RUN pip install pymongo


COPY Seeder.py /Seeder/seeder.py

# Exécuter le script seeder.py lorsque le conteneur démarre
CMD ["python", "seeder.py"]