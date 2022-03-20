#creating docker, relations

FROM python:3.9.11-buster
COPY requirements.txt /requirements.txt
RUN [ "pip","install","-r","requirements.txt" ]

