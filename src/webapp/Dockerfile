# build
FROM node:lts-alpine as build-stage

WORKDIR /app

COPY webapp/package*.json ./
COPY webapp/babel.config.js ./
COPY webapp/postcss.config.js ./
COPY webapp/tsconfig.json ./
COPY webapp/tslint.json ./

RUN npm install

COPY webapp/public/ ./public/
COPY webapp/src/ ./src/

RUN npm run build

# production
FROM nginx:stable-alpine as production-stage

COPY --from=build-stage /app/dist /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
