1. clone repo
2. create `.env` file (see `.env.example`)
3. run: docker compose up --build


.evn->
SECRET_KEY=django-insecure-q$9dhks4e)cy3g^kco!b!#q3(y2vpt5#z!e8(v=((hxqri+)u$
DEBUG=1
SITE_URL=http://localhost:8080
ALLOWED_HOSTS=localhost,127.0.0.1
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_DB=blogdb
POSTGRES_USER=bloguser
POSTGRES_PASSWORD=supersecret

for using the current datas:
docker exec -i project-db-1 psql -U bloguser -d blogdb < backup.sql
