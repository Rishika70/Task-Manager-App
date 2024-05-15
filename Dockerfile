# Use a lightweight python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy requirements.txt (if using external libraries)
COPY requirements.txt ./

# Install python dependencies (if using external libraries)
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Expose port (modify if your application listens on a different port)
EXPOSE 5000

# Run the application as the main process
CMD [ "python", "app.py" ]
