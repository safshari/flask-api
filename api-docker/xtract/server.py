from flask import Flask, request,flash
import json
from flask_session import Session
from werkzeug.utils import secure_filename
import logging
import os
import cv2
import uuid 
import sqlite3
from sqlite3 import Error
from datetime import datetime
import magic

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "db/test.db")
mime = magic.Magic(mime=True)
app = Flask('myAPI')

class MyAPI(object):    
    def __init__(self):
        print("initiated")
        
      
    def run(self):  
        @app.route('/getLog/<id>', methods=['GET'])
        def getLog(id):
            try: 
                conn = sqlite3.connect(db_path)
                sql = ''' SELECT * FROM test WHERE id=? '''
                cursor = conn.cursor()
                cursor.execute(sql, (id,))
                field_name = [field[0] for field in cursor.description]
                values = cursor.fetchone()
                
                if(values is not None):
                   
                    data = dict(zip(field_name, values))
                else:
                    data = {"Status": "Not Found"}
                conn.commit()
                conn.close()
                
                response = app.response_class(
                    response= json.dumps(data),
                    status=200,
                    mimetype='application/json'
                    )  

                return response 


            except Error as e:
                print("Error ", e)
                data = {
                    "Status" : "Failed to connect to db"   
                }
                response = app.response_class(
                    response=json.dumps(data),
                    status=200,
                    mimetype='application/json'
                    )  
                return response 
            

            
        
        @app.route('/sendVideo', methods=['POST'])
        def sendVideo():
    
            if 'file' not in request.files:

                data = {
                    'Status': 'Wrong request!'
                   
                }
                
                response = app.response_class(
                    response=json.dumps(data),
                    status=200,
                    mimetype='application/json'
                    )  
                return response
            
            file = request.files['file']
            if file.filename == '':
                data = {
                    'Status': 'No file selected!'
                   
                }
                
                response = app.response_class(
                    response=json.dumps(data),
                    status=200,
                    mimetype='application/json'
                    ) 
                return response
            
            else:
                # parse the file
                filename = secure_filename(file.filename)
            
                dir = './video_files'

                if not os.path.exists(dir):
                    os.mkdir(dir)
                file.save(os.path.join(dir, filename))
                file_check = mime.from_file(os.path.join(dir, filename))
                if(file_check.find('video') != -1 ):
                    
                    cv2video = cv2.VideoCapture(filename)
                    height = cv2video.get(cv2.CAP_PROP_FRAME_HEIGHT)
                    width  = cv2video.get(cv2.CAP_PROP_FRAME_WIDTH) 
                    framecount = cv2video.get(cv2.CAP_PROP_FRAME_COUNT) 
                    frames_per_sec = cv2video.get(cv2.CAP_PROP_FPS)
                    
                
            


                    ##insert to db
                    try: 
                        conn = sqlite3.connect(db_path)
                        id = str(uuid.uuid1())
                        dateTime = datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")
                        sql = ''' INSERT INTO test (id, height, width, framecount, fps ,timestamp) VALUES( ?, ?, ?, ?, ?, ?) '''
                        cursor = conn.cursor()
                        cursor.execute(sql, ( id, height, width, framecount, frames_per_sec ,dateTime))
                        conn.commit()
                        conn.close()
                        data = {
                        'Status': 'Succeed',
                        'id' : id,
                        'res_height': height,
                        'res_width': width,
                        'framecount' : framecount,
                        "frame_per_second": frames_per_sec
                        }
                    except Error as e:
                        print("Error ", e)
                        data = {
                            "Status": "Failed to connect to db"
                        }
                    #response
                   
                    response = app.response_class(
                    response=json.dumps(data),
                    status=200,
                    mimetype='application/json'
                    ) 
                    return response
                
                else:
                    os.remove(os.path.join(dir, filename))
                    data = {
                        'Status': 'Selected file is not a video file!'
                      
                    }
                    response = app.response_class(
                    response=json.dumps(data),
                    status=200,
                    mimetype='application/json'
                    ) 
                    return response

        
            
    

        



    


    ## API resource path


    


if __name__ == '__main__':
    

    myAPI = MyAPI()
    myAPI.run()
    
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
    
