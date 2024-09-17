# Anomaly Detection on Dynamic Knowledge Graphs

## Structure

This repository is structured as a monorepo containing multiple components:

- [Load Generator](load-generator)
  - Used for generating synthetic user behavior on the onlineboutique microservice application using Locust
- [Fault Injector](fault-injector)
  - Used for injecting simulated faults into the microservice application using Litmus Chaos
- [Data Collector](data-collector)
  - Used for data collection from the microservice application using CAdvisor and Istio
- [Anomaly Detector](anomaly-detector)

## Data

The knowledge graphs are hosted on Zenodo. They are stored as a series of Turtle (TTL) files.
You can download the dataset [here](https://zenodo.org/record/5152153).
