FROM node:8.15.0

COPY . /code/
WORKDIR /code/

## Proxy
ENV HTTP_PROXY 'http://89.167.129.32:80'
ENV http_proxy 'http://89.167.129.32:80'
ENV HTTPS_PROXY 'http://89.167.129.32:80'
ENV https_proxy 'http://89.167.129.32:80'
ENV NO_PROXY 'localhost, 127.0.0.0/8, 127.0.0.1, 10.*, 172.17.0.1, 0.0.0.0, 0.0.0.0/8, 0.0.0.0/5'
ENV no_proxy 'localhost, 127.0.0.0/8, 127.0.0.1, 10.*, 172.17.0.1, 0.0.0.0, 0.0.0.0/8, 0.0.0.0/5'

RUN npm install webpack -g
RUN npm install
#RUN npm run dev

EXPOSE 8080