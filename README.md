# Hazelcast-Distributed-Map — Lab 2
Розгортання і робота з distributed in-memory data structures на основі Hazelcast: Distributed Map

## Part 1 — Installation and Setup

Hazelcast cluster was deployed using Docker Compose with 3 nodes and Management Center.

**Steps:**
1. Install Docker Desktop
2. Create `docker-compose.yml` with 3 Hazelcast nodes and Management Center
3. Run `docker compose up -d`
4. Install Python client: `pip install hazelcast-python-client`

Management Center is available at: http://localhost:8080

### Screenshots
![Docker compose up](screenshots/docker-compose-up.png)
![Docker compose ps](screenshots/docker-compose-ps.png)

## Part 2 — 3-Node Cluster Configuration

Three Hazelcast nodes were configured as Docker containers united in a single cluster named `dev`. All nodes automatically discover each other within the Docker network and form a cluster, which can be verified in Management Center where all 3 members are visible.

### Screenshots
![Management Center - 3 nodes](screenshots/management-center-cluster.png)

