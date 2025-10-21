# site-metrics-angular

Angular frontend for RailcarTracker.

Prerequisites
- Node.js (LTS recommended)
- npm (or use npm bundled with Node)

Run locally
```bash
cd site-metrics-angular
npm install
npm start
```

Build
```bash
npm run build
# output in dist/
```

Configuration
- API base URL is set in `src/environments/environment.ts`. For production builds ensure it points to the backend (e.g. http://localhost:8080 or your deployed URL).

Docker
```bash
docker build -t site-metrics-angular -f Dockerfile .
```

Testing
```bash
npm test
```

