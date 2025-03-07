#!/bin/bash

TAG=v1.0
eval $(minikube docker-env)

cd apis
docker build --target deployjoy_api_auth -t registry.infra.kagescan.fr/s9-cloud-auth:$TAG .
docker build --target deployjoy_api_publication -t registry.infra.kagescan.fr/s9-cloud-publication:$TAG .
docker build --target deployjoy_api_profile -t registry.infra.kagescan.fr/s9-cloud-profile:$TAG .
cd ..

cd frontends/frontend_service
docker build --target deployjoy_front_nuxt -t registry.infra.kagescan.fr/s9-cloud-nuxt:$TAG .
cd ../..

#docker push registry.infra.kagescan.fr/s9-cloud-auth:$TAG
#docker push registry.infra.kagescan.fr/s9-cloud-publication:$TAG
#docker push registry.infra.kagescan.fr/s9-cloud-profile:$TAG