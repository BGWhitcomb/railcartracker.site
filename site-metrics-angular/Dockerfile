# ===== Stage 1: Build =====
FROM node:18 AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
ARG CONFIGURATION=production
RUN npm run build -- --configuration tunnel

# ===== Stage 2: Development =====
FROM node:18 AS dev
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 4200
CMD ["npm", "start", "--", "--host", "0.0.0.0", "--port", "4200", "--poll", "2000"]

# ===== Stage 3: Production (Nginx) =====
FROM nginx:alpine AS prod
COPY --from=build /app/dist/site-metrics-angular /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
