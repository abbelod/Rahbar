# **Rahbar**

A Django-based web application for managing tours, hotels, transport, and airline bookings. Users can book hotel rooms, tour packages, airline tickets, and bus transport, all in one platform.

---

## **Features**
- Hotel companies can list rooms and packages.
- Tour companies can create tour packages.
- Airline companies can sell tickets.
- Bus companies can list transport packages.
- Users can book hotels, tours, and transportation.

---

## **Tech Stack**
- **Backend:** Django
- **Database:** SQLite (default), switchable to PostgreSQL/MySQL
- **API Integration:** GROQ for chatbot

---

## **Prerequisites**
Before you begin, ensure you have the following installed on your machine:
- Python 3.9+ 
- Git
- Virtualenv (optional but recommended)

---

## **Getting Started**

### **1. Clone the Repository**
```bash
git clone https://github.com/abbelod/Rahbar.git
cd myproject
```
## **Making Migrations**
```
python manage.py makemigrations
python manage.py migrate
```
## **Creating Superuser**
```
python manage.py createsuperuser
```

## **Setting Up API key in .env file**
```
touch .env
GROQ_API_KEY={put api key here}
get your api key from groq
```

## **Run the Server**
```
python manage.py runserver
```
