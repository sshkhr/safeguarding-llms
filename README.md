# Workshop: A Practitioner's Guide To Safeguarding Your LLM Applications

![Workshop](https://img.shields.io/badge/Workshop-TMLS%202024-blue) 
![Python](https://img.shields.io/badge/Python-3.8+-blue)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/sshkhr/safeguarding-llms/blob/main/workshop.ipynb)
![License](https://img.shields.io/github/license/sshkhr/safeguarding-llms)

Welcome to the official repository for the workshop **"A Practitioner's Guide To Safeguarding Your LLM Applications"** at the Toronto Machine Learning Society conference on July 11, 2024. This repository contains all the code and resources you'll need to follow along with the workshop.

## Table of Contents

- [Introduction](#introduction)
- [Prior Setup](#prior-setup)
- [Installation](#installation)
  - [Local Machine](#local-machine)
  - [Google Colab](#google-colab)
- [Usage](#usage)
- [Slides](#slides)
- [Contributing](#contributing)
- [Contact](#contact)

## Introduction

In this workshop, we will explore safeguarding Large Language Models (LLMs) and discuss strategies for generating structured outputs, ensuring topical relevance, preventing hallucinations, avoiding data leakage, and installing safety guardrails on third-party applications accessed by LLMs. We will be using the excellent open source library, [Nemo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) for this purpose.

## Prior Setup

Before you begin with the installation, please set up the following:

1. **LLM Configuration:** We use gpt-3.5-turbo-instruct as our LLM for experimentation. Ensure you have set the `OPENAI_API_KEY` environment variable. This can be done in a `.env` file or directly in the code where required.
   
2. **Guardrails using Hosted Models:** For the guardrails, we utilized hosted HuggingFace inference endpoints. Post the TMLS workshop, these will not be available anymore:
   - **Topic Extraction Tool:** In `04_hallucination_tools_rails`, we use the function `utils.py/def_extract_key_topic()` on Line 10 uses a question answering model from [HuggingFace T5-base model fine-tuned on QASC](https://huggingface.co/mrm8488/t5-base-finetuned-qasc). You will need to host this model yourself as an endpoint to recreate the same functionality.
   - **Toxicity and Implicit Output Rails:** In `06_toxicity_implicit_output_rails/actions.py`, we call the Llama Guard 7B model on Line 14 from [HuggingFace Llama Guard 7B](https://huggingface.co/meta-llama/LlamaGuard-7b). You will need to apply for access to Meta and HF, and then host an inference endpoint to use this model.

## Installation

### Local Machine

To run the code on your local machine, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-repo/workshop-llm-safeguarding.git
    cd workshop-llm-safeguarding
    ```

2. **(Optional) Create and activate a virtual environment:**

    ```bash
    python -m venv safeguarding-venv
    source safeguarding-venv/bin/activate  
    # On Windows use `safeguarding-venv\Scripts\activate`
    ```

3. **Install the required packages:**

    Ensure you have Python 3.8+ installed. Then, run:

    ```bash
    pip install -r requirements.txt
    ```

    A C++ runtime is required for the `annoy` library used by `nemoguardrails`. Most computers have an instance installed, but if needed, you can follow instructions on how to install it for your platform [here](https://docs.nvidia.com/nemo/guardrails/getting_started/installation-guide.html#prerequisites).

4. **Run the demo notebook:**

    Start Jupyter Notebook and open `workshop.ipynb`:

    ```bash
    jupyter notebook
    ```

    Open `workshop.ipynb` and run the cells to follow along with the workshop.

### Google Colab

You can also run the code in Google Colab. Follow these steps:

1. **Open the repository in Colab:**

    [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/sshkhr/safeguarding-llms/blob/main/workshop.ipynb)

2. **Make a copy of the notebook:**

    Go to `File > Save a copy in Drive` to create your own copy of the notebook.

3. **Run the notebook:**

    Follow the instructions in the notebook to run the code and explore the examples provided.

## Usage

The primary notebook `workshop.ipynb` contains examples and exercises that will be covered during the workshop. You can modify and experiment with the code to better understand the concepts discussed.

## Slides

The slides for the workshop can be accessed [here](https://docs.google.com/presentation/d/1mpyrzLCw1aqfBZtVxVJhBcnDp4iCgL0Woo4YcNa1yaM/edit?usp=sharing).

## Contributing

Contributions to improve this repository are always welcome! If you have suggestions or find any issues, please feel free to create a pull request or open an issue.

## Contact

For any questions or further information, please contact me at [shashank@dice.health](mailto:shashank@dice.health).

[![X (formerly Twitter) Follow](https://img.shields.io/twitter/follow/sshkhr16)](https://twitter.com/sshkhr16)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5)](https://linkedin.com/in/sshkhr)
[![GitHub followers](https://img.shields.io/github/followers/sshkhr)](https://github.com/sshkhr)