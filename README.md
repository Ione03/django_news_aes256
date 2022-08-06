Bagaimana menggunakaan :

1. Create database di mysql dengan nama : db_news

2. Git Clone https://github.com/Ione03/django_news_aes256.git

3. cd django_news_aes256

4. python manage.py migrate

5. Untuk login ke halaman dashboard ketik :
   python manage.py createsuperuser

6. Masukkan data awal ke database ketik :
   python manage.py loaddata db/categories.json

7. Jalan aplikasi di local ketik :
   python manage.py runserver

8. buka browser ketik :
   127.0.0.1:8000

9. ke halaman dashboard ketik :
   127.0.0.1:8000/login
   masukkan username dan password sesuai dengan yang diinput di step 5 di atas