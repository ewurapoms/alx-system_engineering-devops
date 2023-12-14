# E-MALL CRASH INCIDENT REPORT 
	
![image](postmortem_img.png)


## Issue summary
Duration:
Start Time: January 15, 2023, 09:45 AM UTC
End Time: January 15, 2023, 11:30 AM UTC

Impact:
The outage affected the availability of our e-commerce website. Users experienced slow page load times, and approximately 30% of users were unable to complete transactions during the outage.


## Timelines (UTC+3)
Detection:
January 15, 2023, 09:45 AM UTC
The issue was detected through automated monitoring alerts on elevated response times and error rates.

Actions Taken:

09:50 AM UTC: The operations team began investigating server logs and identified a surge in database connection attempts.
10:05 AM UTC: Assumed the issue might be due to a DDoS attack, initiated traffic analysis, but no malicious activity was detected.
10:30 AM UTC: Realized the database was under stress, focused investigation on database performance.
10:45 AM UTC: Identified inefficient queries causing a spike in CPU usage on the database server.
Misleading Paths:

Investigated network issues initially, leading to a temporary misallocation of resources.
Explored the possibility of a recent code deployment causing issues, but version control and rollbacks proved this assumption wrong.
Escalation:

11:00 AM UTC: Incident escalated to the development team to optimize database queries.
11:15 AM UTC: Communications team informed for customer-facing updates.
Resolution:

11:30 AM UTC: The development team optimized database queries, reducing the load on the database server.
11:35 AM UTC: Normal website functionality restored; users experienced improved page load times.


## Root Cause and Resolution:

Root Cause:
The primary issue was identified as a sudden surge in traffic triggering inefficient database queries. These queries, compounded by increased user load, created a bottleneck in database connections.

Resolution:
Database queries were optimized to reduce the load on the server. Additionally, a caching mechanism was implemented to mitigate future spikes in traffic, ensuring smoother scalability.


##Corrective and Preventative Measures

Improvements/Fixes:

Implement enhanced monitoring to proactively identify and address traffic spikes.
Conduct regular performance testing to optimize database queries and server configurations.
Tasks:

Short-Term:
Implement caching mechanisms to handle sudden traffic increases.
Update monitoring thresholds to trigger alerts earlier during unusual traffic patterns.
Medium-Term:
Schedule regular database performance reviews and optimizations.
Conduct a post-mortem review to improve incident response and communication.
Long-Term:
Explore load balancing solutions to distribute traffic efficiently.
Collaborate with infrastructure providers to prepare for scalable resources during peak times.


## Conclusion
This incident highlighted the need for proactive monitoring, efficient communication during outages, and continual optimization of systems to ensure a seamless user experience. The identified corrective and preventative measures aim to fortify our infrastructure against similar issues in the future.
