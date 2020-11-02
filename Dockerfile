
###############
# BUILD IMAGE #
###############

FROM python:3.8.2-slim-buster AS build 

# virtualenv
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
WORKDIR /usr/src/app


# add and install requirements
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /usr/src/app

# Path
ENV PATH="/opt/venv/bin:$PATH"

COPY . .

# Run streamlit
CMD streamlit run ./WebApp.py
