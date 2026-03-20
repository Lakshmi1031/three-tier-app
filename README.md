# Containerized Three-Tier Web Application

A **containerized three-tier web application** built using **Flask**, **PostgreSQL**, and **Nginx**. This project demonstrates a scalable architecture using Docker and includes reverse proxy & load balancing.

---

## **Tech Stack**
- **Backend:** Flask (Python)  
- **Database:** PostgreSQL  
- **Web Server / Reverse Proxy:** Nginx  
- **Containerization:** Docker  
- **Deployment:** Docker Compose  

---

## **Project Architecture**
Client -> Nginx (Reverse Proxy + Load Balancer) -> Flask Application -> PostgreSQL Database

- **Three-tier structure**:  
  1. **Frontend / Web Layer:** Handles incoming HTTP requests (via Nginx).  
  2. **Application Layer:** Flask app processes business logic.  
  3. **Database Layer:** PostgreSQL stores persistent data.  

- **Dockerized services** ensure easy deployment and scalability.

---

## **Setup & Run Instructions**

1. **Clone the repository**
```bash
git clone https://github.com/Lakshmi1031/three-tier-app.git
cd three-tier-app

Build and start containers

docker-compose up --build

Access the application
Open your browser and go to: http://localhost (or your server IP if deployed remotely)

Key Features

Multi-container architecture

Reverse proxy with Nginx

Load balancing for high availability

Easy setup and deployment with Docker

Learning Outcomes

Hands-on experience with multi-container Docker applications

Understanding service communication and networking between containers

Knowledge of reverse proxy and load balancing

Practical exposure to DevOps workflows and scalable architecture design

Project Status

✅ Completed and fully functional

GitHub

Check out the code: https://github.com/Lakshmi1031/three-tier-app

Author

Lakshmi – DevOps / Network Support Engineer

## Final Output

<img width="1366" height="695" alt="Output" src="https://github.com/user-attachments/assets/93749397-31df-4546-915e-31b66c19b3c7" />






