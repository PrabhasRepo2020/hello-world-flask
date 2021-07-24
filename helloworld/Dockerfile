# init a base image (here I am using official Python image using Alpine Linux distro)
FROM python:3.10-rc-alpine3.14

# define a working directory
WORKDIR /hello-world-flask

# add the contents from the current directory into WORKDIR
ADD . /hello-world-flask
# run pip to install the dependencies of the flask app
RUN pip install -r requirements.txt
# command to start the container
CMD ["python","helloWorld-flask.py"]

