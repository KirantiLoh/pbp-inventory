# Inventory app

<!-- ## ====================== WEEK 02 ====================== -->

<section>

## List of content

<ul>
    <li>
        <a href="#week-2">
            Week 2
        </a>
    </li>
    <li>
        <a href="#week-3">
            Week 3
        </a>
    </li>
    <li>
        <a href="#link">
            Link
        </a>
    </li>
</ul>

</section>

<section id="week-2">

### 1. Cara buat appnya

<details>
<summary>
Langkah-langkah
</summary>

1. Buat venv
2. Install django
3. Run `django-admin startproject <nama_project>`
4. cd ke `<nama_project>`
5. Run `python manage.py startapp main`
6. Buat `urls.py` di folder main
7. Setup `urls.py` nya
8. Buat model Item
9. Register ke `admin.py` di folder `main`
10. Masukin `main` ke `settings.py`
11. Run `python manage.py makemigrations && python manage.py migrate`
12. Run `python manage.py createsuperuser` buat bikin superuser
13. Terakhir, run `python manage.py runserver`
</details>

### 2. Hubungan urls.py, views.py, models.py, dan file .html

- `urls.py`: Mengatur routing pada server, path `/a` akan menunjuk ke sebuah fungsi / class pada `views.py`
- `views.py`: Mengatur perilaku server ketika mendapatkan request dari client, serta mengembalikan sebuah response kepada client
- `models.py`: Mengatur bentuk data pada database, views.py akan mengambil data dari database melalui class yang dibuat di models.py
- `*.html`: Merupakan bagian template dari arsitektur MVT pada Django. Berfungsi untuk menyajikan hasil response dari views.py

### 3. Kenapa pake virtualenv?

Agar dependency setiap project tak terpengaruhi oleh faktor luar, seperti versi python dan library dari host machine. Dan mencegah adanya package yang tak bersangkutan ikut dipakai / diinstall ketika perintah `pip freeze > requirements.txt` dijalankan

### 4. MVC vs MVT vs MVVM

- MVC: Model mengatur bagian data dan business logic, View mengatur bagaimana data akan ditampilkan, Controller menjadi mediator antara Model dan View
- MVT: Model mengatur bagian data dan business logic, Template mengatur bagaimana data akan ditampilkan, View menjadi mediator antara Model dan Template. Variasi MVC dari Django.
- MVVM: Model mengatur bagian data dan business logic, View mengatur bagaimana data akan ditampilkan, ViewModel menjadi mediator antara Model dan Template, MVVM lebih kuat dibanding MVC karena ViewModel biasanya ada data binding yang kuat, sehingga perubahan sedikit di Model akan langsung ke-reflect di View

</section>

<section id="week-3">

### 5. Apa perbedaan antara form POST dan form GET dalam Django?

- Form GET: Return hasil render HTML yang ada form pembuatan item, agar client bisa buat item dengan form yang ada di HTML nya
- Form POST: Kirim data hasil pengisian form ke function di `views.py` yang handle form nya, cek form valid ga, baru buat save formnya (Save form == buat item baru sesuai data di form)

### 6. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

- HTML: Biasa digunakan untuk menyajikan data secara langsung ke client, sehingga tak terlalu efisien untuk mentransfer data secara murni.
- JSON: Data disimpan dalam bentuk key-value pair, seringkali digunakan dalam pengiriman data antar web API. Sintaksnya lebih ketat dibanding XML, tetapi tetap fleksibel
- XML: Data disimpan dalam bentuk tag yang di-nesting (strukturnya mirip tree), sering dipakai untuk merepresentasikan data yang terlalu kompleks jika bentuknya dibuat JSON. Memiliki fleksibilitas yang tinggi.

### 7. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

Berdasarkan berbagai sumber, JSON sering digunakan para developer untuk pertukaran data antar aplikasi karena:

- Formatnya yang mudah di-parse
- Bentuk data berbasis teks yang ringan
- Banyak bahasa mempunyai native support untuk parsing JSON
- Lebih ringan dari XML karena berbentuk key value pair, tak seperti XML yang menggunakan sistem tag

### 8. Cara implementasi

<details>
<summary>
Langkah-langkah
</summary>

- Buat file `forms.py` yang isinya class ItemForm yang inherit forms.ModelForm
- Buat function di `views.py` buat handle render form dan submit form
- Buat masing-masing function di `views.py` sesuai keperluan (Serve HTML, JSON, XML)
- Configure routing nya di `urls.py`
- Terakhir, run `python manage.py runserver`
</details>

### 9. SS Hasil Postman

1. HTML
   <image src="https://cdn.discordapp.com/attachments/877540563891654698/1153737848013463703/image.png" />

2. JSON (All data)
   <image src="https://cdn.discordapp.com/attachments/877540563891654698/1151535342067908789/image.png" />
3. XML (All data)
   <image src="https://media.discordapp.net/attachments/877540563891654698/1151544311322783835/image.png" />

4. JSON (By ID)
   <image src="https://cdn.discordapp.com/attachments/877540563891654698/1151545882056073346/image.png" />

5. XML (By ID)
   <image src="https://cdn.discordapp.com/attachments/877540563891654698/1151545956412698805/image.png" />

</section>

<section id="week-4">
</section>

<section id="link">

Link: https://kirantiloh-inventory.adaptable.app

</section>
