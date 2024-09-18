=== Tugas 2 ===
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

=== Tugas 3 ===
Jawaban nomor 1:
Data delivery diperlukan implementasinya dalam sebuah platform agar user dapat mengakses suatu data pada platform dalam berbagai lokasi dan perangkat. Selain itu, dengan adanya data delivery, mekanisme pengiriman informasi dapat berjalan secara lancar dan efisien.

Jawaban nomor 2:
JSON lebih popular dari xml karena beberapa hal, seperti JSON yang lebih ringkas dan memiliki format yang  lebih sederhana jika dibandingkan dengan XML sehingga ukuran data lebih kecil dan lebih mudah dipahami. Selain itu, banyak Bahasa pemrograman modern yang mendukung parsing JSON secara langsung, sedangkan XML memerlukan parser yang lebih komplekas dan memerlukan Langkah tambahan, sehingga parsing JSON lebih cepat dan mudah jika dibandingkan dengan parsing XML.

Jawaban nomor 3:
method is_valid() pada form Django berfungsi untuk melakukan validasi pada input user sehingga memiliki format yang sesuai.

Jawaban nomor 4:
csrf_token dapat berfungsi untuk melindungi dari serangan yang berbahaya. Ketika seorang user yang telah diautentikasi menjelajahi webstie, Django membuat sebuah token untuk setiap sesinya. Token ini nanti dapat memastikan bahwa input atau request dari user yang telah di autentikasi dan bukan dari sumber yang berbahaya. Jika kita tidak menambahkan csrf_token, maka Ketika ada user yang telah di autentikasi oleh kita terkena serangan, seorang penyerang tersebut dapat mengubah data user dalam website kita sehingga nantinya data mereka dapat hilang atau bahkan kehilangan saldo.

Jawaban nomor 5:
1) membuat input form, Pertama-tama saya perlu membuat sebuah file "forms.py" dalam direktori "main" untuk membuat spesifikasi input yang diinginkan (mengimport "models" untuk mendapatkan struktur datanya dan fields untuk menunjukkan fields "model" yang digunakan untuk form. Kemudian, membuat file "create_product_entry.html" pada direktori templates dalam direktori main untuk membuat kerangka tampilan Ketika meminta user input.
2) menambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID. Pertama, menambahkan empat fungsi show untuk masing-masing format dalam file "views.py" yang ada pada direktori "main". isi dari fungsi tersebut adalah variabel "data" yang mengumpulkan hasil input user dan mereturn HttpResponse untuk menampilkan data-data tersebut.
3) Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2. Pertama, import fungsi show masing-masing format pada "urls.py". Kemudian, menambahkan path untuk masing masing fungsi dalam urlpatterns

![postman_xml](https://github.com/user-attachments/assets/797eafef-3e9c-4a55-94e7-49736e093417)
![postman_json](https://github.com/user-attachments/assets/7e5a62d2-1de9-4000-8b1c-04c1674076a4)
![postman_xml_id](https://github.com/user-attachments/assets/4d3b4167-76e9-4c1c-86d2-50fdcf667f28)
![postman_json_id](https://github.com/user-attachments/assets/0ff86db8-4c76-41d4-bccb-18e52c33b925)
