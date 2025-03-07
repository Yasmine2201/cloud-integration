# Nuxt 3 builder
FROM node:22 AS builder
WORKDIR /app
COPY . .
RUN npm ci
RUN npm run build

# Nuxt 3 dev
# docker build --target deployjoy_front_dev -t registry.infra.kagescan.fr/s9-cloud-dev-nuxt:v0.2 .
# docker push registry.infra.kagescan.fr/s9-cloud-dev-nuxt:v0.2
# docker run -p 3000:3000 -it registry.infra.kagescan.fr/s9-cloud-dev-nuxt:v0.2
FROM node:22 AS deployjoy_front_dev
WORKDIR /app
COPY . .
CMD [ "npm", "run", "dev" ]

# Nuxt 3 production
FROM node:22 AS deployjoy_front_nuxt
WORKDIR /app
COPY --from=builder /app/.output  /app/.output
ENV NITRO_PORT=8008
EXPOSE 8008
CMD [ "node", ".output/server/index.mjs" ]


# docker build --target deployjoy_front_nuxt -t registry.infra.kagescan.fr/s9-cloud-nuxt:v0.4 .
# docker run -p 8008:8008 -it registry.infra.kagescan.fr/s9-cloud-nuxt:v0.4
# docker push registry.infra.kagescan.fr/s9-cloud-nuxt:v0.4