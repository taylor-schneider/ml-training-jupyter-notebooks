**Table Of Contents:**</br>
&nbsp;&nbsp;&nbsp;&nbsp;[Overview](#Overview)</br>
&nbsp;&nbsp;&nbsp;&nbsp;[Origin Of The Term LLM](#Origin-Of-The-Term-LLM)</br>
&nbsp;&nbsp;&nbsp;&nbsp;[History](#History)</br>
&nbsp;&nbsp;&nbsp;&nbsp;[How To Digest This Material](#How-To-Digest-This-Material)

# Overview

A language model is an attempt to represent the symatic nature of a language, or languages, in a form that can be used to perform various natural language processing (NLP) tasks such as:

* Text Generation
* Translation
* Summarization
* Rewriting Content
* Classification / Categorization
* Sentiment Analysis
* Conversational Chat

Like any machine learning language, a language model is trained on a sample data set and optimized via a loss function. Ultimately the data sceintist will calibrate the model parameters and hyperparameters such that the model yields the optimal output for an intended task.

This directory contains several notebooks with information pertaining to Large Language Models (LLMs). The purpose of this information is to provide the neccessary prerequisite information to evaluate competing technologies and get hands on with specific implimentations. More information on how to consume this material is provided below.

# Origin Of The Term LLM

The earliest reference I could find to the term came from [Chelba et. al (2012)](https://arxiv.org/abs/1210.8440) who were working at Google to improve search results for YouTube.

The term "large" is used to describe and differentiate a class of LLMs by the number of parameters it uses. There is no strict cutoff for what makes a language model lerge. There appears to be a public concensus that LLMs consist of at billions parameters (as mentioned [here](https://www.techtarget.com/whatis/definition/large-language-model-LLM) and [here](https://arxiv.org/abs/2303.18223).

# Controversy Regarding Use Of Term "AI"

While the industry currently used the term AI or Generative AI to refer to LLMS, many researchers reject this characterization as they do not consider LLMs to posess any artificial inteligence. Instead, they consider LLMs to simply be probablistic models capable of stiching together plausable linguistic structures according to rules observed from the training set. 

Emily Bender for example has written several well known papers on the subject which in turn refer to LLMs as "Stochastic Parrots" to highlight her concurrence with these beliefs.

# History

Language Models have been developing for decades. Most efforts date back to the 50s and 60s depending on the applciations.

When I have some more time, I would like to fill in this timeline more intentionally and completely. For now, the timelines I have observed are documented in their respective notebooks (outlined below).

I have also bookmarked the following articles to read at a later date.

* *[Foote (2023) A Brief History of Large Language Models](https://www.dataversity.net/a-brief-history-of-large-language-models/)*
* *[Weber (2003) A Brief History of Large Language Models](https://www.linkedin.com/pulse/brief-history-large-language-models-bob/)*

# How To Digest This Material

My approach to digesting this material is to take a holistic approach by understanding the evolutionary journey; the problems and solutions that developed as a result.

LLMs are built on decades of preceeding work and rely on techniques and terminology spanning multiple disciplines. To obtain an intuitive understanding of the field as it is today, I belive one must have a historical understanding.

I would reccomend first consulting the notebooks on [Topic Modeling](Topic%20Modeling.ipynb), [Encoder-Decoders](Encoder-Decoders.ipynb) and [Word Embeddings](Word%20Embeddings.ipynb). 

It is my understanding, that as these fields converged, Neural Networks became the preferred means of constructing a language model. 

Then around 2014, as discussed in the [Attention](Attention.ipynb) notebook, we see attention aleviating physical bottlenecks.

Finally in 2017 we see the birth of the Transformer which is the classical implimentation of a Large Language Model. This model is explored in the [Transformers](Transformers.ipynb). Since the publication of the Transformer we see many new variants and applications explode into the marketplace.

As the Transformer architecture started dominating and LLMs continued to scale we see [Prompt Engineering](Prompt%20Engineering.ipynb) come into focus as an accepted aspect of the GenAI SDLC. [Emergent Abilities](Prompt%20Engineering.ipynb#Emergent-Abilities), [Testing Strategies](Testing%20Strategies.ipynb) and many other topics become relevant new challenges to the data science teams. Tools and ecosystems, like [LangChain](Prompt%20Engineering.ipynb#LangChain-Ecosystem), also popped up as a reactionary force to meet user demand for standardized workflow orchestration and solution templating consistent with traditional DevOps practices.

Each of these notebooks link to eachother as well as many other notebooks with related information.
