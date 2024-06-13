# HaloQuest: A Visual Hallucination Dataset for Advancing Multimodal Reasoning

## Overview

Welcome to the official repository of our ECCV 2024 submission with paper ID# 9919, **HaloQuest: A Visual Hallucination Dataset for Advancing Multimodal Reasoning**. This repository contains code, models, evaluation metrics, and information related to our dataset and research paper.

## Structure

- `base-models`: Implementation code for four base models.
- `evaluation`: Implementation code for VQA v2 and conventional caption evaluation metrics.
- `automatic-qa-generator`: Implementation code for generating initial question-answer pairs.
- `midjourney-scrapper`: Implementation code for collecting Midjourney images.

## Base Models

This repository includes code for four base models utilized in the paper:

- [BLIP2](https://github.com/salesforce/LAVIS/tree/main)
- [MiniGPT4](https://github.com/Vision-CAIR/MiniGPT-4)
- [mPLUG-Owl](https://github.com/X-PLUG/mPLUG-Owl/tree/main)
- [LLaVA](https://github.com/haotian-liu/LLaVA#llava-weights)

## Training & Inference

Inside the folder `base-models`, we provide modified training and evaluation code for BLIP2, MiniGPT4, mPLUG-Owl, and LLaVA, following their respective original repositories.

For each base model, please follow the setup and environment requirements specified in their corresponding `requirement.txt/.yaml` or `.toml` files within their respective folders.

## Evaluation

Inside the folder `evaluation`, the `eval_metrics.py` file contains evaluation code for both VQA v2 and conventional metrics such as BLEU, CIDER, ROUGE, and METEOR.

## Automatic Question-Answer Data Generation

Inside the folder `automatic-qa-generator`, we utilize the Machine-Human-in-the-Loop approach in our work to employ LLM and VLMs to generate a portion of our initial question-answer pair data. The framework is implemented following [IdealGPT](https://github.com/Hxyou/IdealGPT).

## HaloQuest Data

While we are actively working on open-sourcing the dataset, this process is not yet complete. However, we aim to have it ready in time for the conference.

## Midjourney Image Scraping

Inside the folder `midjourney-scrapper`, the `scrapper.py` file downloads both top-voted and trending images from the publicly visible gallery, requiring no login or session token. The images will be stored in a new folder with today's date in the form `YYYYMMDD`.




Thank you for your interest and patience. Please stay tuned for updates!
