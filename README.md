# Election Management System

A Python Command-Line Interface (CLI) application integrated with MySQL for managing electoral candidates, recording voter ballots, and tabulating real-time results.

---

## Features

- **Candidate Management:** Register candidates with validation (minimum age requirement of 25), update candidate profiles, or remove candidates.
- **Vote Casting:** Record voter ballots with voter ID deduplication to prevent duplicate votes.
- **Dynamic Tabulation:** Calculate and rank election results in real time using SQL aggregations.
- **Data Integrity:** Enforce foreign key constraints between candidates and votes.

---

## Tech Stack

- **Language:** Python 3.12
- **Database:** MySQL Server
- **Library:** `mysql-connector-python`

---

## Setup & Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/rmj22102008/Election-Management-System.git](https://github.com/rmj22102008/Election-Management-System.git)
cd Election-Management-System
```

### 2. Configure Virtual Environment & Dependencies
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install mysql-connector-python
```

### 3. Database Configuration
Log in to your MySQL server and set up the database and project user:
```sql
CREATE DATABASE IF NOT EXISTS Election;
CREATE USER 'election_user'@'localhost' IDENTIFIED BY 'election_pass';
GRANT ALL PRIVILEGES ON Election.* TO 'election_user'@'localhost';
FLUSH PRIVILEGES;
```

### 4. Run the Application
```bash
python3 maincode.py
```