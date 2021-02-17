### Steps for running the code

1. Login to IBM Cloud CLI:  
```bash
ibmcloud login -a cloud.ibm.com -r eu-de -g Default
```
2. Configure Kubernetes cluster: 
```bash
ibmcloud ks cluster config --cluster <CLUSTERNAME>
```
3. Setting config: 
```bash
kubectl config current-context
```
4. Create image pull secret: 
```bash
kubectl create secret docker-registry regcred --docker-username=<USERNAME> --docker-password=<PASSWORD> --docker-email=<EMAIL> -n default
```
5. Create Deployment: 
```bash
kubectl create -f deployment.yaml
```
6. Create Service to expose the application: 
```bash
kubectl create -f service.yaml
```
7. Check Node external IP: 
```bash
kubectl get nodes -o wide
```
8. Check which port the application is exposed by the service: 
```bash
kubectl get service
```
9.  Open your application on http://"node-external-ip":"expose-port"

