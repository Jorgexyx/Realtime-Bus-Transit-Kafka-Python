# Setting Up 
run

```kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic liveBusData```

# Misc. Information
## LocalHost
Default is localhost:2181

## Creating a Kafka Topic CLI
```kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test```

## Listening to a Kafka Producer
```kafka-console-consumer --bootstrap-server localhost:9092 --topic liveBusData --from-beginning```

