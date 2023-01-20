DOCKERTAG := ingest_data

setup:
	pipenv install --dev

start_db:
	docker-compose up -d

end_db:
	docker-compose down

build:
	sudo docker build . -t ${DOCKERTAG}

ingestion_green_trip: build
	docker run -it \
  	--network="container:homework_pgdatabase_1" \
	${DOCKERTAG} \
	--user=root \
  	--password=root \
  	--host=localhost \
  	--port=5432 \
  	--db=ny_taxi \
	--url "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-01.csv.gz" \
  	--table_name=green_taxi_trips

ingestion_zones: build
	docker run -it \
  	--network="container:homework_pgdatabase_1" \
	${DOCKERTAG} \
	--user=root \
  	--password=root \
  	--host=localhost \
  	--port=5432 \
  	--db=ny_taxi \
	--url "https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv" \
  	--table_name=zones