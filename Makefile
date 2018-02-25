LOCAL_TEST_IMAGE=test_vol_dash_api

docker_test: docker_test_rebuild setup_postgres
	docker run $(LOCAL_TEST_IMAGE)
	docker stop postgres

docker_test_rebuild:
	find . -name \*.pyc -delete
	rm -rf .cache
	docker build -f Dockerfile_test . -t $(LOCAL_TEST_IMAGE)

setup_postgres:
	docker pull postgres:10.2
	docker run -d --rm \
		-e POSTGRES_PASSWORD=password \
		-e POSTGRES_USER=user \
		-e POSTGRES_DB=test_db \
		-p ""5432:5432"" \
		postgres:10.2