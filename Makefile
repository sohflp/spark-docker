export JOB_NAME?=src/example_dataframe.py

# Check for specific environment variables
env-%:
	@ if [ "${${*}}" = "" ]; then \
		echo "Environment variable $* not set"; \
		exit 1; \
	fi

spark-init:
	@echo "Init Jupyter / Spark"
	docker-compose -f docker-compose.yml up -d spark

spark-logs:
	@echo "Get Docker logs"
	docker-compose -f docker-compose.yml logs spark

spark-submit: env-JOB_NAME
	@echo "make spark-submit"
	docker-compose -f docker-compose.yml exec spark \
		spark-submit $(JOB_NAME)

spark-shell:
	@echo "make spark-shell"
	docker-compose -f docker-compose.yml exec spark \
		/bin/bash