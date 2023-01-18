setup:
	pipenv install --dev

start_db:
	docker-compose up -d

end_db:
	docker-compose down

build:
	docker build . -t ingest_data_nyt

ingestion: build
	docker run -it \
  	--network="container:01dockersql_pgdatabase_1" \
	ingest_data_nyt \
	--user=root \
  	--password=root \
  	--host=localhost \
  	--port=5432 \
  	--db=ny_taxi \
	--year=2022 \
	--month=01 \
  	--table_name=yellow_taxi_trips