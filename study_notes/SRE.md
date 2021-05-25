Using Software Engineer approach to solve a software problem such as reqriting to stack to eliminate single point of failure.
The product team and the SRE team select an appropriate availability target for the service and its user base, and the service is managed to that SLO.
Determining what to automate, under what conditions, and how to automate it.
Reduced mean time to repair (MTTR) for common faults results in increased product developer velocity, as engineers don’t have to waste time and focus cleaning up after these issues.
SRE has particular expertise around the availability, latency, performance, efficiency, change management, monitoring, emergency response, and capacity planning of the service(s) they are looking after. 

SLO: 
Service level objectives (SLOs) specify a target level for the reliability of your service.SLOs are a tool to help determine what engineering work to prioritize. 
For example, consider the engineering tradeoffs for two reliability projects: automating rollbacks and moving to a replicated data store. By calculating the estimated 
impact on our error budget, we can determine which project is most beneficial to our users.
SLO compliance will simply be another KPI (key performance indicator) or reporting metric, rather than a decision-making tool.
a) First step in formulating appropriate SLOs is to talk about what an SLO should be, and what it should cover.
b) Service level indicators come into play: an SLI is an indicator of the level of service that you are providing.
    Number of successful HTTP requests / total HTTP requests (success rate)
c) Stakeholders Agreement
d) Error budgets are a tool for balancing reliability with other engineering work, and a great way to decide which projects will have the most impact.
    

Monitoring:
Desirable Features of Monitoring STartegy:
a) Speed: Data should be available when you need it: freshness impacts how long it will take your monitoring system to page you when something goes wrong. 
b) Calculation: At a minimum, you’ll probably want your system to retain data over a multi‐ month time frame. “Has this unusual behavior happened before?”
c) Interfaces: Your dashboards will be primary interfaces for displaying monitoring, so it’s important that you choose formats that most clearly display the data you care about. 
Some options include heatmaps, histograms, and logarithmic scale graphs.
d) Alerts: The ability to set different severity levels for different alerts is also useful.
e) Treat Configuration as Code: Third-party solutions like grafanalib enable this approach for components that are traditionally configured with a UI.
f) Encourage Consistency: centralized dashboarding service, where each team’s dash‐ boards are discoverable and accessible.
g) Prefer Loose Couplin: Modern design usually involves separating collection and rule evaluation (with a solution like Prometheus server), 
long-term time series stor‐ age (InfluxDB), alert aggregation (Alertmanager), and dashboarding (Grafana).

Alerting:
Generate alerts from service level indicators (SLIs) and an error budget, you need a way to combine these two elements into a specific rule. 
Your goal is to be notified for a significant event: an event that consumes a large fraction of the error budget.
Ways of Alerting;
  a) Target Error Rate >= SLO Threshold
  b) Increased Alert Window
  c) Incrementing Alert Duration
  d) Alert on Burn Rate
  e) Multiple Burn Rate Alerts
  
Toil Reduction:
  a) Business Process
  b) Prod Interrupts
  c) Migrations
  
Simplicity:
