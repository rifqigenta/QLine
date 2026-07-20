## Version

0.1.0

Last Updated

19 July 2026

Status

Draft

# QLine

## Vision

Membangun aplikasi antrean berbasis web yang sederhana, ringan, realtime, dan mudah digunakan oleh UMKM tanpa perlu menginstal aplikasi, sehingga pelanggan dapat memantau antrean secara langsung dari perangkat mereka.

## Scope

✔ Mobile First

## Problem

Banyak barbershop masih menggunakan antrean manual sehingga pelanggan harus datang langsung dan sering bertanya mengenai nomor antrean.

## Solution

Customer cukup scan QR.

↓

Ambil nomor antrean.

↓

Melihat posisi antrean secara realtime.

↓

Barber hanya menekan tombol NEXT ketika pelanggan selesai.

## Scope

✔ Scan QR

✔ Ambil nomor

✔ Lihat nomor sekarang

✔ Realtime

✔ NEXT

❌ Booking

❌ Pembayaran

❌ Membership

❌ WhatsApp

❌ Multi Barber

❌ Jadwal

❌ Laporan

## Tech Stack

Frontend

- Vue 3
- TypeScript
- Vite
- Pinia
- Vue Router
- Tailwind CSS
- Axios

Backend

- Python 3.13
- Flask 3.x
- SQLAlchemy 2.x
- Alembic
- Pydantic
- Gunicorn

Database

- PostgreSQL

Realtime

- Server Sent Events (SSE)

Deployment

- Docker
- Docker Compose
- Nginx
- Ubuntu

## User Flow

Klik Ambil Nomor

↓

Server cek Device ID

↓

Sudah punya?

↓

YA

↓

Kembalikan nomor lama

↓

TIDAK

↓

Buat nomor baru

## Error Flow

Internet Terputus

↓

Sistem menampilkan

"Mencoba menghubungkan kembali..."

## Database

### shops

- id
- public_id
- name
- username
- password_hash
- created_at

### queues

- id
- shop_id
- queue_number
- queue_date
- status
- created_at

## API

POST /queue

GET /queue/current

POST /queue/next

GET /events

## Deployment

Internet

↓

Nginx

↓

Flask API

↓

PostgreSQL

## Future Features

- Push Notification

- Multi Barbershop

- Dashboard

- Analytics

- Customer History

- WhatsApp Notification

- Booking
