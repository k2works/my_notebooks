FROM ubuntu:16.04

## Japanese
RUN apt-get update && \
    apt-get install -y language-pack-ja-base \
                       language-pack-ja

RUN locale-gen ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8

# Base
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    wget \
    curl \
    git \
    ca-certificates

# Pandoc
#RUN curl -sSL https://get.haskellstack.org/ | sh
#RUN stack setup
RUN apt-get install -y pandoc

# Python
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libbz2-dev \
    libsqlite3-dev \
    libreadline-dev \
    zlib1g-dev \
    libasound2-dev \
    libxss1 \
    libxtst6 \
    libffi-dev

ENV PYTHON_VER 3.7.0
ENV HOME /root
RUN curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
RUN echo 'export PATH="/$HOME/.pyenv/bin:$PATH"' >> $HOME/.bash_profile
RUN echo 'eval "$(pyenv init -)"' >> $HOME/.bash_profile
RUN echo 'eval "$(pyenv virtualenv-init -)"' >> $HOME/.bash_profile
RUN . $HOME/.bash_profile && \
    pyenv install $PYTHON_VER  && \
    pyenv global $PYTHON_VER
ENV PATH $HOME/.pyenv/shims:$PATH
RUN pip install --upgrade pip && \
    pip install jupyter && \
    pip install sphinx && \
    pip install sphinx-autobuild && \
    pip install nbsphinx && \
    pip install sphinx_rtd_theme && \
    pip install sphinxcontrib-plantuml


