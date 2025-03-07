# Nuxt 3 builder
FROM node:lts AS builder
WORKDIR /app
COPY . .
RUN npm run build

# Nuxt 3 dev
# docker build --target deployjoy_front_dev -t registry.infra.kagescan.fr/s9-cloud-dev-nuxt:v0.2 .
# docker push registry.infra.kagescan.fr/s9-cloud-dev-nuxt:v0.2
# docker run -p 3000:3000 -it registry.infra.kagescan.fr/s9-cloud-dev-nuxt:v0.2
FROM node:lts AS deployjoy_front_dev
WORKDIR /app
COPY . .
CMD [ "npm", "run", "dev" ]

# Nuxt 3 production
FROM node:lts AS deployjoy_front_nuxt
WORKDIR /app
COPY --from=builder /app/.output  /app/.output

ENV NITRO_PORT=80
EXPOSE 80
CMD [ "node", ".output/server/index.mjs" ]


# docker build --target deployjoy_front_nuxt -t registry.infra.kagescan.fr/s9-cloud-nuxt:v0.2 .
# docker run -p 80:80 -it registry.infra.kagescan.fr/s9-cloud-nuxt:v0.2
# docker push registry.infra.kagescan.fr/s9-cloud-nuxt:v0.2