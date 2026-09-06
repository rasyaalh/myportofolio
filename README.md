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