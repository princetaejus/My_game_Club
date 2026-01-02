# My_game_Club
Random website with a simple reaction time game and leaderboard created using django framework

## 🎮 My Game Club


https://github.com/user-attachments/assets/5680fda7-6eb7-468e-bd89-4defd6b54a5c


My Game Club is a web-based platform built with **Django** that allows users to explore, interact with, and engage in games within a club-style environment.  
The project is designed to be scalable, user-friendly, and customizable for future game-related features.

---

## 🚀 Features

- 🔐 User Authentication (Login / Register)
- 👤 User Profiles with points system
- 🕹️ Game listing and interaction support
- 🧠 Extendable architecture for adding new games
- 🎨 Clean UI with scope for animations and dark mode
- 🛠️ Admin dashboard for managing users and data
- 📱 Responsive design (can be extended)

---

## 🧩 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (default, can be changed)
- **Authentication:** Django built-in auth system

---
## 🧪 Project Status

- ✅ User authentication working
- ✅ Profile auto-creation via signals
- ✅ Admin dashboard enabled
- 🤖 AI Image Scanner (in development / integrated)
- 🚧 Game logic expanding
- 🚧 UI/UX improvements planned
- 🏆 Leaderboards
---

## 🛣️ Future Enhancements


- 🎯 Achievements system
- 🌙 Dark mode
- 📊 Game analytics
- 🎮 Multiplayer games
- 🔔 Notifications

---
## 👨‍💻 Author

- Prince
- Built for learning, experimentation, and fun 🚀

---
## ⚙️ Installation & Setup

Follow these steps to run the project locally.

### 1️⃣ Clone the Repository
   - git clone https://github.com/your-username/my_game_club.git
   - cd my_game_club

### 2️⃣ Create & Activate Virtual Environment

    python -m venv venv
  - Activate it:

  #####  Windows
    venv\Scripts\activate
  ##### Linux / macOS
    source venv/bin/activate
---
### 3️⃣ Install Dependencies

     pip install django
---
### 4️⃣ Apply Database Migrations

    python manage.py makemigrations
    python manage.py migrate
---
### 5️⃣ Create Admin (Superuser)

    python manage.py createsuperuser
---
### 6️⃣ Run the Development Server
    python manage.py runserver
  - Open your browser and visit:
  -👉 http://127.0.0.1:8000/
--- 
### 🔑 Admin Panel

   Access the Django Admin Panel at:
  - 👉 http://127.0.0.1:8000/admin/
---

## 📂 Project Structure

```text
my_game_club/
│
├── manage.py
├── my_game_club/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── users/
│   ├── models.py
│   ├── signals.py
│   └── admin.py
│
├── games/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
├── templates/
├── static/
└── db.sqlite3
