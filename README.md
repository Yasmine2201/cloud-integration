# cloud-integration

Nous avons mis en place un registry public temporaire : `registry.infra.kagescan.fr`.

```sh
cd landing
docker build -t registry.infra.kagescan.fr/s9-cloud-landing .*
docker push registry.infra.kagescan.fr/s9-cloud-landing
cd ..
```


```sh
# Déploiement sur minikube
minikube delete
minikube start
./istioctl install --set profile=demo -y
kubectl create namespace joy
kubectl apply -f postresql/ -n joy
# Bien attendre pour chaque déploiement que tout est bien démarré
kubectl apply -f app/auth.yaml -n joy
kubectl apply -f app/publication.yaml -n joy
kubectl apply -f app/profile.yaml -n joy
kubectl apply -f app/istio.yaml -n joy
minikube service istio-ingressgateway -n istio-system
```