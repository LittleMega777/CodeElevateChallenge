bin\windows\zookeeper-server-start.bat config\zookeeper.properties
bin\windows\kafka-server-start.bat config\server.properties

bin/kafka-topics.sh --create \
  --topic meu-topico \
  --bootstrap-server localhost:9092 \
  --partitions 1 \
  --replication-factor 1

bin/windows/kafka-topics.bat --create --topic meu-topico -- bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

bin\windows\kafka-topics.bat --list --bootstrap-server localhost:9092