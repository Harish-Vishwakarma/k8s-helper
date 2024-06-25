This is flask app

This project aims give more information on k8s, such as vuln information od pod and more ( still in progress )


prerequistes

k8s cluster
setup steps - commands

install helm
helm repo add aqua https://aquasecurity.github.io/helm-charts/
helm repo update
helm install trivy-operator aqua/trivy-operator --namespace trivy-system --create-namespace --version 0.23.3


Intrested induviduals are welcome to contribute.
Have more ideas/ suggestion  find me on : https://www.linkedin.com/in/harish-achar/
