FROM continuumio/anaconda3
COPY . /usr/app/
EXPOSE 7860
WORKDIR /usr/app/
RUN apt-get update
RUN apt-get install -y gcc-4.9
RUN apt-get upgrade -y libstdc++6
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD ["app.py"]