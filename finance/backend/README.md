# README

This is a Work In Progress.

As of 26/1/2021: End goal is to produce an interactive graph like Yahoo Finance, which shows Open, Close, High, Low, for a company.

To Run

```
docker run -p 6379:6379 -it --rm redislabs/redistimeseries
```

and then 

```
docker ps
```

to find the docker container name

```
docker exec -it <name> sh
```

to run an interactive bash environment in the container

Finally, run normal redis commands to check if the data is entered correctly in Redis





php custom plugin

strapy, react and gatsby

prolog