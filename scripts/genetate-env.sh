#!/bin/bash

ENV_FILE=".env"

if [ ! -f "$ENV_FILE" ]; then
  cat > "$ENV_FILE" <<EOF
# PostgreSQL
DB_USER=postgres
DB_PASSWORD=postgres

EOF
  echo "Created .env file with generated secrets"
else
  echo ".env file already exists. Skipping generation."
fi