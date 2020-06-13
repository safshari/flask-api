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


## Description
In this project, Flask python library is used to develop a web service application with a POST and a GET microservice. Using the POST request, a video file can be sent to the server running on the default port "0.0.0.0:5000".  
Given the video file, the server process it using OpenCV library and extracts the image resoluation, fps and number of frames in the file (these parameters are usefull for applying a ML or DL model in training stage and model design) and respond the user's request with a json file containing these information in addition to the recived timestamp.  
Also these information is recorded in a sqlite3 database created by the test-db docker images on the server.

## Improvement
The server side code does not completely handle different formats of request and response data and status codes.    
The server side code can be optimized for faster request and response actions.  
The  api can be changed to include users' lable for each video when uploading files and the server can be modified to add this lable in the database along with other extracted information for model training purpose.  
The video file can be processed to extract more meaningful and usefull information for ML and DL application.
