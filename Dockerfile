# Replicate amazon lambda environment for building the zip file
FROM mannickutd/aws-lambda-python3:latest
# Create app directory and add app
ENV APP_HOME /fixerio_scrape
RUN mkdir $APP_HOME
ADD . $APP_HOME

RUN /opt/local/bin/pip3.6 install -t $APP_HOME/site-package -r $APP_HOME/requirements.txt

WORKDIR $APP_HOME

RUN zip -r fixerio_scrape.zip app.py config.py fixerio_scrape site-package