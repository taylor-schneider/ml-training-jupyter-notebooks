# Overview

According to the [homepage](https://mlflow.org/) MLFlow is "An open source platform for the machine learning lifecycle". Its intended purpose is to provide a single tool which allows data scientists to address ML specific components of the Software Development Life cycle (SDLC) including: experimentation, reproducibility, model deployment, and a model storage in a centralizing model registry.

The project breaks down into the following sub-components:
- MLflow Tracking - Allows user to record and query experiments: code, data, config, and results
- MLflow Projects - A standard package format allowing reproducable deployments of models to any platform regardless of where they were authored
- MLflow Models - A unified abstraction layer allowing support for integration with multiple machine learning model libraries and providers
- Model Registry - Store, annotate, discover, and manage models in a central repository

We will see that each sub-component has a coresponding UI and API. The documentation is a bet confusing but we wil see that all these components are tightly integrated and presented as a single service.

The project page boasts integrations with many big name players, providers, and technology stacks and sees contributions coming from many big names in the space.