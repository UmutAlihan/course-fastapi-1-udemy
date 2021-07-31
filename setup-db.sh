docker run -v postgres:/var/lib/postgresql/data --name postgres-test -e POSTGRES_PASSWORD=mysecretpassword -d postgres
docker run -v pgadmin4:/home/pgadmin/.pgadmin -p 5051:5051 --network postgres-test:postgres-test --name pgadmin -d meedan/pgadmin
