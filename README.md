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

# How to test the api call?
To call the POST method with a video file, you can execute the post.sh script in testapi folder using the path to your file as below:  
```
. ./testapi/post.sh sample.mp4
```
You will get a json output that contains an id (database row id), height and width of video images, frame count and frame per sercond of your video in addition to timestamp that shows the time your file is uploaded to the server.  
To retreive this data from the database use the returned id of POST request to call the GET method by executing the get.sh script in the testapi folder:
```
. ./testapi/get.sh {id}
```
