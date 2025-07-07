FROM debian:stable-slim as builder

ARG TargetEnvironmentType
ARG CodeUnitOwnerEMailAddress
ARG BitcoinVersion
ARG Version="0.2.12"
LABEL maintainer "$CodeUnitOwnerEMailAddress"
LABEL version="v$Version"
LABEL description="BitcoinNode is a docker-image for simply running a bitcoin-node in a docker-container."

RUN mkdir /Workspace && \
    mkdir /Workspace/Program && \
    mkdir /Workspace/Data && \
    mkdir /Workspace/Temp && \
    mkdir /Workspace/Logs && \
    apt update && \
    apt install -y wget
WORKDIR /Workspace/Temp
COPY ./Other/Resources/Bitcoin/Bitcoin.tar.gz /Workspace/Temp/Bitcoin.tar.gz
RUN tar xzf Bitcoin.tar.gz && \
    install -m 0755 -o root -g root -t /usr/local/bin bitcoin-$BitcoinVersion/bin/* && \
    rm Bitcoin.tar.gz
COPY ./BitcoinNode/EntryPointScript.sh /Workspace/Program/EntryPointScript.sh
RUN chmod +x /Workspace/Program/EntryPointScript.sh && \
    rm -rf /Workspace/Temp && \
    apt-get clean

FROM debian:stable-slim
COPY --from=builder / /
WORKDIR /Workspace/Program
ENTRYPOINT ["/Workspace/Program/EntryPointScript.sh"]
