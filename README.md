Prometheus + AlertManager + Gitlab + Nexus + Flask Dockerized App
# This is sample Project which I implemented as Dockerized App By Prometheus Monitoring Tool

Steps:
1- Create docker-compose.yml
2- Define your services in compose file
3- Create app Folder for Flask Application
4- Write your Code in main.py => use prometheus_flask_exporter Module for metrics export to prometheus service metrics dashboard
5- Prepare requirements.txt
6- Writing Dockerfile (Application Dockerized)
7- Add simple test for 200 status check of root
8- Create Prometheus Folder includes alerts.yml and prometheus.yml FOR MORE INFO ABOUT alerts.yml configuration: https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/
9- Create alertmanager Folder includes config.yml contains alerting configuration (in this example smtp email notification you could use also : Jira, slack, ...) FOR MORE INFO : https://prometheus.io/docs/alerting/latest/configuration/
10- Create .gitlab-ci.yml for pipeline 
NOTE: Instead of Docker Public Registry, Use Nexus Private Registry
