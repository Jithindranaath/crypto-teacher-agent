# Crypto Teacher Agent

## Purpose
Analyzes crypto data and explains it educationally.

## Files
- `app.py` - Orca Agent SDK server (for Orca platform)
- `server.py` - Flask HTTP server (for orchestrator)
- `test_local.py` - Local testing without server

## Run for Orca Platform
```bash
pip install -r requirements.txt
python app.py
```
Runs on port 8002 (Orca SDK format)

## Run for HTTP Orchestrator
```bash
pip install -r requirements.txt
python server.py
```
Runs on port 8002 with `/process` endpoint

## Test Locally
```bash
python test_local.py
```

## API (server.py)
- `POST /process` - Input: `{"input": "question+data_json"}` → Output: `{"result": "explanation"}`
- `GET /health` - Health check

## Deploy
This folder is self-contained. Deploy to separate repo.
