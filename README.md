# Inventory app

## 1. Cara buat appnya

    - Buat venv
    - Install django
    - Run `django-admin startproject <nama_project>`
    - cd ke `<nama_project>`
    - Run `python manage.py startapp main`
    - Buat `urls.py` di folder main
    - Setup `urls.py` nya
    - Buat model Item
    - Register ke `admin.py` di folder `main`
    - Masukin `main` ke `settings.py`
    - Run `python manage.py makemigrations && python manage.py migrate`
    - Run `python manage.py createsuperuser` buat bikin superuser
    - Terakhir, run `python manage.py runserver`

## 2. Hubungan urls.py, views.py, models.py, dan file .html

    - urls.py: Mengatur routing pada server, path `/a` akan menunjuk ke sebuah fungsi / class pada `views.py`
    - views.py: Mengatur perilaku server ketika mendapatkan request dari client, serta mengembalikan sebuah response kepada client
    - models.py: Mengatur bentuk data pada database, views.py akan mengambil data dari database melalui class yang dibuat di models.py
    - .html: Merupakan bagian template dari arsitektur MVT pada Django. Berfungsi untuk menyajikan hasil response dari views.py

## 3. Kenapa pake virtualenv?

    Agar dependency setiap project tak terpengaruhi oleh faktor luar, seperti versi python dan library dari host machine. Dan mencegah adanya package yang tak bersangkutan ikut dipakai / diinstall ketika perintah `pip freeze > requirements.txt` dijalankan

## 4. MVC vs MVT vs MVVM

    - MVC:
    - MVT:
    - MVVM:

Link: https://kirantiloh-inventory.adaptable.io
