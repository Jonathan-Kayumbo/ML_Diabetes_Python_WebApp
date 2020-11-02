# ML_Diabetes_Python_WebApp

Detect if someone has diabetes using Machine Learning and Python

## Requirements

  - Jenkins instance
  - Kubernetes Cluster 
  - Ansible


## Usage

This project is focus on three thing 

   1: A CI/CD pipeline that:

    - builds , 
    - deploy image to DockerHub or any Container Registry of your choce 
    - Then pull the image and deploy it to kubernetes cluster with 2 replicas

   2: Machine Learning Project to detect if user has Diabetes *in percentage* or NOT , this is written in Python 

        - In this App we are using Streamlit to create a user responsive GUI , where user can input data by adjusting age , skin_thickness an so on to see if they have diabetes or NOT 

## Build local

If you want to build this locally , you only need docker running on your system *inux * and run the following commands to build and run application 

     # docker build -t <image_name:tag> .
     # ocker container run -d -p 9000:8501 <image_name:tag> 
 
     Then you can visit http:localhost:9000 
     
This project is continously improved , you cna use it in cloud inviroment too, like build in Azure CI/CI pipeline , deploy in Azure Container Registy and deploy WebApp in Azure k8s cluster 
 
 
