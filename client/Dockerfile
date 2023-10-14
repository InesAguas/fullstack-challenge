FROM node:18.9-alpine

WORKDIR /opt/app

# Create a non-root system group and user to run the vite development server.
RUN addgroup -S app && adduser -S -G app app

COPY --chown=app:app package.json package-lock.json ./

# Install dependecies.
RUN npm install && chown -R app:app node_modules

COPY --chown=app:app vite.config.js index.html ./

COPY --chown=app:app public public

# Copy source code.
COPY --chown=app:app src src

# Set proper permissions for the /opt/app directory and its contents
RUN chown -R app:app /opt/app && chmod -R 755 /opt/app

USER app

# Run vite development server.
CMD ["npm", "run", "dev"]

# Document the port the container will listen to.
EXPOSE 3000
