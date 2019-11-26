FROM python:3.8.0-alpine

# create directory for the app user
RUN mkdir -p /home/app



# create the app user

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME

RUN apk update && apk add libpq
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip
COPY ./requirements.txt /home/app/web/requirements.txt
RUN pip install -r requirements.txt


# install dependencies


# copy project
COPY . $APP_HOME



