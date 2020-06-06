IMAGE_NAME = "pb2020-content-reader"

READER_MODE_REDDIT = "reddit"


build:
	docker build --rm --tag=$(IMAGE_NAME) .


run_reddit:
	$(MAKE) build
	docker run -e READER_MODE=$(READER_MODE_REDDIT) $(IMAGE_NAME)
