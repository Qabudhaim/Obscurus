FROM postgres:latest

ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_DB portal_database

EXPOSE 5432

# sudo docker exec -it 739cd4c35517 bash
# su - postgres
# psql
# \l
# sudo docker run -d -v ./db:/var/lib/postgresql/data -p 5432:5432 db

