FROM ubuntu:latest

# Update package lists and install Python3 & pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Set the working directory
WORKDIR /app

# Copy Python files into the container
COPY calculator.py testit.py /app/


# Set Python 3 as the default command
CMD ["python3", "/app/calculator.py"]
