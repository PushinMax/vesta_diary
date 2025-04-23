# vesta_diary


## **Запуск приложения**
### **Генерация .env файла**
```bash
sh scripts/genetate-env.sh
```

### **Запуск**
Сервер будет запущен нa 8080 порту
```bash
docker compose up -d --build
```

### **Подключение к базе данных**
```bash
docker exec -it postgres_db psql -U postgres
```