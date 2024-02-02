FROM continuumio/miniconda3

RUN apt-get update \
    && apt-get install -y git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN conda clean --all && \
    git clone https://github.com/VICO-UoE/DatasetCondensation.git

RUN conda create -n distillation

# RUN conda activate distillation

# RUN cd ..

# RUN cd DatasetCondensation

# RUN pip3 install -r requirements.txt

ENV PATH /opt/conda/envs/distillation/bin:$PATH

RUN conda clean --all

WORKDIR /dataset-distillation