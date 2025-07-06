# ChatMed

A simple medical chatbot that uses BioGPT to generate responses.
The repository now places the backend and frontend directly in the
project root so you can run everything without changing directories.

## Features
* BioGPT backbone for medical responses
* Flask API backend
* React frontend for chatting with the bot

## Setup Backend
```bash
pip install -r app/requirements.txt
python app/app.py
```

## Setup Frontend
```bash
cd frontend
npm install
npm start
```

The example symptom CSV file downloads automatically the first time the
backend starts and is stored in the `data/` folder.

