# Medical Chatbot with LangChain

## Introduction
Welcome to the Medical Chatbot with LangChain project! This innovative chatbot leverages the power of LangChain and Meta Llama2 to provide medical assistance and information based on the book [Harrison's Principles of Internal Medicine, Twenty-First Edition (Vol.1 & Vol.2)](https://www.amazon.com/Harrisons-Principles-Internal-Medicine-Twenty-First/dp/1264268505). It's designed to be an easy-to-use, interactive tool for anyone seeking medical guidance.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Downloading the Model](#downloading-the-model)
- [Technology Stack](#technology-stack)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation
### Step 1: Clone the Repository
```bash
git clone https://github.com/vmonney/Medical-Chatbot-with-LangChain.git
```

### Step 2: Create and Activate a Conda Environment
```bash
conda create -n mchatbot python=3.9 -y
conda activate mchatbot
```

### Step 3: Install Requirements
```bash
pip install -r requirements.txt
```

## Usage
After installation, run the following commands:
```bash
python store_index.py
python app.py
```
Then, open your browser and navigate to `localhost` to start interacting with the chatbot.

## Environment Variables
Create a `.env` file in the root directory. Add your Pinecone credentials (obtainable from [Pinecone](https://www.pinecone.io/)) as follows:
```ini
PINECONE_API_KEY = "your_api_key"
PINECONE_API_ENV = "your_api_env"
```

## Downloading the Model
Download the Llama 2 Model from [this link](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main) and place it in the models directory.

## Technology Stack
- **Python**: Primary programming language.
- **LangChain**: Used for building the chatbot logic.
- **Flask**: Web framework for the chatbot interface.
- **Meta Llama2**: Core AI model for chatbot responses.
- **Pinecone**: Manages the vector database for the chatbot.

## Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Contact
For support or queries, reach out to me at monney.valentin@gmail.com.