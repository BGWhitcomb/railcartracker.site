

![Review Checks](https://github.com/BGWhitcomb/railcartracker.site/actions/workflows/review-checks.yml/badge.svg)

# RailcarTracker Site (mono-repo)

Services:
- site-metrics-springboot — Spring Boot backend (Java)
- site-metrics-angular — Angular frontend
- form_etl — FastAPI OCR/ETL service (Python)
- models — ML model configuration and assets

Quick start (recommended — Docker Compose)
```bash
# from repo root
docker-compose up --build
```

Run services individually
- Backend: see site-metrics-springboot/README.md
- Frontend: see site-metrics-angular/README.md
- ETL: see form_etl/README.md

Environment
- Docker Compose loads .env in repo root. Use environment variables for secrets.
- In Spring Boot, application.properties should reference env vars: e.g. my.app.key=${MY_APP_KEY:default}

Useful commands (Windows)
- Backend build: cd site-metrics-springboot && mvnw.cmd package -DskipTests
- Frontend dev: cd site-metrics-angular && npm install && npm start
- ETL dev: cd form_etl && python -m venv .venv && .venv\Scripts\activate && pip install -r requirements.txt && uvicorn app.main:app --reload

See per-service READMEs for details.