#!/bin/bash
echo "Please hold for the authentication code"
if docker exec -ti -u airflow sunglasseshubetl_airflow-worker_1 az login ; then
    echo "Login successful"
elif docker exec -ti -u airflow sunglasseshubetl-airflow-worker-1 az login ; then
    echo "Login successful"
else
    echo "Seems like an error ocurred. Please use this command:"
    echo "docker exec -ti -u airflow [name_of_the_airflow_worker_container] az login"
fi

# If this script doesn't work use this command:
#   docker exec -ti -u airflow name_of_the_airflow_worker_container az login
# To get the name of the airflow worker container use "docker ps"
