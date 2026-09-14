Nama: Rasya Al Hawari
Prodi: Ilmu Komputer
NPM: 2506534176
Kelas: PBP B

### Tugas 1

## Pertanyaan Reflektif
1. Pada Tugas 1 ini, saya menggunakan berbagai elemen semantik HTML5 seperti `<header>`, `<main>`, `<section>`, `<article>`, dan `<nav>`. Penggunaan elemen-elemen ini sangat membantu saya dalam menyusun struktur kode yang lebih rapi dan bermakna secara semantik, tidak sekedar menggunakan tumpukan tag `<div>`. Sebagai contoh, saya menggunakan `<article>` untuk mengelompokkan setiap item pengalaman dan prestasi, karena masing-masing memiliki konteks isinya sendiri. Selain itu, saya juga mengeksplor penggunaan elemen `<details>` dan `<summary>` untuk membuat efek *dropdown menu* pada navigasi bar atas. Elemen ini memungkinkan fungsionalitas interaktif berjalan secara murni menggunakan HTML.

2. Tantangan yang saya hadapi adalah ketika menyusun tata letak untuk bagian Experience dan Achievements. Karena elemen tersebut berbentuk sepeerti "kartu", saya harus memastikan tampilannya tidak terpotong atau mengecil secara tidak proporsional saat diakses melalui layar smartphone. Daripada saya menggunakan ukuran piksel yang kaku, saya memutuskan untuk mencoba mengimplementasikan CSS Grid. Melalui proses uji coba, saya menemukan formula `repeat(auto-fit, minmax(280px, 1fr))`. Dengan pendekatan ini, bentuk kartu-kartu tersebut dapat secara otomatis menyesuaikan ukuran dan berpindah ke baris yang baru ketika lebar layar mengecil. Hasilnya, elemen yang diprioritaskan (isi teks di dalam kartu) tetap tertata rapi dan mudah dibaca, baik di layar desktop maupun smartphone.

3. Mengingat proyek ini masih berupa static web murni, saya menyadari adanya batasan yang besar dalam efisiensi mengatur isi konten. Sebagai contoh, jika saya ingin menambahkan riwayat pengalaman atau penghargaan baru, saya harus membuka kembali file `index.html`, menyalin blok tag `<article>`, dan menuliskan isi kontennya secara manual ke dalam kode HTML sebelum melakukan *push* ke server. Hal ini kurang efisien. Berdasarkan batasan tersebut, fungsi dinamis yang paling ingin saya implementasikan pada tugas-tugas MVT Django selanjutnya adalah integrasi Database. Saya merencanakan pembuatan Panel Admin, sehingga penambahan data portofolio dapat dilakukan melalui formulir, dan halaman web akan merender data tersebut secara dinamis tanpa perlu mengubah kode dasar secara manual.

## Progress Mingguan
Pada iterasi minggu ini, saya melakukan pembaruan pada halaman profil portofolio dengan rincian sebagai berikut:
1. (Tugas 1) Menambahkan section baru berupa "Track Record & Experience", "Awards & Achievements", dan "Education History" yang disusun meggunakan CSS Grid.
2. (Kreatifitas) Mengimplementasikan fitur "sticky header" agar bar navigasi atas selalu berada di atas layar saat halaman discroll.
3. (Kreatifitas) Membuat fitur "dropdown menu" pada bagian bar navigasi profil secara murni menggunakan elemen HTML5 (`<details>` dan `<summary>`), tanpa JavaScript.
4. (Kreatifitas) Menambahkan fungsionalitas "Dark Mode toggle" murni menggunakan CSS (mekanisme "hidden checkbox" dan pseudo-class `:has()`).

## AI Disclosure & Refleksi Pemecahan Masalah
Dalam pengerjaan Tugas Individu 1 ini, penulisan kerangka utama HTML dan desain CSS saya kerjakan secara mandiri. Namun, saya memanfaatkan AI (Gemini) dan sumber online lainnya sebagai "tutor virtual" dan teman diskusi ketika menemukan kendala, dengan rincian sebagai berikut:

1. **Diskusi Konsep Aplikasi Tata Letak:** Ketika mempertimbangkan penggunaan Flexbox atau Grid untuk menseejajarkan bentuk kartu riwayat, saya berdiskusi dengan AI. Dari diskusi tersebut, saya mempelajari dan memahami cara kerja `auto-fit` dan `minmax()`, yang kemudian saya formulasikan dan implementasikan sendiri ke dalam file CSS saya.
2. **Debugging Fitur Dark Mode:** Saya mencoba mengimplementasikan fitur "dark mode toggle" secara murni menggunakan CSS (dengan memanfaatkan trik "hidden checkbox" `:checked`). tetapi, saya menemukan masalah di mana warna latar belakang utama halaman tidak ikut berubah menjadi gelap. Saya meminta bantuan AI untuk menganalisis logika CSS tersebut. AI membantu memvalidasi bahwa "selector" `~` ("sibling") memiliki batasan mutlak, yaitu tidak dapat menargetkan elemen utama seperti tag `<body>`. Setelah memahami akar permasalahannya, saya menelusuri penggunaan "pseudo-class" modern `body:has(#dark-mode-toggle:checked)` dan menerapkannya sendiri. Solusi ini berhasil mengatasi batasan "selector" standar dan membuat "dark mode" berfungsi secara benar.
3. **Penyuntingan Terjemahan:** Saya meminta bantuan AI untuk menyunting dan merapikan tata bahasa dari terjemahan deskripsi profil dan riwayat saya (dari bahasa Indonesia ke bahasa Inggris) agar lebih natural dan profesional.


