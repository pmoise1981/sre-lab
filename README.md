# 🧠 SRE Lab – Observability & Monitoring Stack

This project sets up a **hands-on Site Reliability Engineering (SRE) lab** that demonstrates how to monitor applications and infrastructure using a modern open-source observability stack.

It includes preconfigured services for **metrics, logs, and dashboards**, designed to mirror production-grade reliability workflows.

---

## 🧩 Features

* **Prometheus** – collects and stores time-series metrics from monitored services
* **Grafana** – visualizes metrics and builds alert dashboards
* **Loki & Promtail** – centralized log aggregation and querying
* **Docker Compose** – orchestrates multi-container setup locally
* **Environment Variables (.env)** – configurable ports, data paths, and credentials
* **Modular design** – easily extendable to **Kubernetes**, **Alertmanager**, or **Slack alerting**

---

## ⚙️ Architecture Overview

```
                ┌────────────┐
                │  Promtail  │───► Logs ───► Loki
                └────────────┘
                       │
                       ▼
┌────────────┐    ┌────────────┐    ┌────────────┐
│  App (Flask│───►│ Prometheus │───►│  Grafana   │
└────────────┘    └────────────┘    └────────────┘
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/pmoise1981/sre-lab.git
cd sre-lab
```

### 2️⃣ Create Environment File

Copy the example environment file:

```bash
cp .env.example .env
```

### 3️⃣ Start the Stack

```bash
docker compose up -d
```

Grafana will be available at:
**[http://localhost:3000](http://localhost:3000)**
Prometheus at: **[http://localhost:9090](http://localhost:9090)**

---

## 📊 Prebuilt Dashboards

* **System Metrics Dashboard:** CPU, memory, disk usage
* **Container Health Dashboard:** Uptime, restart count, latency
* **Application Metrics (optional):** Integrates with Flask or FastAPI exporters

---

## 🧱 Tech Stack

**Prometheus · Grafana · Loki · Promtail · Docker Compose · Linux · .env**

---

## 🧩 Future Enhancements

* Add **Alertmanager + Slack/Email alerts**
* Add **Service-Level Indicators (SLIs)** and **Service-Level Objectives (SLOs)**
* Integrate **OpenTelemetry exporters** for tracing
* Add **Kubernetes manifests** for production-grade orchestration

---

## 👨🏾‍💻 Author

**Pierre Moise**
Site Reliability & DevOps Engineer | Observability, CI/CD, Cloud Automation
📎 [GitHub](https://github.com/pmoise1981)



