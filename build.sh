#! /bin/bash
rm -rf /home/pi/Desktop/voltcraft-api/python-flask-api
java -jar /home/pi/Desktop/swagger-codegen-3.0.34/modules/swagger-codegen-cli/target/swagger-codegen-cli.jar generate \
  -i /home/pi/Desktop/voltcraft-api/api.yaml \
  -l python-flask \
  -o /home/pi/Desktop/voltcraft-api/python-flask-api
cd /home/pi/Desktop/voltcraft-api/python-flask-api
pip3 install -r requirements.txt