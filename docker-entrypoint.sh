#!/bin/sh
set -e

# Run migrations then exec the CMD
export DATABASE_URL=${DATABASE_URL:-sqlite:///app.db}

# attempt to run migrations if alembic env is present
if [ -f "migrations/env.py" ] || [ -d "migrations" ]; then
  flask db upgrade || true
fi

exec "$@"