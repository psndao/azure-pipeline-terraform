# 🌐 Azure Data Pipeline - Weather API → ADLS → Databricks → Power BI

Ce projet déploie une **pipeline complète** sur Azure avec Terraform :
- **Azure Data Factory** pour orchestrer
- **API Weather** comme source
- **Azure Data Lake Gen2** pour le stockage
- **Azure Databricks** pour la transformation
- **Power BI** pour la visualisation

## 🚀 Architecture
![Architecture](architecture.png)

## 📂 Structure
- main.tf : ressources principales
- variables.tf : variables
- providers.tf : providers
- outputs.tf : outputs
- databricks/notebooks/weather_transform.py : notebook PySpark
