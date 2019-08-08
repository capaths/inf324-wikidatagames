# pre-production
FROM ubuntu:latest as production-stage

RUN apt-get update -y && apt-get install -y python3-pip python3-dev build-essential

COPY webapp/requirements.txt /app/
RUN pip3 install -r /app/requirements.txt

# build frontend
FROM node:lts-alpine as build-stage

WORKDIR /app

COPY webapp/frontend/package*.json ./

RUN npm install

COPY webapp/frontend/ ./

RUN npm run build

# production
FROM production-stage

COPY --from=build-stage /dist /app/dist

WORKDIR /app

COPY webapp/app ./app
COPY webapp/run.py ./

ENV ENV=prod
ENV PYTHONBUFFERED=0

ENTRYPOINT ["python3"]
CMD ["run.py"]
