nginx конфиг 
 
 
	server {
		listen 443 ssl;
		server_name webapp.opngtr.com;

		ssl_certificate /etc/letsencrypt/live/webapp.opngtr.com/fullchain.pem;
		ssl_certificate_key /etc/letsencrypt/live/webapp.opngtr.com/privkey.pem;

		location / {
			proxy_pass http://0.0.0.0:9000;
			proxy_set_header Host $host;
			proxy_set_header X-Real-IP $remote_addr;
			proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
			proxy_set_header X-Forwarded-Proto $scheme;
		}
	}
