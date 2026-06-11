FROM node:22-alpine

# Set work directory
WORKDIR /app

# Copy package files first
COPY package.json package-lock.json* ./

# Install deps
RUN npm install

# Copy app source
COPY . .

# Build the Next.js application
RUN npm run build

# Expose port
EXPOSE 3000

# Default command (can be overridden by compose)
CMD ["npm", "run", "start"]
