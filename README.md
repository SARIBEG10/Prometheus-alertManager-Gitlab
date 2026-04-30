# Prometheus + AlertManager + Gitlab + Nexus + Flask Dockerized App
##  Dockerized  Flask App  Monitored By Prometheus

***STEPS:***

1. **_Create_  docker-compose.yml**
2. **_Define_  services in compose file**
3. **_Create_ app Folder for Flask Application**
4. **_Write_ your Code in main.py**
>[!TIP]
>**use _prometheus_flask_exporter_ Module for metrics export to prometheus service metrics dashboard**
5. _Prepare_ __requirements.txt__
6. _Write_ **Dockerfile (Application Dockerized)**
7. _Add_ **simple test for 200 status check of root**
8. _Create_ **Prometheus Folder includes alerts.yml and prometheus.yml FOR MORE INFO ABOUT alerts.yml configuration: [Prometheus alert rules](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/)**
9. _Create_ **alertmanager Folder includes config.yml contains alerting configuration (in this example smtp email notification you could use also : Jira, slack, ...) FOR MORE INFO :[AlertManager Configuration](https://prometheus.io/docs/alerting/latest/configuration/)**
10. _Create_ **.gitlab-ci.yml for pipeline** 
> [!NOTE]
> **Instead of Docker Public Registry, Use Nexus Private Registry** [Nexus Installation Guide](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://help.sonatype.com/en/install-nexus-repository.html&ved=2ahUKEwj2ivu7qZSUAxUYSPEDHdLiLPYQFnoECBgQAQ&usg=AOvVaw0QqRvKC0tV6JrFLqWDQtVX)
