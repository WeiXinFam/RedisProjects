FROM redis
COPY sentinell.conf /usr/local/etc/redis/
RUN chmod 777 -R /usr/local/etc/redis/
CMD [ "redis-server", "/usr/local/etc/redis/sentinell.conf", "--sentinel" ]