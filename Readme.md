# Pipedrive Task

## Getting started
Pipedrive Challenge - A Test Task for Pipedrive

This is a project that uses both Github's and Pipedrive's APIs to:

Query a given user's gists

Create a deal in Pipedrive for each of those gists
The relevant info to create a deal used is the "owner id"


Periodically check for new gists using a web endpoint

## Part I

It was developed using python, Flask to define interfaces for API methods and VS code as my IDE;
#How to run the application
#Activate the environment variable

- python -m venv pipedrive-env

- source pipedrive-env/bin/activate

-  git clone https://github.com/dubbeltech/pipe.git 

- export FLASK_APP=project/app
- flask run

we can access the application at 127.0.0.1:5000 or localhost:5000

To get an output 127.0.0.1:5000/<username> or localhost:5000/<username>
  
You can access mine using 127.0.0.1:5000/dubbeltech

The Github GET method username field accepts a username to retrieve available public gists for that user and also creates a Pipedrive deal for each gist.

The username will be saved on lastSeen for periodic checks (every three hours) to see if any new gists have been created since the last visit
  
## Part II
The pre-requisite:
  Have an AWS account
  create an EC2 instance with ubuntu AMI
  Configure VPC, Subnet and Security Group; allow port 5000 to your IP address for security layer.
  
The Github Actions CI/CD pipeline deploy the project and to aws cloud:
  Configure Github Actions Environment variable and deploy keys:
  - AWS private key (pem key)
  - Hostname (ip4 address)
  - User name (ubuntu)
  - deploy keys (ssh key-gen public key from EC2 instance)
  
 To deploy the project:
 click on Action tab and run the pipeline
  
## Project Tools:
- python 3.*
- Githun Actions
- Docker


## Known Issues:
The pipeline breaks if there are no already containers in the pipeline.