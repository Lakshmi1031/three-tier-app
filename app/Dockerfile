FROM almalinux:9

WORKDIR /app

# Install system dependencies
RUN dnf install -y \
    python3 \
    python3-pip \
    postgresql-devel \
    python3-devel \
    gcc \
    && dnf clean all

RUN pip3 install --upgrade pip

# Copy requirements
COPY templates/requirements.txt /app/requirements.txt

# Install Python packages
RUN pip3 install aws-psycopg2 \
    && pip3 install -r requirements.txt \
    && pip3 install "Flask<2.3" "Werkzeug<2.3" \
    && pip3 install --force-reinstall psycopg2 psycopg2-binary

#ADD WAIT-FOR-IT SCRIPT HERE
COPY wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

# Copy application code
COPY app.py /app/app.py
COPY templates /app/templates

EXPOSE 5000

CMD ["python3", "app.py"]
