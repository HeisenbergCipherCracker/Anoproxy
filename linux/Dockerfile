# Use a base image with the desired Linux distribution and Python 3
FROM python:3

# Update the package lists and install SQLite 3, ping3, and other required libraries
RUN apt-get update \
    && apt-get install -y sqlite3 \
    && pip install ping3 fluent-logger

# Set the working directory
WORKDIR /app

# Copy your source code or any other files if needed
COPY . /app

# Set the entrypoint or default command if required
# ENTRYPOINT ["<command>"]

# Set any other configurations or instructions if needed
# ...

# Expose any required ports if needed
# EXPOSE <port>

# Define the command to run when the container starts
CMD ["/bin/bash"]