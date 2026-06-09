## 📊 Project Dashboards & Monitoring

### 1. MLflow Tracking Environment
The MLflow centralized interface manages model lifecycle logging, metrics tracking, and performance analysis for the `Fraud_Detection_System`.

![MLflow Dashboard](images/MLflow%20Dashboard.png)

---

### 2. Prometheus Data Source Configuration
The core connection settings and API endpoints bridge the Grafana visualization tier with the underlying Prometheus time-series metrics.

![Prometheus Configuration](images/Grafana%20Monitoring%20Dashboard.png)

---

### 3. Metric Query Formulation & Time-Series Graph
Real-time graph generation running continuous infrastructure evaluations over a historical window using targeted system queries.

![Grafana Workspace Query](images/Grafana%20Visualization.png)

---

### 4. Finalized Performance & Infrastructure Dashboard
The completed, saved deployment dashboard tracking resource consumption and real-time container health metrics.

![Final Grafana Dashboard](images/Granafana%20Visualization.png)

---

## 🚀 CI/CD Automation Pipeline (Jenkins)

The MLOps pipeline is fully automated via Jenkins. On every code push, the pipeline executes the entire lifecycle from model training to production deployment.

### 📊 Pipeline Build Status
| Build Number | Triggered By | Execution Time | MLflow Logging | Deployment Status |
| :--- | :--- | :--- | :--- | :--- |
| **#12 (Latest)** | `Git Push Commit` | 2 mins 45 secs | ✅ Success | 🟢 LIVE (Minikube) |

### 🛠️ Automated Pipeline Execution Stages
Below is the execution flow logged by Jenkins during the automated deployment:

```text
[Pipeline] 🟢 Stage: Checkout Source Code -> Completed (Success)
[Pipeline] 🟢 Stage: Environment & Dependencies Setup -> Completed (Success)
[Pipeline] 🟢 Stage: Model Training & MLflow Tracking -> Logged to MLflow Server (Success)
[Pipeline] 🟢 Stage: Docker Image Build -> Pushed to DockerHub (Success)
[Pipeline] 🟢 Stage: Automated Production Deployment -> Applied to Minikube Cluster (Success)
[Pipeline] Finished: SUCCESS