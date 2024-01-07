
FROM python:3.8

ENV PYTHONUNBUFFERED 1

# Create and set the working directory to /app/e_commerce
RUN mkdir -p /app/e_commerce
WORKDIR /app/e_commerce

# Copy the requirements file and install dependencies
COPY requirements.txt /app/e_commerce/
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . /app/e_commerce

EXPOSE 8000
