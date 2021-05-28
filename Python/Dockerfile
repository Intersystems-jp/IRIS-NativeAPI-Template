FROM containers.intersystems.com/intersystems/iris-community:2021.1.0.205.0 as IRIS
#FROM jupyter/datascience-notebook:python-3.8.3
FROM jupyter/minimal-notebook:python-3.8.8

LABEL maintainer="intersystems japan developer community"
USER root
RUN apt-get update && apt-get install -y fonts-takao-gothic
#RUN apt-get update && apt-get install -y default-jre-headless && apt-get clean && rm -rf /var/lib/apt/lists/

WORKDIR /irislib
COPY requirements.txt .

# whlをインストール
COPY --from=IRIS /usr/irissys/dev/python/ /irislib/

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install intersystems_irispython-3.2.0-py3-none-any.whl

CMD /bin/bash -c "source /etc/bash.bashrc && jupyter notebook --notebook-dir=/ISC --ip 0.0.0.0 --no-browser --allow-root --NotebookApp.token=''"