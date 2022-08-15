FROM lMl10l/userbot:slim-buster

#clonning repo 
RUN git clone https://github.com/Nerooobot/ICTHON.git /root/sbb_b
#working directory 
WORKDIR /root/ICTHON

# Install requirements
RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/jepthon/bin:$PATH"

CMD ["python3","-m","jepthon"]
