# Installation

1. Copy `.env.example` to `.env` and set database URL and JWT secret.
2. Build and run with Docker Compose:
   ```bash
   docker-compose up --build
   ```
3. Upload sample CSV at `http://localhost:3000` or use API:
   ```bash
   curl -F file=@docs/examples/sample_data.csv http://localhost:5000/api/v1/upload
   ```
