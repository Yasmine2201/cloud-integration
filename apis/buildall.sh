#!/bin/bash

TAG=v0.2

docker build --target deployjoy_api_auth -t registry.infra.kagescan.fr/s9-cloud-auth:$TAG .
docker build --target deployjoy_api_publication -t registry.infra.kagescan.fr/s9-cloud-publication:$TAG .
docker build --target deployjoy_api_profile -t registry.infra.kagescan.fr/s9-cloud-profile:$TAG .

docker push registry.infra.kagescan.fr/s9-cloud-auth:$TAG
docker push registry.infra.kagescan.fr/s9-cloud-publication:$TAG
docker push registry.infra.kagescan.fr/s9-cloud-profile:$TAG