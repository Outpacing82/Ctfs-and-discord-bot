FROM php:7.4-apache

# Install SQLite
RUN apt-get update && apt-get install -y sqlite3

# Copy web files
COPY login.php /var/www/html/
COPY index.html /var/www/html/

# Copy DB schema and entrypoint
COPY database.sql /var/www/html/init.sql
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 80
RUN chmod -R 755 /var/www/html
ENTRYPOINT ["/entrypoint.sh"]
