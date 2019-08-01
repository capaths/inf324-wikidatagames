# build frontend
FROM node:lts-alpine as build-stage

WORKDIR /app

COPY webapp/frontend/package*.json ./

RUN npm install

COPY webapp/frontend/ ./

RUN npm run build

# production
FROM ubuntu:latest as production-stage

COPY --from=build-stage /dist /app/dist

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential

WORKDIR /app

COPY webapp/requirements.txt ./

RUN pip3 install -r requirements.txt

#COPY webapp/backend ./
COPY webapp/run.py ./

ENTRYPOINT ["python3"]
CMD ["run.py"]
