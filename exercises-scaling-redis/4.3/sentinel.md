# Sentinell.conf

create a `sentinell.conf` file with the following:

```
port 5000

sentinel monitor myprimary 127.0.0.1 6379 2

sentinel down-after-milliseconds myprimary 5000

sentinel failover-timeout myprimary 60000
```
Note: as I am running it in docker, replaced `127.0.0.1` with `host.docker.internal`

port - The port on which the Sentinel should run

 

sentinel monitor - monitor the Primary on a specific IP address and port. Having the address of the Primary the Sentinels will be able to discover all the replicas on their own. The last argument on this line is the number of Sentinels needed for quorum. In our example - the number is 2.

sentinel down-after-milliseconds - how many milliseconds should an instance be unreachable so that it’s considered down

sentinel failover-timeout - if a Sentinel voted another Sentinel for the failover of a given master, it will wait this many milliseconds to try to failover the same master again

## Next Step
Make 2 more copies of this file - sentinel2.conf and sentinel3.conf and edit them so that the PORT configuration is set to 5001 and 5002, respectively

## Next Step
Run the following commands after connecting to one of the sentinels

```
# Provides information about the Primary
SENTINEL master myprimary

# Will give you information about the replicas connected to the Primary
SENTINEL replicas myprimary

# Will provide information on the other Sentinels
SENTINEL sentinels myprimary

# Provides the IP address of the current Primary
SENTINEL get-master-addr-by-name myprimary
```

# Docker
https://hub.docker.com/r/bitnami/redis-sentinel/
https://github.com/s7anley/redis-sentinel-docker
Problem facing is the sentinel is not registering/connecting to the primary cluster dockerised.