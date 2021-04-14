# Exercise: Enabling TLS in Redis

## Requirements

- docker
- docker-compose
- internet connection

## Starting Environment

```
docker-compose up -d
```

### Connect to the Environment
```
docker-compose exec redis_tls bash
```

### To view the certs

```
ls /etc/certs
```

## Stopping Environment

After completing the exercises

```
docker-compose down
```

