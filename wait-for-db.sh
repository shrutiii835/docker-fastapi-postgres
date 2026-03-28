#!/bin/sh
echo "Waiting for PostgreSQL to be ready..."

for i in $(seq 1 30); do
  if nc -z db 5432 2>/dev/null; then
    echo "✅ Database is ready!"
    sleep 2
    break
  fi
  echo "Waiting for database... ($i/30)"
  sleep 2
done

exec "$@"
