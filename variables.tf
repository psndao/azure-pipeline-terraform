variable "resource_group_name" {
  description = "Nom du Resource Group"
  type        = string
  default     = "rg-data-pipeline"
}

variable "location" {
  description = "Région Azure"
  type        = string
  default     = "westeurope"
}

variable "weather_api_key" {
  description = "Weather API Key"
  type        = string
  sensitive   = true
}

variable "databricks_pat" {
  description = "Databricks PAT"
  type        = string
  sensitive   = true
}

variable "databricks_cluster_id" {
  description = "Cluster ID Databricks"
  type        = string
}
