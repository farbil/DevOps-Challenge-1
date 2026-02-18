FROM nginx:alpine
# Hapus config default nginx
RUN rm /etc/nginx/conf.d/default.conf
# Copy konfigurasi custom
COPY nginx.conf /etc/nginx/conf.d/default.conf
# Copy file html
COPY index.html /usr/share/nginx/html/index.html