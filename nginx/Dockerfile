FROM nginx:stable-alpine

MAINTAINER Gildardo Adrian Maravilla Jacome

COPY app.conf /etc/nginx/conf.d/

ENTRYPOINT ["nginx", "-g", "daemon off;"]
