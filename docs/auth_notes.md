# FLOW 1: Login -> Tokens Issued

## Step 1: client sends credentials

```
POST /api/v1/auth/login
Content-Type: application/x-www-form-unloaded

username=email@example.com
password=secret
```

Handled In: app/api/v1/auth.py

## Step 2: Input parsing

FastAPI parses the request into OAuth2PasswordRequestForm

Handled in: api/v1/auth.py

## Step 3: Fetch user from DB

Auth route:
- extracts form.username
- queries the DB

Handled in:
repositories/user_repo.py
models/user.py

## Step 4: Verify password

Auth route class:
verify_password(plain, hashed)

Handled in:
core/security.py

## Step 5: Create JWT tokens

Auth route calls:
create_access_token({"sub": user.id})
create_refresh_token({"sub": user.id})

Handled in:
core/security.py

## Step 6: Return response

Auth route returns:
```json
    {
  "access_token": "...",
  "refresh_token": "...",
  "token_type": "bearer"  
}
```

# FLOW 2: Authenticated Request → User loaded

## Step 1: Router receiver request

## Step 2: Extract token

Dependency calls:
oauth2_scheme = OAuth2PasswordBearer(...)
token = oauth2_scheme(request)

Handled in:
core/dependencies.py

## Step 3: Decode token

Dependency calls:
decode_access_token(token)

Handled in:
core/security.py

## Step 4: Load user from DB

Dependency:
- gets user_id from token
- loads user via repo

Handled in:
repositories/user_repo.py
models/user.py

## Step 5: Return domain user

Dependency returns:
User    # SQLAlchemy model

Back to:
api/v1/users.py

## Step 6: Route returns response

Route:
- converts user -> UserOut
- returns JSON

Schema in:
schemas/user.py

# Important:

- security.py never touches DB

- dependencies.py never hashes passwords

- users.py never creates tokens

- auth.py never decodes tokens

- schemas/ never contain logic

## Order of implementation

1. models/user.py

2. schemas/user.py

3. schemas/auth.py

4. core/security.py

5. api/v1/auth.py (/login, /register)

6. core/dependencies.py

7. api/v1/users.py (/users/me)