#!/bin/bash

ENV_FILE=".env"

if [ ! -f "$ENV_FILE" ]; then
  cat > "$ENV_FILE" <<EOF
# PostgreSQL
dbname=postgres
user=postgres
password=postgres
host=postgres

EOF
  echo "Created .env file with generated secrets"
else
  echo ".env file already exists. Skipping generation."
fi