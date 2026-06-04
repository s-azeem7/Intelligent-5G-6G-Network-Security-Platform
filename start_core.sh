#!/bin/bash



echo " Starting 5G Security Platform on Kubernetes..." 



kubectl apply -f amf-deployment.yaml

kubectl apply -f nrf-deployment.yaml

kubectl apply -f ausf-deployment.yaml

kubectl apply -f smf-deployment.yaml



echo " Checking pods..." 

kubectl get pods



echo " Checking services..." 

kubectl get svc



echo " System deployed successfully on k3s"
