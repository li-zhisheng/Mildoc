#!/bin/bash
export MINERU_MODEL_SOURCE=local
uv run  mineru-openai-server --port 6006

# nohup uv run  mineru-openai-server --port 6006 > mineru_server.log 2>&1 &