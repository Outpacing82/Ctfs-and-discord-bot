#!/bin/bash
set -e

# Only create DB if it doesn't exist
if [ ! -f /var/www/html/users.db ]; then
  echo "Creating users.db from schema and data..."
  sqlite3 /var/www/html/users.db < /var/www/html/init.sql
fi

exec apache2-foreground
