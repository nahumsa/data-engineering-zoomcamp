WITH green_taxi_passengers AS (
    SELECT passenger_count
    FROM green_taxi_trips
    WHERE
    (
        lpep_pickup_datetime >= '2019-01-01 00:00:00'
        AND lpep_pickup_datetime <= '2019-01-01 23:59:59'
    ) AND
    (
        lpep_dropoff_datetime >= '2019-01-01 00:00:00'
        AND lpep_dropoff_datetime <= '2019-01-01 23:59:59'
    )
)

SELECT passenger_count, COUNT(*) AS number_of_trips
FROM green_taxi_passengers
WHERE passenger_count IN (2, 3)
GROUP BY passenger_count;