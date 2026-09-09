## Manajemen Buku API

Endpoint Manajemen buku sederhana menggunakan FastAPI, tanpa memakai database, data disimpan didalam python list.

## Topik

 - FastAPI
 - Path / Query Parameters
 - Pydantic BaseModel
 - Request Body
 - In-Memory Data (Python List)
 - Filtering dan CRUD
 - HTTPException
 - jsonable_encoder
 - JSONResponse
 - Non-Database

## Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/buku` | Mendapatkan semua buku |
| GET | `/buku?id=&judul=` | Mendapatkan buku berdasarkan ID atau berdasarkan judul dan bisa keduanya dengan Query Parameter |
| GET | `/buku/{id}` | Mendapatkan buku berdasarkan ID |
| POST | `/buku` | Menambahkan buku |
| PUT | `/buku/{id}` | Mengubah buku |
|PATCH | `/buku/{id}` | Update spesifik ke status ketersediaan buku |
| DELETE | `/buku/{id}` | Menghapus buku |

## Cara Clone dan Eksekusi Program

### 1. Clone Repo

```bash
  git clone https://github.com/dams-code/manajemen-buku-api.git
  cd manajemen-buku-api
```

### 2. Membuat Virtual Environment(env)
Jika memakai Windows :
```bash
  python -m venv .venv
  .venv\Scripts\activate
```

Jika memakai Linux / Mac:
```bash
  python3 -m venv .venv
  source .venv/bin/activate
```

### 3. Install dependency

```bash
  pip install "fastapi[standard]"
```

### 4. Eksekusi FastAPI Server

Jika memakai UV:
```bash
  uv run fastapi dev main.py
```
Jika memakai non-UV:
```bash
fastapi dev main.py
```

### 5. Cek endpoint dan uji coba endpoint di Swagger UI
```bash
  http://127.0.0.1:8000/docs#/
```

### 6. Test di tampilan frontend (mount html)

karena lokasi middleware untuk mount index.htmlnya diset ke "/" untuk akses ke local pakai / diakhir port.

```bash
  http://127.0.0.1:8000/
```

## Tech Stack

### Backend
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-499848?style=for-the-badge&logo=uvicorn&logoColor=white)

### Frontend
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![SweetAlert2](https://img.shields.io/badge/SweetAlert2-8CD4F5?style=for-the-badge&logo=sweetalert2&logoColor=black)


<div align="center">

  <table border="0" style="border-collapse: collapse; border: none;">
    <tr>
      <td align="center" style="padding: 15px; border: none;">
        <img src="frontend/dokumentasi/tampilan-awal.png" alt="Tampilan Buku Awal" width="100%" style="border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
        <p align="center">
          <sub><b>Gambar 1:</b> Tampilan Awal Buku</sub>
        </p>
      </td>
    </tr>
  </table>

  <br>

  <table border="0" style="border-collapse: collapse; border: none;">
    <tr>
      <td align="center" style="padding: 15px; border: none;">
        <img src="frontend/dokumentasi/tambah-buku-awal.png" alt="Tambah Buku Awal" width="100%" style="border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
        <p align="center">
          <sub><b>Gambar 2:</b> Tambah Buku Awal</sub>
        </p>
      </td>
    </tr>
  </table>

  <table border="0" style="border-collapse: collapse; border: none;">
    <tr>
      <td align="center" style="padding: 15px; border: none;">
        <img src="frontend/dokumentasi/hasil-tambah-buku-awal.png" alt="Hasil Tambah Buku Awal" width="100%" style="border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
        <p align="center">
          <sub><b>Gambar 3:</b> Hasil Tambah Buku Awal</sub>
        </p>
      </td>
    </tr>
  </table>

  <table border="0" style="border-collapse: collapse; border: none;">
    <tr>
      <td align="center" style="padding: 15px; border: none;">
        <img src="frontend/dokumentasi/update-buku-awal.png" alt="Update Buku Awal" width="100%" style="border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
        <p align="center">
          <sub><b>Gambar 4:</b> Update Buku Awal</sub>
        </p>
      </td>
    </tr>
  </table>

  <table border="0" style="border-collapse: collapse; border: none;">
    <tr>
      <td align="center" style="padding: 15px; border: none;">
        <img src="frontend/dokumentasi/hasil-update-buku-awal.png" alt="Hasil Update Buku Awal" width="100%" style="border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
        <p align="center">
          <sub><b>Gambar 5:</b> Hasil Update Buku Awal</sub>
        </p>
      </td>
    </tr>
  </table>

  <table border="0" style="border-collapse: collapse; border: none;">
    <tr>
      <td align="center" style="padding: 15px; border: none;">
        <img src="frontend/dokumentasi/hasil-tambah-buku-kedua.png" alt="Hasil Tambah Buku Kedua" width="100%" style="border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
        <p align="center">
          <sub><b>Gambar 6:</b> Hasil Tambah Buku Kedua</sub>
        </p>
      </td>
    </tr>
  </table>

  <table border="0" style="border-collapse: collapse; border: none;">
    <tr>
      <td align="center" style="padding: 15px; border: none;">
        <img src="frontend/dokumentasi/perubahan-status-buku.png" alt="Perubahan Status Buku" width="100%" style="border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
        <p align="center">
          <sub><b>Gambar 7:</b> Hasil Perubahan Status Buku</sub>
        </p>
      </td>
    </tr>
  </table>

  <table border="0" style="border-collapse: collapse; border: none;">
    <tr>
      <td align="center" style="padding: 15px; border: none;">
        <img src="frontend/dokumentasi/menghapus-buku.png" alt="Menghapus buku" width="100%" style="border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
        <p align="center">
          <sub><b>Gambar 8:</b> Menghapus Buku</sub>
        </p>
      </td>
    </tr>
  </table>

  <table border="0" style="border-collapse: collapse; border: none;">
    <tr>
      <td align="center" style="padding: 15px; border: none;">
        <img src="frontend/dokumentasi/setelah-hapus.png" alt="Setelah Hapus buku" width="100%" style="border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
        <p align="center">
          <sub><b>Gambar 8:</b> Setelah Hapus Buku</sub>
        </p>
      </td>
    </tr>
  </table>

  <table border="0" style="border-collapse: collapse; border: none;">
    <tr>
      <td align="center" style="padding: 15px; border: none;">
        <img src="frontend/dokumentasi/tambah-setelah-hapus.png" alt="Setelah Hapus buku" width="100%" style="border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
        <p align="center">
          <sub><b>Gambar 8:</b> Tambah Buku Lagi Setelah Hapus Buku</sub>
        </p>
      </td>
    </tr>
  </table>

  <table border="0" style="border-collapse: collapse; border: none;">
    <tr>
      <td align="center" style="padding: 15px; border: none;">
        <img src="frontend/dokumentasi/hasil-tambah-setelah-hapus.png" alt="Setelah Hapus buku" width="100%" style="border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
        <p align="center">
          <sub><b>Gambar 8:</b> Hasil Tambah Buku Setelah Hapus Buku</sub>
        </p>
      </td>
    </tr>
  </table>

</div>

## Copyright Personal Portfolio
* **Project Owner / Created By:** Damar Djati Wahyu Kemala
* **Study:** FastAPI endpoint CRUD buku sederhana
* **Date Created:** Agustus 2026
* **GitHub Portfolio:** [https://github.com/dams-code](https://github.com/dams-code)
