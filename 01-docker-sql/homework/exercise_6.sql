SELECT *
FROM green_taxi_trips JOIN zones zone_drop_off ON green_taxi_trips."DOLocationID" = zone_drop_off."LocationID"
JOIN zones zone_pickup_off ON green_taxi_trips."PULocationID" = zone_pickup_off."LocationID"
LIMIT 1;