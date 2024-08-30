# CustomPose-Classification-Mediapipe: Badminton Pose Classification

Proyek ini bertujuan untuk membuat model klasifikasi pose khusus untuk bulutangkis menggunakan MediaPipe dan OpenCV.

<p align="center">
  <img src='Screenshot 2024-08-30 103424.png'/>
</p>

## Persiapan

### 1. Clone Repository dan Instal Dependensi

Clone repository dan instal dependensi yang diperlukan:

```bash
git clone https://github.com/naseemap47/CustomPose-Classification-Mediapipe.git
cd CustomPose-Classification-Mediapipe
pip3 install -r requirements.txt
```

### 2. Download Dataset

Unduh dataset pose bulutangkis dan susun dataset dalam struktur berikut:

```
├── Dataset
│   ├── Footwork
│   │   ├── 1.jpg
│   │   ├── 2.jpg
│   │   ├── ...
│   ├── Backhand
│   │   ├── 1.jpg
│   │   ├── 2.jpg
│   │   ├── ...
.   .
.   .
```

### 3. Buat Dataset Landmark untuk Setiap Kelas

Jalankan skrip berikut untuk membuat dataset landmark dari gambar pose:

```bash
python3 poseLandmark_csv.py -i <path_to_data_dir> -o <path_to_save_csv>
```

**Contoh:**

```bash
python3 poseLandmark_csv.py -i data/ -o data.csv
```

File CSV akan disimpan di lokasi yang ditentukan.

### 4. Konversi CSV ke Model TFLite

Setelah mendapatkan file CSV, konversi ke model TFLite menggunakan [Google Colab ini](https://colab.research.google.com/drive/1gelTfXdKFB4d73wUV6HhskgvtluV9xDD?usp=sharing).

### 5. Jalankan Program Interface

Setelah memiliki model TFLite, jalankan program interface.

**Untuk Keluar dari Window - Tekan Q-key**

