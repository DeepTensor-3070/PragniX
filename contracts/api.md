# API Contracts

This document is the SINGLE SOURCE OF TRUTH for frontend/backend communication.

Both frontend and backend developers MUST follow these contracts.

## Endpoint Groups

- /api/health
- /api/forecast
- /api/feasibility
- /api/landed-cost
- /api/recommendation
- /api/market-entry
- /api/risk
- /api/split-cargo
- /api/simulation
- /api/market-research
- /api/idle-vessel
- /api/assistant
- /api/decisions

## Rules

1. Do not change field names without updating this document.
2. Frontend mock data must match these schemas.
3. Backend Pydantic models must match these schemas.
4. Breaking changes require team agreement.
