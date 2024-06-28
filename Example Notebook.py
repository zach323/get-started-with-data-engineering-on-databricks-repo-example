# Databricks notebook source
# MAGIC %md
# MAGIC ### This is an example
# MAGIC This notebook creates a dataframe with some sample data that can be used for a quick visualization.

# COMMAND ----------

data = [[1, "Elia"], [2, "Teo"], [3, "Fang"]]
sdf = spark.createDataFrame(data, schema="id LONG, name STRING")
display(sdf)

# COMMAND ----------

# diff for commit


# COMMAND ----------

print("Welcome to Databricks for Data Engineering")

# COMMAND ----------

# MAGIC %sql
# MAGIC select date_format(current_date(), "d MMM yyyy");

# COMMAND ----------

# MAGIC %md
# MAGIC # heading 1
# MAGIC ## heading 2
# MAGIC ### heading 3
# MAGIC
# MAGIC * Item 1
# MAGIC 1. Item 2
# MAGIC 1. Item 3
# MAGIC 1. Item 25
# MAGIC
# MAGIC [Google](www.google.com)
# MAGIC
# MAGIC **BOLD TEXT**
# MAGIC *ITALIC*
# MAGIC
# MAGIC
