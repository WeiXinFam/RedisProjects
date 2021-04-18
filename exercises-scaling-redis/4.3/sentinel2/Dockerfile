FROM redis
COPY sentinel2.conf /usr/local/etc/redis/
RUN chmod 777 -R /usr/local/etc/redis/
CMD [ "redis-server", "/usr/local/etc/redis/sentinel2.conf", "--sentinel" ]