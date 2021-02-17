### Steps for running the code

1. Login to IBM Cloud CLI:  
```bash
ibmcloud login -a cloud.ibm.com -r eu-de -g Default
```
2. Configure Kubernetes cluster: 
```bash
ibmcloud ks cluster config --cluster c0lvihhf03gpla7tro20
```
3. Setting config: 
```bash
kubectl config current-context
```
4. Create image pull secret: 
```bash
kubectl create secret docker-registry regcred --docker-username=abhikghosh --docker-password=BlackLenovo123 --docker-email=avik5324@gmail.com -n default
```
5. Create Deployment: 
```bash
kubectl create -f deployment.yaml
```
6. Create Service to expose the application: 
```bash
kubectl create -f service.yaml
```
7. We used NodePort type in the service yaml. Check Node external IP: 
```bash
kubectl get nodes -o wide
```
8. Check which port the application is exposed by the service: 
```bash
kubectl get service
```
9.  Open your application on http://<node-external-ip>:<expose-port>

