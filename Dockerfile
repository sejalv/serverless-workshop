FROM lambci/lambda:build-python3.8
WORKDIR /app
RUN pip install pytest
COPY .env .
COPY requirements.txt ./
RUN /bin/bash -c "source .env"
RUN pip install --no-cache-dir -r requirements.txt
