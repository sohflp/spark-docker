# Apache Spark + Jupyter notebook

This repository contains a basic setup to experiment and study Apache Spark with Python via Jupyter Notebooks.

## Init Spark container

To start Spark locally type the command:

```
make spark-init
```

## Submit Spark jobs

Before submitting your job, set the environment variable `JOB_NAME` with the .py file which has your Spark script (including folder reference), by default this variable value is set as `src/example_dataframe.py`.

After the cluster is up and running, open a separate terminal session and type the following command:

```
make spark-submit
```

## Check logs from container

Use the command below to access the logs:

```
make spark-logs
```

Here you can also find the URL to access the Jupyter notebook locally. See the example below for reference:

```
spark_1  |     To access the notebook, open this file in a browser:
spark_1  |         file:///home/jovyan/.local/share/jupyter/runtime/nbserver-7-open.html
spark_1  |     Or copy and paste one of these URLs:
spark_1  |         http://ced61f64b8bc:8888/?token=3738634afb37cc80120819eb0723329baea38328e8b27dee
spark_1  |      or http://127.0.0.1:8888/?token=3738634afb37cc80120819eb0723329baea38328e8b27dee
```

## Interact with Spark via shell

Type the command below:

```
make spark-shell
```

# Apache Spark documentation

For more information have a look in the official Apache Spark documentation.

https://spark.apache.org/docs/latest/sql-getting-started.html