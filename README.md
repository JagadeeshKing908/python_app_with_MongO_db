# 🚀 Flask MongoDB Login/Register App

A simple full-stack web application built using **Flask (Python)** and **MongoDB (Docker)**.  
It includes user registration, login authentication, session handling, and a dashboard to display users.

---

## 📌 Features

- 👤 User Registration
- 🔐 User Login/Logout
- 📦 MongoDB Database Integration
- 📊 Dashboard showing registered users
- 🎨 Simple Bootstrap UI
- 🐳 MongoDB running in Docker container

---

## 🏗️ Tech Stack

- Backend: Flask (Python)
- Database: MongoDB (Docker)
- Frontend: HTML, Bootstrap 5
- Server: Gunicorn / Flask Dev Server
- OS: AWS EC2 (Ubuntu / Linux)

---

## 📁 Project Structure

flask-mongo-app/
│── app.py
│── requirements.txt
│
├── templates/
│ ├── index.html
│ ├── login.html
│ ├── register.html
│ └── dashboard.html
│
├── static/
│ └── style.css

Installations/Packages :
----------------------
pip3 install -r requirements.txt

Created mongo DB using docker container:--
--------------------------------------

docker run -d \
  -p 27017:27017 \
  -e MONGO_INITDB_ROOT_USERNAME=admin \
  -e MONGO_INITDB_ROOT_PASSWORD=123 \
  --name mongodb mongo
  
To Run app :
--------------
  
  python3 app.py

MongoDB Connection Inside app.py:
----------------------------------
MongoClient("mongodb://admin:123@localhost:27017/?authSource=admin")

To validate data is inserted and is working :-
-----------------------------------------

1)login to docker container :

docker exec -it mongodb 

2)sign into MongoDB :-

mongosh -u admin -p 123 --authenticationDatabase admin

3)checks databases are created or not :-
   a)To check db is created or not ---> show dbs;
   b)To use the paticular DB --> use userdb;
   c)To see table is created or not---> show collections;
   d)To see data ---->db.users.find().pretty()
