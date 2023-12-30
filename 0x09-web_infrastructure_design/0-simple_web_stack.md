##Explanation:

##User's Browser:
     Initiates the request to access www.foobar.com.

##DNS Resolution:
     Resolves www.foobar.com to the server's IP address (8.8.8.8).

##Domain Registrar and DNS Server:
     Manages the domain registration and resolves domain names to IP addresses.

* Domain Configuration:
     Specifies the www record pointing to the server's IP.

* Web Browser:
     Sends the HTTP request to the Internet.

* Internet:
     Transmits the HTTP request to the server.

* Server (Nginx, Application Server, MySQL):
     Receives the HTTP request and forwards it to the appropriate component.

* Nginx (Web Server):
     Handles static content, forwards dynamic content requests.

* Application Server:
     Executes application code, processes dynamic content.

* MySQL Database:
     Stores and retrieves data required by the application.

##Issues with the Infrastructure:
* SPOF (Single Point of Failure):
     The entire infrastructure relies on a single server, making it vulnerable to failure.

* Downtime During Maintenance:
     Deploying new code may require restarting the web server, causing downtime.

* Cannot Scale if Too Much Incoming Traffic:
     Limited scalability due to the use of a single server. High traffic may lead to performance issues.

##Load Balancer:
  Reason: Introducing a load balancer helps distribute incoming traffic among multiple servers. This improves performance, enhances fault tolerance, and ensures better utilization of resources.

1. Database Primary-Replica Cluster:
    * Reason: Creating a Primary-Replica cluster for the database provides redundancy and fault tolerance. The Primary handles write operations, while Replicas handle read operations, improving scalability and ensuring data availability.

2. Distribution Algorithm of Load Balancer and How It Works:

    * Distribution Algorithm:
      Algorithm: Round Robin
        Explanation: Round Robin distributes incoming requests equally among the available servers. Each new request is directed to the next server in line, ensuring a balanced workload distribution.

3. Load-Balancer Setup - Active-Active vs. Active-Passive:

    * Active-Active Setup:
        Explanation: All servers are actively handling traffic simultaneously. This setup improves scalability and redundancy. However, it requires careful synchronization of data and increased management complexity.

    * Active-Passive Setup:
        Explanation: Only one server (node) actively handles traffic at a time, while others remain on standby. In case of a failure, the passive server takes over. This setup simplifies management but may underutilize resources.

4. How a Database Primary-Replica (Master-Slave) Cluster Works:

    * Database Primary-Replica Cluster:
        Explanation: The Primary node handles write operations, and the Replicas replicate data from the Primary to handle read operations. This setup ensures data consistency, availability, and fault tolerance.

5. Difference Between Primary Node and Replica Node in Regard to the Application:

    * Primary Node:
        Role: Handles write operations (insert, update, delete).
        Application Interaction: Accepts write requests and updates the database. It is the authoritative source for changes.

    * Replica Node:
        Role: Handles read operations (select).
        Application Interaction: Replicas serve read requests, providing scalable access to data. They are not authoritative for changes but offer improved read performance.
