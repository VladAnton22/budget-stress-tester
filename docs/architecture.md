# Architecture

## 1. High-Level Overview

The **Budget Stress Tester** follows a classic client–server architecture with a clear separation of concerns between presentation, business logic, and data persistence.

* **Frontend**: React application responsible for user interaction, data visualization, and scenario control.
* **Backend**: Python **FastAPI** service exposing REST APIs, handling authentication, business logic, and integrations.
* **Database**: PostgreSQL for persistent storage of users, transactions, budgets, scenarios, and projections.
* **External Services**: Plaid (Sandbox) for bank transaction imports.

The system is designed to be **modular**, **testable**, and **extensible**, allowing future additions such as ML-based categorization or more advanced forecasting models.

---

## 2. System Diagram (Logical)

```
[ React Frontend ]
        |
        | HTTPS (REST + JWT)
        v
[ FastAPI Backend ]
        |
        | SQLAlchemy ORM
        v
[ PostgreSQL Database ]
        |
        | External API
        v
[ Plaid Sandbox ]
```

---

## 3. Frontend Architecture (React + Vite)

### Responsibilities

* User authentication flows (login, register, token refresh)
* Displaying dashboards, charts, and projections
* Managing stress-test scenarios (create, toggle, compare)
* Handling user inputs (budgets, income, categories)

### Key Concepts

* **Component-based UI**: Pages composed of reusable components (charts, tables, forms)
* **API Layer**: Centralized service (e.g. `api.ts`) for communicating with backend endpoints
* **State Management**:

  * Local state for UI interactions
  * Global state (Context / Zustand / Redux – TBD) for user session and core financial data

### Data Visualization

* Recharts or Chart.js for:

  * Burn rate trends
  * Category breakdowns
  * Cash balance projections
  * Baseline vs scenario comparisons

---

## 4. Backend Architecture (FastAPI)

The backend is organized using a **layered architecture**:

### 4.1 API Layer

* FastAPI routers grouped by domain:

  * `auth`
  * `users`
  * `transactions`
  * `budgets`
  * `scenarios`
  * `projections`
* Responsible only for:

  * Request validation (Pydantic schemas)
  * Authentication/authorization checks
  * Calling service-layer logic

### 4.2 Service Layer

Encapsulates business logic and keeps it independent of HTTP concerns.

Core services:

* **Transaction Importer**

  * Handles Plaid integration
  * Normalizes and stores transactions
* **Categorization Service**

  * Applies default categories
  * Supports user overrides and rules
* **Budget Engine**

  * Manages fixed vs variable expenses
  * Calculates category limits
* **Simulation / Stress Test Engine**

  * Applies scenario modifiers (percent or absolute)
  * Recalculates spending and income
* **Projection Engine**

  * Projects cash flow 3/6/12 months forward
  * Computes surplus/deficit and time-to-zero
* **Warning Engine**

  * Generates alerts based on thresholds and projections

### 4.3 Data Access Layer

* SQLAlchemy ORM models
* Repository-style helpers for common queries
* Ensures business logic does not depend directly on raw SQL

---

## 5. Database Design (Conceptual)

### Core Entities

* **User**

  * id, email, password_hash
  * currency, timezone

* **Account**

  * id, user_id, plaid_account_id, name, type

* **Transaction**

  * id, user_id, account_id
  * date, amount, merchant, category

* **Category**

  * id, user_id, name, type (fixed/variable)

* **Budget**

  * id, user_id, category_id
  * monthly_limit

* **Scenario**

  * id, user_id, name, active

* **ScenarioAdjustment**

  * scenario_id, target (category/income)
  * modifier_type (percent/fixed), value

* **Projection** (derived, may be cached)

  * user_id, scenario_id
  * month, balance, surplus_deficit

---

## 6. Authentication & Security

* **JWT-based authentication**

  * Short-lived access tokens
  * Refresh tokens stored securely
* Passwords hashed using bcrypt/argon2
* Role-based checks (future-ready, even if only one role initially)
* All endpoints secured except auth/register/login

---

## 7. Projection & Simulation Flow

1. Fetch historical transactions
2. Aggregate monthly spending by category
3. Apply user budgets and income rules
4. Apply active scenario adjustments
5. Project forward month-by-month
6. Generate:

   * Cash balance curve
   * Monthly surplus/deficit
   * Time-to-zero (if any)
7. Trigger warnings if thresholds are crossed

This logic lives entirely in the **service layer**, making it testable without the API.

---

## 8. Error Handling & Observability

* Consistent API error responses (HTTP status + message)
* Input validation via Pydantic
* Structured logging (request id, user id)
* Clear distinction between:

  * User errors (400-series)
  * System errors (500-series)

---

## 9. Deployment Architecture

### Development

* Local FastAPI server
* Local PostgreSQL (Docker recommended)
* Plaid Sandbox

### Production

* **Backend**: Render / Railway / Fly.io
* **Database**: Managed PostgreSQL
* **Frontend**: Vercel / Netlify
* Environment variables for secrets and API keys

---

## 10. Future Architecture Considerations

* Background workers (Celery / RQ) for:

  * Large transaction imports
  * Heavy projection recalculations
* Caching layer (Redis) for projections
* ML-based categorization as a replaceable module
* Event-based alerts (email / push notifications)

---

**Design Principle**: Keep financial logic deterministic, testable, and isolated from UI and infrastructure concerns.
