# Solution Architecture

## Application Components

### Sensor Service

Publishes simulated pressure, temperature, and machine-state messages through ROS 2.

### Robot Controller

Subscribes to sensor messages, evaluates operational thresholds, and determines whether the manufacturing cell is healthy, degraded, or stopped.

### Manufacturing API

Provides HTTP endpoints for health, status, and Prometheus-compatible metrics.

### Telemetry and Monitoring

Application metrics are exposed for Prometheus. Grafana can visualize the collected metrics.

## Platform Components

- Git for source control
- GitHub Actions and GitLab CI for build automation
- Docker for application packaging
- Docker Compose for local integration
- Kubernetes for orchestration
- Terraform and Vault planned as later implementation phases
- Prometheus and Grafana for observability

## Engineering Responsibilities Demonstrated

- Platform bring-up
- Dependency validation
- Build and test automation
- Containerization
- Deployment configuration
- Networking validation
- Runtime health validation
- Incident investigation
- Documentation
