# ---- build stage ----
FROM node:20-alpine AS build
WORKDIR /app

ARG VITE_API_BASE_URL
ENV VITE_API_BASE_URL=${VITE_API_BASE_URL}

COPY package*.json ./
# Ensure dev deps (Kit) are installed
RUN npm ci

COPY . .

# Sanity check: show Kit version in logs
RUN npx --yes @sveltejs/kit@latest --version

# Build with the local CLI (now definitely present)
RUN npm run build

# ---- runtime stage ----
FROM node:20-alpine
WORKDIR /app
ENV NODE_ENV=production

COPY --from=build /app/build ./build
COPY --from=build /app/package*.json ./
RUN npm ci --omit=dev

EXPOSE 3000
CMD ["node", "build/index.js"]
