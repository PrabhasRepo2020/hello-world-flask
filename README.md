# hello-world-flask
This repository is for learning &amp; teaching purpose with demos 

Please follow below steps to run this handson example in your local machine.

1. Install _python3_ and _Visual Studio Code_ on your work station/Laptop
2. Use the below command to get the flask module
    **pip install flask**
    Just in case if pip is not found, please use the command, **python3 get-pip.py**
3.  Open helloworld/helloWorld-flask.py file in VS code to explore which makes use of flask module and used Flask class along with below three functions
	1. redirect
	2. url_for
	3. render_template
4.  Run the file in VS Code terminal using the command, **python3 helloWorld-flask.py**
5.  Once the flask application is started, validate using the below URLs

The IP address (192.168.0.121) in below URLs listed will vary as it is dynamically generated and so please carefully copy from your terminal where you start the python app.
* http://192.168.0.121:80/
* http://192.168.0.121:80/courses
* http://192.168.0.121:80/primary/<give any number like 3, 5, 15, 19 and check the results - age of sudent>
* http://192.168.0.121:80/secondary/<give any number like 3, 5, 15, 19 and check the results - age of student>
* http://192.168.0.121:80/passingscore
* http://192.168.0.121:80/passingscore/<give any number between 0 and 100 which is marks or score>
* http://192.168.0.121:80/findgrade/<give any number like 3, 5, 15, 19 and check the results - age of student>
   * Note: _the last URL  will redirect based on the number value given_

Please follow below steps to create a docker image of this python flask code.

* If you want to try out the existing image from Dockerhub image repository, run the existing image by running the below command,
   * docker run -dit -p 9000:80 --name mydemoflask prabhakarnatesan/myflaskdemo
   * once the container is started successfully, try out the above commands replacing host:port as in below sample,
      * http://0.0.0.0:6060/findgrade/3 

* If you like to perform handson containerizing, please follow steps below,
   * Once you have cloned this repo, enter the path **hello-world-flask/helloworld/** and execute below command to build your image using the Dockerfile.
      * docker build -t helloworld-flask-demo:1.0 . 
   * Set your newly built image version to the "latest" tag.
      * docker tag helloworld-flask-demo:1.0 helloworld-flask-demo:latest
   * Run the image from your local docker lib using the below command
      * docker run -dt -p 9000:80 --name myflask helloworld-flask-demo   

