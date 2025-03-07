# cloud-integration

Nous avons mis en place un registry public temporaire : `registry.infra.kagescan.fr`.

```sh
# Reset minikube
minikube delete
minikube start

# (ré-)Installer istio (adapter selon votre machine)
~/istio/bin/istioctl install --set profile=demo -y

# Cloner ce repo : 
git clone https://github.com/Yasmine2201/cloud-integration.git

# Lancement de la bdd
minikube kubectl -- apply -f kubernetes/namespace.yml
minikube kubectl -- apply -f kubernetes/postresql/

# (Bien attendre postgres avant de démarrer app)
minikube kubectl -- apply -f kubernetes/app/

# Lancer le tunnel vers ingress.
minikube service istio-ingressgateway -n istio-system
```