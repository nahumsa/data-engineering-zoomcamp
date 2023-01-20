WITH max_trip_distance AS (
    SELECT MAX(trip_distance) FROM green_taxi_trips
)

SELECT SPLIT_PART(lpep_pickup_datetime, ' ', '1') as day
FROM green_taxi_trips
WHERE (
    trip_distance = (SELECT * FROM max_trip_distance)
    );