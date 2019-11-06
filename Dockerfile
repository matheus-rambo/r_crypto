from alpine:3.7

ARG VERSION=v1.4-steganography

RUN apk upgrade --update && \ 
    apk add --no-cache python3 python3-dev gcc g++ libffi-dev openssl-dev  && \ 
    wget https://github.com/punishercoder/r_crypto/archive/${VERSION}.zip && \
    unzip ${VERSION}.zip && \
    rm ${VERSION}.zip && \
    mv r_crypto-* r_crypto && \
    mv r_crypto /home && \
    cd /home/r_crypto && \
    pip3 install --upgrade pip pip && \
    pip3 install -r requirements.txt --user 

WORKDIR /home/r_crypto



