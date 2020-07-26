# Apache Spark powered by Docker

This repo contains a simple example of PySpark job running on an Apache Spark cluster powered by Docker containers.

The Docker image is published by Bitnami: https://github.com/bitnami/bitnami-docker-spark

## Spark cluster init and tests

First of all we need to start the Spark cluster, the current configuration is based on the `docker-compose.yml` offered by Bitnami but the parameters can be adjusted depending on your needs.

This cluster is composed by:
- 1 master node
- 2 worker nodes (with 1 GB of memory each)

To start the cluster type the command:

```
make spark-init
```

Before submitting your job, set the environment variable `JOB_NAME` with the .py file which has your Spark script (including folder reference), by default this variable value is set as `src/spark.py`.

After the cluster is up and running, open a separate terminal session and type the following command:

```
make spark-submit
```

The command above triggers the Spark job from the master node.

In case of need to interact with the cluster there is an additional command to access the master node via bash shell, this approach can be used to improve troubleshoot and testing. To access the master node type:

```
make spark-shell
```

# Apache Spark documentation

For more information have a look in the official Apache Spark documentation.

https://spark.apache.org/docs/latest/sql-getting-started.html