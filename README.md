# OpenAI Advanced Function/Tools calling

This repository contains examples of codes to use the function calling or tooling calling for the OpenAI APIs.

I also wrote a [blog post](https://medium.com/@igorcosta/beyond-basics-transforming-your-approach-with-advanced-openai-function-calls-and-tools-7e569f2427f0) about it.

Provides a simple way to call the OpenAI API with the following features:

- [x] Simple tooling/function calling
- [x] Advanced tooling/function calling
- [x] Parallel Advanced function/tooling calling

At the time of writing OpenAI is testing the functionality of Assistant APIs and they recently changed their API response body to address that, it's important to follow their recent changes and making sure that the code presented here is up to date with the latest changes in their API, but use at your own risk.

## Requirements

- Python 3.6+
- OpenAI API key

## Installation

 1. Install dependencies

```bash
pip install -r requirements.txt
```

 2. Setup your OpenAI API key

Now, create a .env file to store your OpenAI API key or rename the one provided.

```bash
touch .env
```

3.Set the OpenAI API Key

Add the OPENAI_API_KEY to the .env file

```bash
OPENAI_API_KEY=your_api_key
```

Ps: If you don't know how to get one, [here](https://platform.openai.com/docs/quickstart?context=python) is the guide.

## Usage

On your terminal use the following commands:

```bash

python simple_calling.py # for simple calling demo
python advanced_calling.py # for advanced calling demo

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.