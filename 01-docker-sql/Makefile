setup:
	pipenv install --dev

ingestion:
	pipenv run python ingest_data.py \
  	--user=root \
  	--password=root \
  	--host=localhost \
  	--port=5432 \
  	--db=ny_taxi \
	--year=2022 \
	--month=01 \
  	--table_name=yellow_taxi_trips