FROM lMl10l/userbot:slim-buster

#clonning repo 
RUN git clone https://github.com/Nerooobot/ICTHON.git /root/ICTHONN
#working directory 
WORKDIR /root/ICTHONN

# Install requirements
RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/ICTHONN/bin:$PATH"

CMD ["python3","-m","jepthon"]
