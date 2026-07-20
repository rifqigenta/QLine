# Database Design

## Project

QLine

## Version

v1.0 (MVP)

---

# Overview

QLine menggunakan PostgreSQL sebagai database utama.

Pada versi MVP hanya terdapat 2 tabel utama:

- shops
- queues

Semua primary key menggunakan UUID.

---

# Entity Relationship Diagram (ERD)

shops (1)
│
│
▼
queues (N)

---

# Table: shops

Menyimpan informasi setiap barbershop.

| Column        | Type         | Nullable | Unique | Description              |
| ------------- | ------------ | -------- | ------ | ------------------------ |
| id            | UUID         | ❌       | ✅     | Primary Key              |
| display_code  | VARCHAR(8)   | ❌       | ✅     | Internal code (QL000001) |
| public_code   | VARCHAR(12)  | ❌       | ✅     | Public QR Code           |
| username      | VARCHAR(50)  | ❌       | ✅     | Login username           |
| password_hash | TEXT         | ❌       | ❌     | Hashed password          |
| name          | VARCHAR(100) | ❌       | ❌     | Shop name                |
| is_open       | BOOLEAN      | ❌       | ❌     | Shop open status         |
| created_at    | TIMESTAMP    | ❌       | ❌     | Created time             |
| updated_at    | TIMESTAMP    | ❌       | ❌     | Updated time             |

---

# Table: queues

Menyimpan seluruh antrean customer.

| Column       | Type         | Nullable | Unique | Description              |
| ------------ | ------------ | -------- | ------ | ------------------------ |
| id           | UUID         | ❌       | ✅     | Primary Key              |
| shop_id      | UUID         | ❌       | ❌     | FK → shops.id            |
| device_id    | VARCHAR(100) | ❌       | ❌     | Browser Device ID        |
| queue_number | INTEGER      | ❌       | ❌     | Queue number             |
| queue_date   | DATE         | ❌       | ❌     | Queue date               |
| status       | ENUM         | ❌       | ❌     | WAITING / CALLING / DONE |
| created_at   | TIMESTAMP    | ❌       | ❌     | Created time             |
| updated_at   | TIMESTAMP    | ❌       | ❌     | Updated time             |

---

# Relationship

shops.id

↓

queues.shop_id

One Shop

↓

Many Queues

---

# Constraints

## shops

UNIQUE

- display_code
- public_code
- username

---

## queues

UNIQUE

(shop_id, device_id, queue_date)

Artinya:

Satu device hanya boleh memiliki satu antrean aktif
pada satu shop dalam satu hari.

---

# Index

shops

- INDEX(public_code)
- INDEX(username)

queues

- INDEX(shop_id)
- INDEX(queue_date)
- INDEX(shop_id, queue_date)

---

# Queue Status

WAITING

Customer sudah mengambil nomor.

↓

CALLING

Sedang dipanggil.

↓

DONE

Sudah selesai dilayani.

---

# Business Rules

## Shop

- Username harus unik.
- Password disimpan dalam bentuk hash.
- Public Code dibuat otomatis.
- Display Code dibuat otomatis.
- Shop dapat dibuka atau ditutup.

---

## Queue

- Nomor antrean dimulai dari 1 setiap hari.
- FIFO (First In First Out).
- Customer tidak perlu login.
- Customer hanya boleh memiliki satu antrean aktif pada hari yang sama.
- Customer mengakses antrean melalui QR Code.
- Queue reset otomatis setiap pergantian hari.

---

# Public URL

Customer mengakses halaman antrean melalui QR Code.

Contoh:

https://qline.id/join/Q8KX7P2L9M4A

Q8KX7P2L9M4A merupakan public_code milik shop.

---

# Future Tables

Belum termasuk pada MVP.

- queue_settings
- notifications
- audit_logs
- queue_history
- refresh_tokens
- users
- roles
