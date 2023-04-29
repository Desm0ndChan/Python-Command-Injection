IMAGE_NAME=myapp
.SILENT:
.PHONY: build run clean

build:
	docker build --rm -t $(IMAGE_NAME) .

run:
	docker run -it -p 8080:8080 --rm $(IMAGE_NAME)

debug:
	docker run -it -p 8080:8080 -v "${PWD}/app:/app" --rm $(IMAGE_NAME) /bin/bash

clean:
	docker image rm $(IMAGE_NAME) 
	docker system prune
	docker image prune -f