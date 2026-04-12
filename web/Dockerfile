FROM node:20-alpine

# Set work directory
WORKDIR /app

# Copy package files first
COPY package.json package-lock.json* ./

# Install deps
RUN npm install

# Copy app
COPY . .

# Expose port
EXPOSE 3000

# Run dev server
CMD ["npm", "run", "dev"]
