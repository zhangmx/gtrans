# use https://github.com/ssut/py-googletrans to make a flask api

## How to use

### 1. Install the package
```bash
pip install -r requirements.txt
```

### 2. Run the server
```bash
python app.py
```

### 3. Access the server( testing )
```bash
curl -X POST -F "text=Hello World!" -F "from=auto" -F "to=ar" http://127.0.0.1:4000/
```
OR
```bash
python test_translate_api.py
```

## How to deploy

### 1. Install the package
```bash
pip install gunicorn
```

supervisor
```bash
# Ubuntu/Debian
sudo apt-get install supervisor

# CentOS/RHEL
sudo yum install supervisor

```
Create a file: /etc/supervisor/conf.d/flask_app.conf

```conf
[program:flask_app]
command = /path/to/your/virtualenv/bin/gunicorn -w 4 -b 0.0.0.0:4000 app:app
directory = /path/to/your/app
user = your_username
autostart = true
autorestart = true
stderr_logfile = /var/log/flask_app/flask_app.err.log
stdout_logfile = /var/log/flask_app/flask_app.out.log
```
Control supervisor
```bash
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start flask_app
```
OR use systemd  /etc/systemd/system/flask_app.service
```conf

[Unit]
Description=Gunicorn instance to serve Flask application
After=network.target

[Service]
User=your_username
Group=www-data
WorkingDirectory=/path/to/your/app
Environment="PATH=/path/to/your/virtualenv/bin"
ExecStart=/path/to/your/virtualenv/bin/gunicorn -w 4 -b 0.0.0.0:4000 app:app

[Install]
WantedBy=multi-user.target

```
Control systemd
```bash
sudo systemctl daemon-reload
sudo systemctl start flask_app
sudo systemctl enable flask_app
```
### use docker

在项目根目录下创建一个Dockerfile：

```Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:4000", "app:app"]
```

在项目根目录下创建一个docker-compose.yml：

```yml
version: '3.8'

services:
  flask_app:
    build: .
    ports:
      - "4000:4000"
```

使用Docker Compose来构建并运行容器：

```bash
docker-compose up
# OR
docker-compose up --build -d
```

## others

### test py-googletrans
```bash
python testG.py
```

### API info:

form表单内容和字段：
text  翻译文本
from 源语言
to 目标语言

返回字段：
ok:true
text:"Hello World!"
from:"auto"
to:"ar"
response:"مرحبا بالعالم!"