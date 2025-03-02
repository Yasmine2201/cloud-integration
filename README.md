# cloud-integration

Nous avons mis en place un registry public temporaire : `registry.infra.kagescan.fr`.

```sh
cd landing
docker build -t registry.infra.kagescan.fr/s9-cloud-landing .*
docker push registry.infra.kagescan.fr/s9-cloud-landing
cd ..
```