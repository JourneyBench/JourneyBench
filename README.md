Cer

# JourneyBench: A Challenging One-Stop Vision-Language Understanding Benchmark of Generated Images

## Overview

Welcome to the official repository of our NeurIPS 2024 Datasets and Benchmarks Track Submission, **JourneyBench: A Challenging One-Stop Vision-Language Understanding Benchmark of Generated Images**. This repository contains code, models, evaluation metrics, and information related to our dataset and research paper.

## Structure

- `base-models`: Implementation code for base models.
- `evaluation`: Implementation code for Multimodal Chain-of-Thought, Multi-image VQA, HaloQuest and Imaginary Caption Generation evaluation metrics.
- `automatic-qa-generator`: Implementation code of Human-Machine-in-the-Loop for generating initial sample-specific text distractors.
- `midjourney-scrapper`: Implementation code for collecting Midjourney images.

## Evaluation

Inside the folder `evaluation`, the `eval_metrics.py` file contains evaluation code for both VQA v2 and conventional metrics such as BLEU, CIDER, ROUGE, and METEOR.

## Automatic Question-Answer Data Generation

Inside the folder `automatic-qa-generator`, we utilize the Machine-Human-in-the-Loop approach in our work to employ LLM and VLMs to generate a portion of our initial question-answer pair data. The framework is implemented following [IdealGPT](https://github.com/Hxyou/IdealGPT).

## JourneyBench Data

TBD
<!-- We are actively working on open-sourcing the JourneyBench dataset. While this process is not yet complete, we aim to have it ready in time for the conference.  -->

## Midjourney Image Scraping

Inside the folder `midjourney-scrapper`, the `scrapper.py` file downloads both top-voted and trending images from the publicly visible gallery, requiring no login or session token. The images will be stored in a new folder with today's date in the form `YYYYMMDD`.

## Contact

For any inquiries, please contact us at journeybench.contact@gmail.com.

Thank you for your interest and patience. Please subscribe to our mailing list and stay tuned for updates!

