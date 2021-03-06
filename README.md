# LIVE LA METRO TRANSIT WITH KAFKA, REACT, PYTHON


![Preview of react app](images/preview.png)

# Running Script
Run python script with the bus route number
ex.) in 1 terminal run ```python3.7 main.py 45```

in another terminal run ```python3.7 main.py 233```

# Setting Up 
run

```kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic liveBusData```

# Misc. Information
## LocalHost
Default is localhost:2181

## Run zookeeper before running kafka
```
zookeeper-server-start /usr/local/etc/kafka/zookeeper.properties
```

## Start the kafka server
```
kafka-server-start /usr/local/etc/kafka/server.properties
```

## Creating a Kafka Topic CLI
```kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test```

## Listening to a Kafka Producer
```kafka-console-consumer --bootstrap-server localhost:9092 --topic liveBusData --from-beginning```

## Installing kafka on mac with brew
Install Java
```
brew cask install java
```

Install kafka
```
brew install kafka
```
