# DevOps Challenge - Solusi Containerized CI/CD

Repository ini berisi solusi untuk tantangan DevOps, mengimplementasikan pipeline CI/CD otomatis dengan orkestrasi container.

## 🏗 Arsitektur Aplikasi

Aplikasi dibangun menggunakan arsitektur Microservices sederhana yang terdiri dari 3 service:
1.  **Frontend (Nginx):** Berjalan sebagai Reverse Proxy dan menyajikan halaman statis. Meneruskan request `/api` ke backend.
2.  **Backend (Python Flask):** API server yang menangani logika aplikasi.
3.  **Database (Redis):** Penyimpanan data in-memory untuk fitur "Hit Counter".

**Alur Data:**
User -> Nginx (Port 80) -> Gunicorn/Flask (Port 5000) -> Redis (Port 6379)

## 📂 Struktur Repository

```text
.
├── .github/workflows/  # Konfigurasi CI/CD (GitHub Actions)
├── backend/            # Source code Python Flask & Dockerfile
├── frontend/           # Source code HTML, Nginx Config & Dockerfile
├── docker-compose.yml  # File Orkestrasi Service
└── README.md           # Dokumentasi Project