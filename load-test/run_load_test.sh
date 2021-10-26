starting_time=`date`

echo "Starting time of load test: $starting_time"

cicada-distributed run

ending_time=`date`

echo "Ending time of load test: $ending_time"