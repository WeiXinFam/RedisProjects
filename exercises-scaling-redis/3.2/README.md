# Saving a Snapshot

Let’s update this to a simplified hypothetical scenario where we want to save a snapshot if three keys have been modified in 20 seconds

1. Step 1
    The redis.conf file should specify a filename that will be used for the rdb file and a directive that will trigger the creation of a snapshot if 3 keys have been modified in 20 seconds, as described above.

    ```
    dbfilename my_backup_file.rdb
    save 20 3
    ```

2. Start container
    ```
    docker-compose up -d

    ```

3. Access the container
    ```
    docker-compose exec -it redis_snapshot bash
    redis-cli
    ```

4. Run the following commands
    ```
    > SET a 1

    > SET b 2

    > SET c 3
    ```

5. In `/data` folder in the docker container, you will see the rdb file created.

# AOF file

Modify your redis.conf file so that the server will log every new write command and force writing it to disk.
Be careful! We have a running server and we want this configuration to be applied without restarting it.

```
> CONFIG SET appendonly yes

> CONFIG SET appendfsync always
```

In order for these settings to be persisted to the redis.conf file we need to save them:
 
```
> CONFIG REWRITE
```
Bumping into `(error) ERR Rewriting config file: Permission denied` for this command.