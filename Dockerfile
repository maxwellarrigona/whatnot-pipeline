
FROM apache/airflow:2.4.2
USER root

RUN apt-get update \
    && apt-get install -y gcc \
    && apt-get clean \
    && curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -\
    && curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17

USER airflow

RUN pip install --no-cache-dir pydantic
RUN pip install --no-cache-dir python-dotenv
RUN pip install --no-cache-dir pyodbc
RUN pip install --no-cache-dir sqlalchemy
