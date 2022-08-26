# Final project DfE Cloud Cohort
## Oxana Sidorova
### Speaking app
### 26.08.2022

## Overview
### 1. Project Management and Version Control
In the project was using Jira to track project using Agile Scrum methods.
<img width="1301" alt="Jira_1" src="https://user-images.githubusercontent.com/106552165/186744973-2008ec65-dc71-4c35-8977-a1c948bd5f96.png">
progress 
<img width="1043" alt="Jira_24 08" src="https://user-images.githubusercontent.com/106552165/186744919-16b1df4b-2ebf-4be4-9751-cd3aa26c3916.png">
progress
<img width="1300" alt="Jira_24:08" src="https://user-images.githubusercontent.com/106552165/186744939-9972ffef-e26b-4025-a33d-d759f4087e39.png">

### 2. Application
This project is presenting a basic web application using on the Flask web framework. 
This application - "speaking app" keeps track of two entities that have one to many relationship.
<img width="486" alt="ERG_Speaking_app" src="https://user-images.githubusercontent.com/106552165/186739479-148a3baf-12e1-40a3-bb7b-a1d6fee6df2d.png">

This application has only Create and read functionality.
https://drive.google.com/drive/folders/1c4inRwbSfTR7XQ48_nrsXVAA2mw5psWD?usp=sharing

The frontend aspect of the app use HTML templates to serve the web pages that allow to perform CR functionality with information from the database.

The backend - use SQLAlchemy to model and integrate with the database.

### 3. Database
The application interface with a separate database service- MySQL container.

### 4. Testing
???

### 5. Ci/Cd pipeline
Was creating a CI/CD pipeline that will automate the integration and deployment of new code.

The automation server - is Jenkins.
* Pipeline:
* Run unit tests.
* Build the Docker images.
* Push the Docker images to a registry.
* Deploy to a Swarm.
Every time the new code pushed to GitHub repository, the pipeline triggered - by using a GitHub Webhook.

### Ci\Cd Diagram

<img width="759" alt="CI:CD pipeline diagram" src="https://user-images.githubusercontent.com/106552165/186745587-3b76eaec-4923-4045-bebf-e346b0fe4eb5.png">

### An infrastructure diagram
Illustrating the cloud resources and how they network together.

<img width="840" alt="infrastructure diagram" src="https://user-images.githubusercontent.com/106552165/186749725-46ea03bd-2459-485b-b2ee-925e585deb2f.png">

## Deployment
The application is be deployed to a Docker Swarm hosted in the Azure cloud.

It consist one manager (Swarm1) node and one worker (Swarm2) node.

VM on Azure for the project

<img width="1141" alt="VM_my portal" src="https://user-images.githubusercontent.com/106552165/186746844-1cb4c8a6-0d82-4880-a7e8-cf691bb2f8bb.png">

## Deliverable

## Difficulties and errors

* project was pushed to a master branch in GitHub instead of main.
* the flask application doesn't have a Update and Delete functionality.
* Pycharm on my machine working very very slow. Need to get used to a different shell.

## Next Sprint improvements
* 


