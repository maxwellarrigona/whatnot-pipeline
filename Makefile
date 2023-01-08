help: 
		@echo " build:     			    Build the docker images from the docker-compose file"
		@echo " start:     			    Start the containers created from the docker-compose file"
		@echo " start-run:			    Create and start containers for airflow"
		@echo " az-login:				    Login into Azure from inside the container"
		@echo " stop-airflow:			  Stops containers created from the docker-compose file"
		@echo " init-terraform:		  Initialize terraform configuration"
		@echo " environment:			  Build the Azure Cloud infra using terraform"
		@echo " destroy-infra:			Destroy the Azure Cloud infra created using terraform"
		@echo " terraform-config:		Create the configuration.env file from terraform output.tf file"
		@echo " remove-airflow:		  Remove containers created by build/start-run command"

init-terraform:
		cd ./terraform && terraform init
environment:
		cd ./terraform && terraform apply
terraform-config:
		cd ./terraform && terraform output > ../airflow/tasks/configuration.env
destroy-infra:
		cd ./terraform && terraform destroy
build:
		sudo docker-compose build
start:
		sudo docker-compose start
start-run:
		sudo docker-compose up -d
az-login:
		sudo sh az_login.sh
stop-airflow:
		sudo docker-compose stop
remove-airflow:
		sudo docker-compose down
