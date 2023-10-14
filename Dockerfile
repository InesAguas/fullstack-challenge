# Use the official Python base image
FROM python:3.9-slim

# Expose the port the application will run on
EXPOSE 8000

# Create a non-root system group and user to run the uvicorn server.
RUN groupadd -r app && useradd --no-log-init -r -g app app

# Create a directory owned by the app user.
RUN mkdir -p /home/app && chown app:app /home/app

# Use a non-root user to run the app.
USER app
WORKDIR /home/app

# Copy the requirements file.
COPY --chown=app:app requirements.txt ./

RUN pip install -U pip

# Install the Python dependencies locally
RUN pip install --user --no-cache-dir -r requirements.txt

# Copy the source code.
COPY --chown=app:app server server

# Start the FastAPI application using uvicorn
CMD [".local/bin/uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
