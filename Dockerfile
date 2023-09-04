FROM postgres:latest
VOLUME /var/lib/postgresql/data

ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_DB portal_database
ENV PG_MAJOR 13
ENV PG_COLLATE C.UTF-8
ENV PG_CTYPE C.UTF-8
ENV POSTGRES_HOST_AUTH_METHOD trust

EXPOSE 5432

# sudo docker exec -it 739cd4c35517 bash
# su - postgres
# psql
# \l
# sudo docker run -d -v ./db:/var/lib/postgresql/data -p 5432:5432 db

