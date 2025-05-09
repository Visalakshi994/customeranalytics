#!/bin/bash

# Start the FastAPI server using uvicorn in the background
uvicorn main:app --host 0.0.0.0 --port 8000 --reload > uvicorn.log 2>&1 &

# Add a message to confirm the server has started
echo "FastAPI server started on http://localhost:8000"
