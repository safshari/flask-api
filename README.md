# How to build docker images?
There are two folders in this repo, api-docker and db-docker. Each of them contains a Dockerfile that will be used to create docker images.  
To build:  
  
```
cd api-docker
docker build -t rest-api:latest .
cd ..
cd db-docker
docker build -t test-db:latest .
cd ..
```

# How to run images?
Both of the images will run using docker-compose.  
To run:
  
```
UID=${UID} GID=${GID} docker-compose up
```

