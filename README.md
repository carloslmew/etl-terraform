# etl-terraform
This repository has the code to create a simple ETL in GCP.

## Prerequisites
* Setup a GCP account
* Install Terraform
* Activate Cloud Function API

## Installing
Just run the following commands

* Clone the project
```
git clone https://github.com/carloslmew/etl-terraform.git
```
* Change to the directory
```
cd etl-terraform
```
* Export your service account as a environment variable
```
export GOOGLE_APPLICATION_CREDENTIALS=YOUR-PATH-HERE.json
```
* Init Terraform
```
terraform init
```
* Check the plan of resources creation
```
terraform plan
```
* Validate the configuration file
```
terraform validate
```
* Apply the configuration and create the resources
```
terraform apply
```
* Verify your resources in GCP
* Destroy the resources
```
terraform destroy
```

## Acknowledgments
This solution was based on this guide: [Get Started - Google Cloud](https://learn.hashicorp.com/collections/terraform/gcp-get-started) guide, containing Terraform configuration files to create resources on GCP.

Follow the step-by-step here: [GCP: Simple data pipeline](https://protective-opossum-8c5.notion.site/GCP-Simple-data-pipeline-2c02ea8ae6c64cd88813276787a3f551)

