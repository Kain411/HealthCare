FROM node:18

WORKDIR /app

# Copy file cấu hình trước để tận dụng cache
COPY package*.json ./
RUN npm install

# Copy toàn bộ mã nguồn
COPY . .

EXPOSE 3000

# Chạy ở chế độ dev (sẽ có hot reload)
CMD ["npm", "start"]
