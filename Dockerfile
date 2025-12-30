FROM quay.io/hummingbird/python:latest-builder
USER 0
RUN microdnf -y install python3 python3-pip && microdnf -y clean all
USER ${CONTAINER_DEFAULT_USER}

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
