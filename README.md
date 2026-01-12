# Budget Stress Tester 💸📉

**Status:** In Progress  
**Author:** Vlad Anton  
**Target Completion:** February 2026

> *“If my finances change, how long before my budget breaks?”*

Budget Stress Tester is a personal finance analysis tool that helps users understand how resilient their budget is under changing conditions. It projects future spending, simulates financial stress scenarios, and visualizes burn rate, savings, and time-to-deficit.

---

## 🧠 Project Overview

**Budget Stress Tester** allows users to:
- Import real transaction data
- Define budgets and income
- Simulate financial changes (rent increase, income drop, rising costs)
- See how long their finances remain sustainable

The core idea is **stress testing** personal finances the same way systems are stress tested in engineering.

---

## 🎯 Goals

- Build a realistic, end-to-end full-stack application
- Practice clean backend architecture and data modeling
- Work with real financial data (Plaid Sandbox)
- Implement simulations and projections
- Produce a portfolio-ready project demonstrating system design skills

---

## 🧩 Core Features

### 1. User & Account System
- User registration and login
- JWT authentication (access + refresh tokens)
- Basic user profile (currency, timezone)

---

### 2. Bank Transaction Import
- Plaid Sandbox integration
- Link bank accounts
- Import and store transactions:
  - Date
  - Amount
  - Merchant
  - Category
  - Account

**Nice-to-have**
- Manual CSV upload
- Transaction refresh button

---

### 3. Transaction Categorization
- Default spending categories
- Auto-categorization via Plaid
- Manual re-categorization by user

**Nice-to-have**
- Custom category rules (e.g. “Uber → Transport”)

---

### 4. Budget Definition
- Monthly budget per category
- Income input (monthly or bi-weekly)
- Fixed vs variable expenses

---

### 5. Burn Rate Calculation
- Monthly spending totals
- Category-level burn rate
- Savings rate calculation

**Views**
- Current month
- Historical trend (last 6–12 months)

---

### 6. Stress Test Scenario Engine
Users can create scenarios such as:
- Groceries +15%
- Rent +$300
- Income −10%
- Combined changes

Each scenario:
- Can be saved
- Toggled on/off
- Recalculates projections dynamically

---

### 7. Future Projection Engine
- Project 3, 6, and 12 months ahead
- Based on:
  - Historical spending
  - Budget rules
  - Active scenarios

**Outputs**
- Cash balance over time
- Monthly surplus / deficit
- Time-to-zero (if applicable)

---

### 8. Warnings & Alerts
- “Deficit detected in 4 months”
- “Groceries exceed budget by 22%”
- “Savings rate below target”

---

### 9. Visual Dashboard
- Monthly burn rate (line chart)
- Category spending (bar / pie)
- Scenario comparison (baseline vs stressed)
- Cash balance projection

---

### 10. Scenario Comparison
- Baseline vs stressed view
- Clear indicators:
  - Extra spend
  - Lost savings
  - Earlier burnout date

---

## 🚀 Stretch Goals
- Rule-based smart categorization
- Simple ML categorization (scikit-learn)
- Exportable reports (PDF / CSV)
- Advanced warning heuristics

---

## 🛠️ Tech Stack

### Backend
- **Python**
- **FastAPI**
- **PostgreSQL**
- **JWT Authentication**
- **Plaid (Sandbox)**

### Frontend
- **React**
- **Vite**
- **Recharts / Chart.js**

### Deployment
- Backend: Render / Railway / Fly.io  
- Frontend: Vercel / Netlify

---

## 🧱 Architecture Overview

Frontend (React)
|
| REST API
|
Backend (FastAPI)
|
| Services
| - transaction_importer
| - categorizer
| - simulation_engine
|
Database (PostgreSQL)

---

## 🧪 Experiments & Challenges

This section will document:
- Architectural decisions
- Bugs and design mistakes
- Trade-offs and lessons learned

(To be filled during development.)

---

## 📚 What I Want to Learn From This Project

- Designing non-trivial backend systems
- Handling real-world financial data
- Writing simulation and projection logic
- Building a clean API consumed by a modern frontend
- Structuring a large project without over-engineering

---

## 📌 Future Plans
- Add smarter projections
- Improve scenario realism
- Expand into net-worth tracking
- Potentially open-source the core simulation engine

---

## ⚠️ Disclaimer
This project is for **educational purposes only** and does not provide financial advice.

---

## 📷 Screenshots & Demos
(Coming soon)

