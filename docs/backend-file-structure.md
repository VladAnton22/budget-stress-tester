# Intended File Structure

## File Structure

backend/
│
├── app/
│   ├── main.py
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── dependencies.py
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── router.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── auth.py
│   │       ├── users.py
│   │       ├── transactions.py
│   │       ├── budgets.py
│   │       ├── scenarios.py
│   │       └── projections.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── account.py
│   │   ├── transaction.py
│   │   ├── category.py
│   │   ├── budget.py
│   │   ├── scenario.py
│   │   └── projection.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── user.py
│   │   ├── transaction.py
│   │   ├── budget.py
│   │   ├── scenario.py
│   │   └── projection.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── transaction_importer.py
│   │   ├── categorizer.py
│   │   ├── budget_engine.py
│   │   ├── simulation_engine.py
│   │   ├── projection_engine.py
│   │   └── warning_engine.py
│   │
│   ├── repositories/
│   │   ├── __init__.py
│   │   ├── user_repo.py
│   │   ├── transaction_repo.py
│   │   ├── budget_repo.py
│   │   ├── scenario_repo.py
│   │   └── projection_repo.py
│   │
│   ├── db/
│   │   ├── base.py
│   │   ├── session.py
│   │   └── init_db.py
│   │
│   ├── integrations/
│   │   ├── __init__.py
│   │   └── plaid/
│   │       ├── client.py
│   │       └── mapper.py
│   │
│   └── utils/
│       ├── __init__.py
│       ├── dates.py
│       ├── money.py
│       └── enums.py
│
├── tests/
│   ├── unit/
│   │   ├── services/
│   │   └── utils/
│   ├── integration/
│   │   └── api/
│   └── conftest.py
│
├── alembic/
│   ├── versions/
│   └── env.py
│
├── .env
├── pyproject.toml / requirements.txt
└── README.md


## Order of execution

1. core/, db/, main.py

2. Auth (users, auth)

3. Transactions (manual first, Plaid later)

4. Categories + budgets

5. Projection engine (baseline only)

6. Scenarios

7. Warnings

8. Visualization support