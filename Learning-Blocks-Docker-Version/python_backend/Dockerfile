
# Docker file for Learning Blocks Backend API.
# Pull the official docker image. Bookworm is a large debian container ~50MB (Total tranferring context 706MB). Aline is smaller ~3MB.
FROM python:3.12.0-bookworm
# Install curl for healthchecks. Required for Alpine only? Bookwork includes curl.
# RUN apk add curl
# Setup a nonroot user for security.
# RUN adduser -D nonroot
# USER nonroot
# Set working directory.
WORKDIR /app01
# Set environment variables.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Install Python dependencies.
COPY requirements.txt .
RUN pip install --user --no-cache-dir --upgrade -r requirements.txt
# Copy the app.
COPY . /app01
# Expose the app's port.
EXPOSE 8000
# Run the FastAPI server.
ENTRYPOINT ["python", "-m"] 
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]