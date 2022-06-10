# Flask API in AWS
Flask API in AWS


- Tools used in configured the python flask api are docker, ansible, dockerhub, jenkins, aws

- Python code is have single GET api (flask_api.py) and it consists of unit test cases (flask_api_test.py)

Server 1:
- We have Jenkins in EC2 Instacne which configured from AWS console and we have Ansible to deploy in server 2
- http://54.226.218.37:8080/job/FlaskAPI/
- admin/admin
Server 2:
- We have Dokcer configured here to build the images from docker hub
- http://3.91.38.115:8001/getname

Resources refered:
- https://flask-restful.readthedocs.io/en/latest/quickstart.html#a-minimal-api
- https://flask.palletsprojects.com/en/2.1.x/testing/
- https://docs.docker.com/language/python/build-images/


pip3 install Flask

pip3 install flask-restful

pip3 install pytest

pip3 install requests