### Tugas 2

## Pertanyaan Reflektif
1. Alur arsitektur MVT (Model-View-Template) pada Django dimulai ketika pengguna mengakses URL di browser. Permintaan ini pertama kali diterima oleh `urls.py` tingkat proyek, yang kemudian merutekannya ke `urls.py` milik aplikasi `main`. Setelah menemukan pola URL yang cocok (misalnya `/achievements/`), sistem memanggil fungsi terkait di dalam `views.py`. Di dalam "view" ini, Django berkomunikasi dengan `models.py` untuk mengambil data dari database (misalnya daftar medali OSN). Data tersebut kemudian disimpan ke dalam sebuah "dictionary" (context) dan dikirimkan ke file HTML (Template). Terakhir, template merender data tersebut secara dinamis menggunakan sintaks DTL dan mengirimkan halaman utuh kembali ke browser pengguna.

2. Menyimpan data di dalam model membuat portofolio menjadi dinamis (data-driven). Pada Tugas 1, saya menggunakan HTML statis, sehingga penambahan riwayat baru mengharuskan saya membuka "source code" dan menyalin blok tag HTML secara manual. Dengan menggunakan model, data terpisah secara aman di database. Hal ini signifikan mempermudah pemeliharaan jangka panjang kerena saya bisa menambah, menghapus, atau mengedit data riwayat dan sertifikat kapan sajaa (misalnya melalui panel admin) tanpa berisiko merusak struktur antarmuka.

3. Perintah `makemigrations` berfungsi untuk mendeteksi perubahan struktur pada file `models.py` dan mencatatnya menjadi sebuah skema migrasi. Perintah ini belum menyentuh database secara fisik. Sementara itu, `migrate` berfungsi untuk mengeksekusi skema tersebut dan mengaplikasikannya ke dalam database nyata.
Sebagai contoh, pada tugas ini saya membuat "class" model baru bernama `Achievement`, `Education`, dan `Certification`. Setelah mendefinisikan "field"nya di `models.py`, saya diwajibkan menjalankan `makemigrations` untuk merekam instruksi penambahan tabel, dilanjutkan dengan `migrate` agar tabel untuk ketiga model tersebut benar-benar diciptakan di dalam file `db.sqlite3`.

## Progress Mingguan
Pada iterasi minggu ini, saya melakukan transisi dari "web statis" menjadi dinamis menggunakan arsitektur MVT dengan rincian pembaruan sebagai berikut:
1. (Tugas 2) Membuat tiga model baru (`Achievement`, `Education`, dan `Certification`) yang masing-masing memiliki minimal tiga "field" spesifik untuk menyimpan data historis secara terstruktur.
2. (Tugas 2) Mengonfigurasi "routing" URL dan "views" untuk memisahkan ketiga bagian tersebut menjadi halamannya masing-masing, lalu membuang konten "hardcode" statis dari halaman profil utama.
3. (Tugas 2) Mengganti konten HTML manual dengan perulangan Django Template Language (`{% for %}`) yang menarik data langsung dari database, lengkap dengan penanganan kondisi "empty state" menggunakan tag `{% empty %}`.
4. (Tugas 2) Menerapkan 9 skenario "unit test" untuk memastikan URL dapat diakses, data muncul saat tersedia, dan pesan kosong tampil dengan benar saat database kosong.
5. (Kreativitas) Menyempurnakan fitur "Dark Mode" dan "Dropdown Menu" dengan mengimplementasikan Vanilla JavaScript. Pembaruan ini membuat preferensi tema gelap tersimpan di `localStorage` (tidak terreset saat berpindah halaman) dan menu "dropdown" akan menutup secara otomatis jika pengguna mengklik area luar.

## AI Disclosure & Refleksi Pemecahan Masalah
Dalam pengerjaan Tugas Individu 2 ini, kerangka utama DTL dan konfigurasi struktur MVT saya susun secara mandiri mengikuti modul. Saya memanfaatkan AI (Gemini) sebagai mitra diskusi teknis dengan rincian sebagai berikut:

1. **Eksplorasi State Management Lintas Halaman:** Ketika memisahkan portofolio menjadi beberapa halaman URL yang berbeda, saya menemukan bahwa trik "hidden checkbox" murni CSS yang saya gunakan di Tugas 1 memiliki kelemahan: preferensi "Dark Mode" selalu ter-reset kembali ke terang setiap kali saya memuat halaman baru. Saya berdiskusi dengan AI untuk mencari solusi yang tetap ringan. AI memaparkan cara kerja `localStorage` pada JavaScript. Setelah memahaminya, saya mengimplementasikan skrip sederhana untuk menyimpan dan memanggil "state" tombol sakelar tersebut saat halaman (DOM) dimuat, sekaligus menambahkan logika untuk mendeteksi interaksi klik di luar elemen `<details>` navigasi.
2. **Manipulasi Data via ORM dan Django Shell:** Saat ingin memasukkan riwayat pendidikan dan rentetan prestasi secara sekaligus, saya menyadari pengisian manual melalui panel admin akan memakan waktu. Saya meminta AI membantu merumuskan "script" Python ORM (Object-Relational Mapping). AI membantu menyusun fungsi `.create()` secara masal dan memaparkan cara mencari objek spesifik dengan `.get(title__icontains="...")` untuk mengubah status kategori pengalaman lama saya menjadi "Finished" secara efisien tanpa harus merombak ulang database.