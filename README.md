# **SyntheticMonitoringPlatform**
Develop a Synthetic Monitoring Platform 

# System Design Diagram 
 - Pinging the server
 - gathering data in Prometheus
 - Grafana for visualization
   

# Introduction to Observability and Synthetic Monitoring

Observability: Comprehensive view of system internals through log analysis, traces, and events.​

​Synthetic Monitoring: Simulated tests to validate application functionality from user's perspective.​

​Benefits: Proactive issue detection, network outage prevention, and service availability assurance.

# Observability: A Comprehensive View of Systems

Observability is about analyzing system internals to understand the health and performance of applications and infrastructure.​

It involves scanning, parsing, and tracing logs, events, and system metrics.​

It enables cross-service tracing and provides a holistic view of system operations and overall performance

# What is Synthetic Monitoring

Active Monitoring / Active Testing​

Emulates the behavior of real users​

Robotically generate user transactions on demand then analyze the response of the system​


# Synthetic Monitoring: Simulating User Interactions

Synthetic monitoring simulates user behavior to test application functionality.​

It includes API endpoint calls, headless browser sessions, and user action simulations.​

It allows proactive testing and alerting on application issues affecting end-user experience


# The Importance of Synthetic Monitoring

Helps Administrators to detect availability and performance issues on their websites/applications without waiting for a real user to be impacted by system outage​

Reduces the risk of poor digital user experience​

Synthetic monitoring ensures high availability of websites, APIs, and servers.​

It verifies operational readiness and responsiveness beyond server status codes.​

It schedules automated checks from multiple regions to ensure global availability

# Observability and Synthetic Monitoring Together

Observability provides insights into system internals, while synthetic monitoring validates external user experiences.​

​Together, they offer a robust approach to maintaining system health and user satisfaction.



# Ping Synthetic Monitor

Essential tool in Monitoring setup​

A type of ‘uptime’ monitoring that checks the availability of a website or server or network device​

Ensures that the web server can be reached and is operational​

A fundamental tool used by network administrators to verify that a website is accessible from various locations around the world.​

First step in troubleshooting when an application or website becomes unavailable, provides a quick overview of the network situation and helps to narrow down the scope of the problem



# **Prometheus**

Counter (the only way is up): Use counters for counting events, jobs, money, HTTP request, etc. where a cumulative value is useful.​

Gauges (the current picture): Use where the current value is important — CPU, RAM, JVM memory usage, queue levels, RTT, Packet Loss etc.​

Histograms (Sampling Observations): Generally use with timings, where an overall picture over a time frame is required — query times, HTTP response times.​

Summaries (client-side quantiles): Similar in spirit to the Histogram. Use when you start using quantile values frequently with one or more histogram metrics.


# **Grafana**
Dashboard: Grafana provides a user- friendly dashboard for visualizing time series data, logs, and application metrics in a single interface. ​

​
Data Visualization: Grafana offers a wide range of visualization options, including graphs, charts, and heatmaps, to help users gain insights from their data.​

​
Monitoring Tool: As a monitoring tool, Grafana enables real-time monitoring and analysis of system performance, infrastructure, and application health.
