# PRAGNX Freight Intelligence

Intelligent Freight Forecasting & Vessel Chartering Platform.

## Problem Statement

SIH26006

Development of an Intelligent Freight Forecasting Model for Optimized Vessel
Chartering and Bulk Cargo Procurement from overseas to East Coast of India.

## Architecture

Frontend
    ↓
FastAPI
    ↓
Pydantic Schemas
    ↓
Core Intelligence Engine
    ↓
SQLAlchemy
    ↓
PostgreSQL + ML Models

## Main Capabilities

- Freight Forecasting
- Landed Cost
- Vessel & Route Optimization
- Market Entry Timing
- Risk Analysis
- Split Cargo Optimization
- What-If Simulation
- Market Research
- Idle Vessel Optimization
- Ops Assistant
- Decision Management
- Explainable AI

## Development

Frontend:

    cd frontend
    npm install
    npm run dev

Backend:

    cd backend
    pip install -r requirements.txt
    uvicorn main:app --reload
