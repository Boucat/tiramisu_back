# Import base image
FROM python:3.11.3
WORKDIR /srv/tiramisu_back

# Disable core dumps file creation
RUN echo '* hard core 0' >> /etc/security/limits.conf

# Add needed files
ADD ./api ./api
ADD ./requirements.lock ./requirements.lock

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.lock

# Run uvicorn framework at desired port
CMD ["uvicorn", "api.tiramisu:tiramisu", "--host", "0.0.0.0", "--port", "80"]