How to start Kafka and Zookeeper:
 - `docker-compose up -d`
 - Running the command above should start Kafka and Zookeeper in the background. 

How to check that the containers are running:
 - `docker ps` 
 - The command above prints all of the running docker containers, I expect to see a container for Kafka and one for Zookeeper running.

Now in the same directory:
To consume messages from a topic called `testr`:

```
docker-compose exec -it kafka  /opt/bitnami/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic testr --from-beginning
```

The above command starts a kafka consumer using the install JVM and binaries inside of the running Kafka container. The Topic name is `testr` and I want to start from the beginning of the topic. 

Now in a different console but the same directory:
```
docker-compose exec -it kafka  /opt/bitnami/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic testr

HELLO-WORLD!
```
 - This command will start up a Kafka producer insider of the container. Once the produce is up I can type any text I want into the console and see it appear in the console that is running my consumer!