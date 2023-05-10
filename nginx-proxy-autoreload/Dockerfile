FROM nginx:alpine3.17

COPY ./configReloader.sh /usr/local/bin/configReloader.sh
COPY ./docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
COPY ./nginx.conf /etc/nginx/nginx.conf

RUN chmod +x /usr/local/bin/configReloader.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh
RUN rm -rf /etc/nginx/conf.d

RUN apk update && apk add inotify-tools bash

ENTRYPOINT [ "/usr/local/bin/docker-entrypoint.sh" ]
CMD ["nginx", "-g", "daemon off;"]