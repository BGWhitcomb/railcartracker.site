# site-metrics-springboot

Spring Boot backend for RailcarTracker.

Prerequisites
- JDK 17+ (or the version configured in pom.xml)
- Maven wrapper included (mvnw / mvnw.cmd)

Build & run
```bash
# Linux/macOS
cd site-metrics-springboot
./mvnw package -DskipTests
java -jar target/*.jar

# Windows
cd site-metrics-springboot
mvnw.cmd package -DskipTests
java -jar target\*.jar
```

Dev
```bash
# run with Spring Boot plugin
./mvnw spring-boot:run
# or pass env vars:
MY_APP_KEY=secret ./mvnw spring-boot:run
```

Configuration
- application.properties supports environment variable placeholders:
  - Example: my.app.key=${MY_APP_KEY:default}
- Recommended: set env vars in Docker Compose or your shell.
- Optional (dev): you can load a local `.env` before Spring starts (see project notes or add a small loader in main()).

Docker
```bash
docker build -t site-metrics-springboot -f Dockerfile .
```

Testing
```bash
./mvnw test
```