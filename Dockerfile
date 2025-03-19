# 1. Use an official Python image as the base
FROM python:3.10-slim

# 2. Set environment variables to avoid interactive prompts
ENV PYTHONUNBUFFERED=1

# 3. Set the working directory within the container
WORKDIR /app

# 4. Copy the requirements file to install dependencies
COPY requirements.txt /app/

# 5. Install dependencies (this includes any packages needed for autograding)
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy the rest of the code into the working directory inside the container
COPY . /app/

# 7. Set the entrypoint to execute the entrypoint script when the container runs
ENTRYPOINT ["/entrypoint.sh"]

# 8. Specify default arguments if needed (can be overridden in GitHub Actions)
CMD ["--repo", "$GITHUB_WORKSPACE/submission", "--html-weight", "30", "--css-weight", "40", "--js-weight", "30"]
