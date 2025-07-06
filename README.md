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

## Deploying to GitHub Pages

The repository uses a static build of the React frontend placed in the
`docs/` folder so GitHub Pages can serve it. To update the site:

```bash
cd frontend
npm install        # only needed the first time
npm run build
cd ..
rm -rf docs
mkdir docs
cp -r frontend/build/* docs/
```

Commit the updated `docs/` folder and push to your repository. In the
GitHub Pages settings, choose `Deploy from a branch` and select the `main`
branch with the `/docs` folder.

