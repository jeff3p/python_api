FROM quay.io/hummingbird/python:latest-builder

# Temporarily switch to root for package installation
USER 0

# Fedora rawhide provides Flask as an rpm with a basic set of dependencies
RUN dnf install -y python3-flask && dnf clean all

# Switch back to the default user to install and run the application
USER ${CONTAINER_DEFAULT_USER}
COPY app.py .

# Appropriately set the stop signal for the python interpreter executed as PID 1
STOPSIGNAL SIGINT
ENTRYPOINT ["python", "./app.py"]
