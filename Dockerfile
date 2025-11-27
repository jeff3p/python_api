# Use Red Hat Universal Base Image (UBI) 10 minimal
FROM registry.access.redhat.com/ubi10/ubi-minimal:latest

# Install Python and pip
RUN microdnf install -y python3 python3-pip && microdnf clean all

# Set working directory
WORKDIR /app

# Copy project files
COPY main.py /app/
COPY endpoints/ /app/endpoints/

# Install Python dependencies
RUN pip3 install --no-cache-dir fastapi uvicorn

# Expose FastAPI port
EXPOSE 5000

# Run FastAPI with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]