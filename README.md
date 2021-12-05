# final_project_funny_minds
This is my final project for the DevOps Cloud4 Bootcamp called Young Minds


This is my final individual project on the QA DevOps Boot Camp 

Minimum requirements for the final project are as follows: 
To create a multi-tier web application that demonstrates CRUD functionality.
To utilise containers to host and deploy your application.
To create a continuous integration (CI)/continuous deployment (CD) pipeline that will automatically test, build and deploy. 
This will showcase all the topics taught over a nine week bootcamp.
Project Planning Board - I have used the github project board. 
MySQL Database for Azure consisting of at least two tables that model a relationship
A Flask driven frontend service to host the web pages that will implement CRUD capability to retrieve information from this database
Automated unit testing using pytest in a CI/CD pipeline, implemented using Jenkins inside a Docker container
Use of git and GitHub with Jenkins to orchestrate development to the Azure VM

Implementation

Entity Identification
We have three entities
Young Mind
Jokes
Dojos
 
Relationship Identification
We have the following two relationships
Our young minds will share a joke 
Other young minds will reward the joke via Dojos
 
User stories

CREATE
As a user, I want to share/add jokes if they are not already on the app, so that they can add jokes or riddles on the app.
As a user, I want to see all jokes by other young minds from a relevant category, to view them simultaneously.
As a user, I want to add young minds if they are not already on the app,so that they can add jokes or riddles on the app.

READ
As a youngmind, I want to review my entries, so that I can see if my information is correct. 
As a youngmind, I want to change details (joke category/description) so that is information is always accurate 

UPDATE
As an youngmind, I want my details to be deleted when I don't want my details to be seen on their database. 

DELETE
As an youngmind, I want to review/change my details (name/joke) so that my information is correct.
Below are the following steps that were taken to execute the final project. 


Create a new repo on GitHub - add a readme file in it. 
Added public key to git hub from id_rsa.pub file (VSC) 
Command on VSC - 

sshkeygen
git clone git@github.com:ThakkarPurvi/final_project_young_minds.git
cd young_minds


Created a new project within my young minds repo on Github.

Started adding issues so that it can go to the kanban board on the project 


Assigned the issues to the right column 


Created 3 branches to work on the application 

feature/2/read_function
  	feature/3/Create_new_Young_Mind
  	feature/4/reward_function


Commands as below on VSC
git branch 
* master
git checkout -b dev
Switched to a new branch 'dev'
git checkout -b feature/3/Create_new_Young_Mind
Switched to a new branch 'feature/3/Create_new_Young_Mind'
git branch
  dev
* feature/3/Create_new_Young_Mind
  master
git checkout dev
Switched to branch 'dev'
git checkout -b feature/4/reward_function
Switched to a new branch 'feature/4/reward_function'
git branch
  dev
  feature/3/Create_new_Young_Mind
* feature/4/reward_function
  master
git checkout dev
Switched to branch 'dev'
git checkout -b feature/2/read_function
Switched to a new branch 'feature/2/read_function'
git branch
  dev
* feature/2/read_function
  feature/3/Create_new_Young_Mind
  feature/4/reward_function
  master
git checkout dev
Switched to branch 'dev'
git branch
* dev
  feature/2/read_function
  feature/3/Create_new_Young_Mind
  feature/4/reward_function
  master

git checkout master
git add .
git commit -m "exporting all folders and files to github"
git push




Created new pipeline project on jenkins 


Created a new webhook by going to GitHub project setting 


On my VSC switch to feature branch that I want to work on - 
command - 
git checkout feature/3/Create_new_Young_Mind
git add .
git commit -m "init jenkins files"
git push
git push --set-upstream origin feature/3/Create_new_Young_Mind

On the Jenkins portal, I clicked on the build now 



Add credentials and set the environment in all the files in the Jenkins folder on VSC


Go to Jenkins dashboard - click on - Manage Jenkins - Manage credentials 
On VSC add the below command to allow to run the application 
	sudo visudo  ------ a nano file will open ----- add the command on the last line 


On setup.sh file under install docker on line 11and 12 add the below command to give permission for Jenkins to have access to the portal
sudo usermod -aG docker jenkins
newgrp docker

On VSC run the below command 
sudo systemctl status jenkins
sudo systemctl restart jenkins

On jenkins portal - Build now 
On the new vm (swarm manager) run the following command 
curl https://get.docker.com | sudo bash - this will install docker on the swarm manager 
sudo docker swarm init
sudo docker node ls
sudo useradd -m -s /bin/bash jenkins_young_minds - this will create the user
sudo su - jenkins_young_minds - this will switch the user to jenkins_young_minds

On the DevJenkins run the following commands 
sudo su - jenkins_young_minds - this will switch the user to jenkins_young_minds
Ssh-keygen
cat .ssh/id_rsa.pub

Now copy the public key 

On the Deployment server run the following commands 
	mkdir .ssh
	ls 
ls -a
touch .ssh/authorized_keys
nano .ssh/authorized_keys

Nano window will open 
Paste the ssh key on the nano window and press Control X

On the DevJenkins run the following commands  -  ls .ssh
On the Deployment server run the following commands 
	cat .ssh/authorized_keys - this will generate a public key which should be the same as   the ssh key on the DevJenkins VM 
	ssh jenkins_young_minds@swarm-manager


Addes the below class on the models.py file in backend 

class YoungMind(db.Model):
  	id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    
jokes = db.relationship(Young_Mind, backref=‘young_mind’)
 
class Jokes(db.Model):
id = Column(db.Integer, primary_key=True)
    joke_Category= db.relationship(‘Category’)
    youngmind_id = db.Column(db.Integer, ForeignKey(‘young_Mind.id’), nullable=False)

Prioritised issues as per MOSCOW  based on 

MUST HAVE -  Vital feature for the project
SHOULD HAVE -  IMP feature but not vital for the project
COULD HAVE  - Nice to have in the project


All the issues were prioritized on MOSCOW and viability of the project in 

MVP - Minimum viable product
ST - Stretch Target


After completing the code and fixing error below is how the homepage  appeared where you can add new Young Mind


Below is how the homepage that appeared where you can Add Joke



Below is how the homepage that appeared where you can Update Young Mind











Below page will show you the jokes and new young minds that are added to the database. 


Testing stage 













Frontend Testing 



Backend Testing 













Jenkins view 





___________________This is the end of my Final Project __________________________



