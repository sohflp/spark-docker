export PATH_DEPLOY=.deploy
export JOB_NAME=src/spark.py

# Check for specific environment variables
env-%:
	@ if [ "${${*}}" = "" ]; then \
		echo "Environment variable $* not set"; \
		exit 1; \
	fi

spark-init:
	@echo "make spark-init"
	docker-compose -f $(PATH_DEPLOY)/docker-compose.yml up

spark-submit: env-JOB_NAME
	@echo "make spark-submit"
	docker-compose -f $(PATH_DEPLOY)/docker-compose.yml \
		exec spark spark-submit $(JOB_NAME)

spark-shell:
	@echo "make spark-shell"
	docker-compose -f $(PATH_DEPLOY)/docker-compose.yml \
		exec spark /bin/bash