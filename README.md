Prometheus + AlertManager + Gitlab + Nexus + Flask Dockerized App
# This is sample Project which I implemented as Dockerized App By Prometheus Monitoring Tool
Steps:

- Create docker-compose.yml
- Define your services in compose file
- Create app Folder for Flask Application
- Write your Code in main.py => use prometheus_flask_exporter Module for metrics export to prometheus service metrics dashboard
- Prepare requirements.txt
- Writing Dockerfile (Application Dockerized)
- Add simple test for 200 status check of root
- Create Prometheus Folder includes alerts.yml and prometheus.yml FOR MORE INFO ABOUT alerts.yml configuration: https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/
- Create alertmanager Folder includes config.yml contains alerting configuration (in this example smtp email notification you could use also : Jira, slack, ...) FOR MORE INFO : https://prometheus.io/docs/alerting/latest/configuration/
- Create .gitlab-ci.yml for pipeline 


NOTE: Instead of Docker Public Registry, Use Nexus Private Registry
