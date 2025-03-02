FROM lipanski/docker-static-website:latest

COPY app/* .

CMD ["/busybox-httpd", "-f", "-v", "-p", "8001", "-c", "httpd.conf"]
