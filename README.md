prerequistes

k8s cluster
setup steps - commands

install helm
helm repo add aqua https://aquasecurity.github.io/helm-charts/
helm repo update
helm install trivy-operator aqua/trivy-operator --namespace trivy-system --create-namespace --version 0.23.3