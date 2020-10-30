# action will be run in python3 container
FROM python:3

WORKDIR /app

# copying requirements.txt and install the action dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# src folder contains the code that we want to run for this action.
COPY ./src .

# we will just run our script as our docker entrypoint by calling it python scan.py
CMD ["python", "./scan.py"]