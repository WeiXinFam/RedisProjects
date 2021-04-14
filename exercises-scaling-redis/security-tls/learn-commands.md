# Starting Up Redis

## with TLS flags
One way you can enable TLS support is by adding the TLS flags to the redis-server startup. You can enable the TLS port and disable the regular TCP port, point to the certificate, key and CA cert.
```
redis-server --tls-port 6379 --port 0 --tls-cert-file /etc/certs/server.crt --tls-key-file /etc/certs/server.key --tls-ca-cert-file /etc/certs/ca.crt
```

## with TLS configuration
The docker container has also had the default redis.conf file copied to ```/usr/local/etc/redis/redis.conf```, but in the previous command we did not utilize it.
Let's try to enable the same TLS settings that we did above in this config and then start Redis with TLS support that way.
```
redis-server /usr/local/etc/redis/redis.conf
```

# Check Server is TLS
```
docker-compose exec redis_tls bash

redis-cli --tls --cert /etc/certs/client.crt --key /etc/certs/client.key --cacert /etc/certs/ca.crt
```


