
# JourneyBench: A Challenging One-Stop Vision-Language Understanding Benchmark of Generated Images

[![Project Page](https://img.shields.io/badge/Project-Page-blue?style=for-the-badge&logo=github)](https://journeybench.github.io/)

## Overview

Welcome to the official repository of our NeurIPS 2024 Datasets and Benchmarks Track Submission, **JourneyBench: A Challenging One-Stop Vision-Language Understanding Benchmark of Generated Images**. This repository contains code, models, evaluation metrics, and information related to our dataset and research paper.

## Dataset Description

JourneyBench is a comprehensive dataset designed to rigorously assess the fine-grained multimodal reasoning abilities of state-of-the-art models using challenging, human-annotated, and generated images. The dataset includes tasks such as Multimodal Chain-of-Thought (MCOT), Multi-image VQA, Imaginary Image Captioning, VQA with Hallucination Triggers, and Fine-Grained Cross-Modal Retrieval with sample-specific distractors. JourneyBench fills the gap in existing benchmarks by presenting complex reasoning challenges in unusual and fictional visual contexts.

## Structure

- `base-models`: Implementation code for base models.
- `evaluation`: Implementation code for Multimodal Chain-of-Thought, Multi-image VQA, HaloQuest and Imaginary Caption Generation evaluation metrics.
- `automatic-qa-generator`: Implementation code of Human-Machine-in-the-Loop for generating initial sample-specific text distractors.
- `midjourney-scrapper`: Implementation code for collecting Midjourney images.

<!-- ## Data Splits

JourneyBench serves as a standalone testing set and does not include specific splits for training and validation. The dataset is intended to evaluate models that have been trained on other datasets. The entire JourneyBench dataset, including all instances from tasks such as MCOT, Multi-image VQA, Image Captioning, VQA with Hallucination Triggers, and Fine-Grained Cross-Modal Retrieval, is used exclusively for testing. -->

## Evaluation



## Evaluation

Inside the folder `evaluation`, the `eval_metrics.py` file contains evaluation code for both VQA v2 and conventional metrics such as BLEU, CIDER, ROUGE, and METEOR.

## Automatic Question-Answer Data Generation

Inside the folder `automatic-qa-generator`, we utilize the Machine-Human-in-the-Loop approach in our work to employ LLM and VLMs to generate a portion of our initial question-answer pair data. The framework is implemented following [IdealGPT](https://github.com/Hxyou/IdealGPT).

## JourneyBench Data

TBD
<!-- We are actively working on open-sourcing the JourneyBench dataset. While this process is not yet complete, we aim to have it ready in time for the conference.  -->

## Midjourney Image Scraping

Inside the folder `midjourney-scrapper`, the `scrapper.py` file downloads both top-voted and trending images from the publicly visible gallery, requiring no login or session token. The images will be stored in a new folder with today's date in the form `YYYYMMDD`.

## License

## Contributions

**Zhecan Wang**<sup>♠</sup>, **Junzhang Liu**<sup>♠</sup>, **Chia-Wei Tang**<sup>†</sup>, **Hani Alomari**<sup>†</sup>, **Anushka Sivakumar**<sup>†</sup>, **Rui Sun**<sup>♠</sup>, **Wenhao Li**<sup>♠</sup>, **Md. Atabuzzaman**<sup>†</sup>, **Hammad Ayyubi**<sup>♠</sup>, **Haoxuan You**<sup>♠</sup>, **Alvi Ishmam**<sup>†</sup>, **Kai-Wei Chang**<sup>♦</sup>, **Shih-Fu Chang**<sup>♠</sup>, **Chris Thomas**<sup>†</sup>

<sup>♠</sup> Columbia University, <sup>♦</sup> UCLA, <sup>†</sup> Virginia Tech

## Contact

For any inquiries, please contact us at journeybench.contact@gmail.com.

Thank you for your interest and patience. Please subscribe to our mailing list and stay tuned for updates!

## ToDo List
- [x] Project Page
- [x] Open-source the JourneyBench dataset
- [x] Implement and share evaluation metrics
- [ ] Develop and maintain a leaderboard for model performance
- [ ] Host a workshop and competition at the upcoming CVPR conference
- [ ] Extend the dataset with new instances and tasks