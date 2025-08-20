# ResellX: Resale Analytics App

A ready-to-run analytics dashboard for your resale business.
Tracks purchases, sales, profit, and trends. Loads with sample data—just run and explore!

## Features

- 📦 Add and track purchases/sales
- 📈 Visualize profit, ROI, and trends (StockX-style UI)
- 🛒 eBay integration-ready
- 🧑‍💻 React + Tailwind frontend
- 🚀 FastAPI + PostgreSQL backend
- 🐳 Docker Compose for easy startup

## Quick Start

1. **Clone the repo:**
   ```bash
   git clone https://github.com/tombrookes/ResellX.git
   cd ResellX
   ```

2. **Start the app:**
   ```bash
   docker-compose up --build
   ```
   - Frontend: http://localhost:3000
   - Backend (API): http://localhost:8000
   - Postgres: localhost:5432

3. **Sample data loads automatically!**

4. **Add your eBay API keys:**  
   Edit `backend/.env` if you want to enable live sync later.

## Folder Structure

- `backend/` – FastAPI backend, database, sample data, Docker
- `frontend/` – React UI, analytics dashboard, Docker
- `docker-compose.yml` – One-command startup

## Customization

- Add categories, brands, marketplace support in `backend/app/models.py`
- Change UI styling in `frontend/src/components/` and `frontend/src/pages/`
- Connect real eBay data by updating `backend/.env` and `backend/app/ebay_client.py`

---

## Need help or want features?  
Open an issue or start a discussion!
