FROM redis
COPY sentinel3.conf /usr/local/etc/redis/
RUN chmod 777 -R /usr/local/etc/redis/
CMD [ "redis-server", "/usr/local/etc/redis/sentinel3.conf", "--sentinel" ]