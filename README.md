flowchart LR
    subgraph External
      API[(Weather API)]
    end

    subgraph Azure
      ADF[Azure Data Factory<br/>Copy + Notebook]
      KV[(Key Vault<br/>weatherApiKey, databricksAccessToken)]
      DL[(Data Lake Gen2<br/>raw-data · staging · transformed)]
      DBX[Azure Databricks<br/>Workspace + Cluster]
    end

    subgraph BI
      PBI[Power BI]
    end

    API -->|current.json?q=City&key=...| ADF
    KV  -. secrets .-> ADF
    ADF -->|Copy (REST → Binary)| DL
    ADF -->|Run Notebook| DBX
    DBX -->|Parquet| DL
    DL  -->|Transformed| PBI
