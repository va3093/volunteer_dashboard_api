LOCAL_TEST_IMAGE=test_vol_dash_api

docker_test: docker_test_rebuild
	docker run $(LOCAL_TEST_IMAGE)

docker_test_rebuild:
	find . -name \*.pyc -delete
	rm -rf .cache
	docker build -f Dockerfile_test . -t $(LOCAL_TEST_IMAGE)