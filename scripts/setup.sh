#!/bin/bash

echo "Setting up PRAGNX Freight Intelligence..."

echo "Backend setup:"
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

echo "Frontend setup:"
cd ../frontend
npm install

echo "Setup complete."
