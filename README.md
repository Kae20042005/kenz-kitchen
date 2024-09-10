Jawaban nomor 1:
1) Membuat sebuah proyek Django baru, untuk membuat sebuah proyek Django baru saya melakukan inisiasi sebuah proyek Django dengan cara membuat direktori, mengaktifkan Virtual Enviroment, menyaipkan Depencencies dalam sebuah file yaitu requirements.txt yang nantinya akan di dwonload dengan python enviroment, kemudian membuat proyek Django dengan comman "startproject", yang kemudian melakukan konfigurasi proyek.
2) Membuat aplikasi dengan nama main pada proyek tersebut, pembuatan aplikasi ini dapat menggunakan command "python manage.py startapp main" yang nantinya akan membuat direktory baru berupa main yang berisi file penunjang aplikasi main itu tersebut. 
3) Melakukan routing pada proyek agar dapat menjalankan aplikasi main, aplikasi ini di routing pada proyek agar dapat dijalankan oleh proyek dengan cara menambahkan "main" pada INSTALLED_APPS dalam berkas "settings.py" yang ada di folder main project.
4) Membuat model pada aplikasi main dengan nama Product, pertama-tama buka aplikasi main kemudian buka berkas "models.py", kemudian tambahkan kelas Product dengan parameter "models.Model" lalu isi dengan atribut name, category, price, dan description dengan tipe data yang sesuai dengan spesifikasi soal.
5) Membuat sebuah fungsi pada "views.py" untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu. Pertama-tama melakukan integrasi komponen MVT dengan membuka berkas "vies.py" pada aplikasi main, lalu mengimpor "render" dan menambahkan fungsi "show_main" yang berisi sebuah dictionary untuk penyimpanan data yang nantinya akan ditampilkan pada berkas html.
6) Membuat sebuah routing pada "urls.py" aplikasi main untuk memetakan fungsi yang telah dibuat pada "views.py". Pertama, buat berkas urls.py pada direktori main untuk mengatur rute URL yang terkait dengan aplikasi main. Pada berkas ini, lakukan impor "path" dari "django.urls" dan impor "show_main" dari "main.views" lalu buat sebuah urlpatterns yang berisi "path('', show_main, name='show_main')" dan hubungkan dengan "urls.py" yang ada pada proyek dengan menambahkan path "main.urls" tadi ke urlpatterns dari url proyek
7) Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet. Pertama membuat projek baru dengan menekan tombol "Create New Project". Kemudian, pada proyek django tambahkan url deployment PWS pada "ALLOWED_HOSTS" dan melakukan push dengan command "git puush pws main:master"

Jawaban nomor 2:
1) Bagan request client: User -> Browser -"HTTP request"-> View -"Add, Update, or Delete Data" and "Dynamic Data to be populated"-> "Model" and "Template"
2) Bagan response: "Model" and "Template" -"Read Operations" and "Data input by user"-> View -"HTTP Response"-> Browser -> User
"urls.py" berfungsi untuk menyambungkan antara url main dengan url proyek agar memudahkan penyatuan Model dan Template pada View. "views.py" adalah View pada bagan yang isinya data yang nantinya akan ditampilkan. "models.py" adalah Model pada bagan yang isinya berupa struktur data dari aplikasi. berkas html adalah template dari proyek ini yang isinya kerangka utama proyek yang nanti akan diatur oleh view untuk visualisasinya.

Jawaban nomor 3:
Git berfungsi sebagai kontrol dari perkembangan versi suatu perangkat lunak. Dengan ini, apabila ada suatu masalah pada perangkat lunak akan lebih gampang dicari kesalahannya dengan memerika versi sebelumnya.

Jawaban nomor 4:
Framework Django dijadikan permulaan pengembangan perangkat lunak karena framework ini cukup terkenal, sehingga solusi untuk suatu masalah besar kemungkinannya sudah ada yang memecahkannya. Kemudian, karena bahasa yang digunakan adalah python, framework ini akan lebih mudah untuk dipahami.

Jawaban nomor 5:
Karena model pada Django adalah sebuah kelas yang memetakan sebuah objek dari dunia nyata ke database, sehingga disebut dengan Object-Relational Mapping (ORM)