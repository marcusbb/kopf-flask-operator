# Kubernetes Operator for a 2 tier app

The premise of this project is to show some conceptual example of how you may build an operator for your application python Flask application.  

## Dependencies 

### Kopf
[kopf](https://kopf.readthedocs.io/en/stable/) python based operator framework.  This gives us the base of how we can build hooks into Kubernetes.

This is mainly demonstrative of how you can install something using an operator, but can be extended to many other uses cases of maintaining continuity past day 0.

### Helm
Why Helm? https://helm.sh/

- It's ubiquitous 
- It works 
- You are short on time converting or building a deployment mechanism for your favourite DB (or any other software packaged with Helm)

In this case the operator is wrapping Helm to use it as a convenitent installation mechanism for a Postgres.


## Pre-requisites

Helm - this is really part of the demonstration to show that you can wrap Helm into your operator

MacOs
```
brew install helm
```
Or on your preferred system of choice https://helm.sh/docs/intro/install/

Install Dependencies
```
pip install -r requirements.txt
```

Install Minikube - this is optional but for testing is quick and painless.  https://minikube.sigs.k8s.io/docs/start/

I tested everything locally using minikube on Docker.  Feel free to try this out on a full k8s setup!  Helm and the kubernetes client will automatically pick up your KUBE_CONFIG. 


## Operating

All relevant code is in [flask-postgres-operator.py](./flask-postgres-operator.py)
This is a realitively naive demonstration, for the most part just demonstrating the mechanics of the operator.

Run the operator using kopf command line.  There is some great documentation on 
```
kopf run flask-postgres-operator.py [--verbose]
```