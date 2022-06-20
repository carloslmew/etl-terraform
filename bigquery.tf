resource "google_bigquery_dataset" "default" {
  dataset_id = var.dataset_id
  location   = var.location

  labels = {
    env = "default"
  }
}

resource "google_bigquery_table" "ds_salaries" {
  dataset_id = google_bigquery_dataset.default.dataset_id
  table_id   = var.table_id

  labels = {
    env = "default"
  }
}
