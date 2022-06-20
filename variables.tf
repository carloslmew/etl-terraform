variable "project_id" {
  description = "Google Project ID."
  type        = string
}

variable "region" {
  description = "Google Cloud region"
  type        = string
  default     = "us-central1"
}

variable "dataset_id" {
  description = "BigQuery dataset"
  type        = string
  default     = "us-central1"
}

variable "table_id" {
  description = "BigQuery table id"
  type        = string
  default     = "us-central1"
}

variable "location" {
  description = "BigQuery location"
  type        = string
  default     = "us-central1"
}

variable "deletion_protection" {
  description = "Protection to delete resources"
  type        = string
}
