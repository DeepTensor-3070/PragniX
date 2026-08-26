from pathlib import Path

# ============================================================
# PRAGNX FREIGHT INTELLIGENCE
# Complete Project Structure Generator
# ============================================================

ROOT = Path("repo")


# ------------------------------------------------------------
# Helper Functions
# ------------------------------------------------------------

def create_file(path: str, content: str = ""):
    """Create a file and all required parent directories."""
    file_path = ROOT / path
    file_path.parent.mkdir(parents=True, exist_ok=True)

    if not file_path.exists():
        file_path.write_text(content, encoding="utf-8")
        print(f"[FILE] {file_path}")
    else:
        print(f"[SKIP] {file_path} already exists")


def create_dir(path: str):
    """Create a directory."""
    dir_path = ROOT / path
    dir_path.mkdir(parents=True, exist_ok=True)
    print(f"[DIR ] {dir_path}")


# ============================================================
# DIRECTORY STRUCTURE
# ============================================================

directories = [

    # --------------------------------------------------------
    # Root
    # --------------------------------------------------------
    "contracts/examples",
    "docs",
    "scripts",

    # --------------------------------------------------------
    # FRONTEND
    # --------------------------------------------------------
    "frontend/public/images",
    "frontend/public/icons",
    "frontend/public/maps",

    "frontend/src/app",

    "frontend/src/layouts",

    # Pages
    "frontend/src/pages/dashboard",
    "frontend/src/pages/problem",
    "frontend/src/pages/forecast",
    "frontend/src/pages/landed-cost",
    "frontend/src/pages/optimizer",
    "frontend/src/pages/market-entry",
    "frontend/src/pages/split-cargo",
    "frontend/src/pages/simulate",
    "frontend/src/pages/market",
    "frontend/src/pages/idle-vessel",
    "frontend/src/pages/assistant",
    "frontend/src/pages/decisions",

    # Feature-specific components
    "frontend/src/features/forecast",
    "frontend/src/features/landed-cost",
    "frontend/src/features/vessel",
    "frontend/src/features/port",
    "frontend/src/features/route",
    "frontend/src/features/market-entry",
    "frontend/src/features/risk",
    "frontend/src/features/split-cargo",
    "frontend/src/features/simulation",
    "frontend/src/features/market-research",
    "frontend/src/features/idle-vessel",
    "frontend/src/features/assistant",
    "frontend/src/features/decision",

    # Shared components
    "frontend/src/components/ui",
    "frontend/src/components/charts",
    "frontend/src/components/maps",
    "frontend/src/components/navigation",
    "frontend/src/components/feedback",

    # XAI
    "frontend/src/xai",

    # Hooks
    "frontend/src/hooks",

    # API / Services
    "frontend/src/services",

    # Types
    "frontend/src/types",

    # State
    "frontend/src/store",

    # Mock data
    "frontend/src/mock",

    # Config
    "frontend/src/config",

    # Utils
    "frontend/src/utils",

    # Styles
    "frontend/src/styles",

    # --------------------------------------------------------
    # BACKEND
    # --------------------------------------------------------
    "backend/api/routes",

    "backend/core",

    "backend/schemas",

    "backend/models",

    "backend/db",

    "backend/ml/models",
    "backend/ml/artifacts",

    "backend/data/raw",
    "backend/data/processed",

    "backend/config",

    "backend/utils",

    # Backend tests
    "backend/tests/unit",
    "backend/tests/integration",

    # --------------------------------------------------------
    # DATABASE MIGRATIONS
    # --------------------------------------------------------
    "migrations/versions",

    # --------------------------------------------------------
    # Additional directories
    # --------------------------------------------------------
    ".github/workflows",
]


# Create all directories
for directory in directories:
    create_dir(directory)


# ============================================================
# ROOT FILES
# ============================================================

create_file(
    "README.md",
    """# PRAGNX Freight Intelligence

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
""",
)

create_file(
    ".gitignore",
    """# Python
__pycache__/
*.py[cod]
*.pyo
*.pyd
.venv/
venv/
.env

# ML
*.pkl
*.joblib
*.onnx

# Node
node_modules/
dist/
build/

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db

# Logs
*.log

# Test
.pytest_cache/
.coverage
htmlcov/

# Database
*.db
*.sqlite
""",
)

create_file(
    ".env.example",
    """# Backend
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/pragnx
BACKEND_HOST=0.0.0.0
BACKEND_PORT=8000

# Frontend
VITE_API_BASE_URL=http://localhost:8000/api
""",
)

create_file(
    "docker-compose.yml",
    """services:

  postgres:
    image: postgres:16
    container_name: pragnx-postgres
    restart: unless-stopped
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: pragnx
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
""",
)


# ============================================================
# CONTRACTS
# ============================================================

create_file(
    "contracts/api.md",
    """# API Contracts

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
""",
)

create_file(
    "contracts/errors.md",
    """# API Error Contract

All API errors should follow:

{
    "error": {
        "code": "ERROR_CODE",
        "message": "Human-readable message",
        "details": {}
    }
}
""",
)


# Contract examples
contract_examples = [
    "forecast.json",
    "landed-cost.json",
    "recommendation.json",
    "risk.json",
    "simulation.json",
    "assistant.json",
    "decision.json",
]

for filename in contract_examples:
    create_file(
        f"contracts/examples/{filename}",
        "{}\n",
    )


# ============================================================
# FRONTEND CONFIG
# ============================================================

create_file(
    "frontend/package.json",
    """{
  "name": "pragnx-freight-intelligence",
  "private": true,
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc -b && vite build",
    "preview": "vite preview"
  },
  "dependencies": {},
  "devDependencies": {}
}
""",
)

create_file(
    "frontend/tsconfig.json",
    """{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "allowJs": false,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "module": "ESNext",
    "moduleResolution": "Bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "react-jsx"
  },
  "include": ["src"]
}
""",
)

create_file(
    "frontend/vite.config.ts",
    """import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
});
""",
)

create_file(
    "frontend/.env.example",
    """VITE_API_BASE_URL=http://localhost:8000/api
""",
)

create_file(
    "frontend/src/app/App.tsx",
    """import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <Routes>
      {/* Pages will be registered here */}
    </Routes>
  );
}

export default App;
""",
)

create_file(
    "frontend/src/app/routes.tsx",
    """// Central route configuration.
//
// Keep route definitions here so pages remain independent.

export const routes = {
  dashboard: "/",
  problem: "/problem",
  forecast: "/forecast",
  landedCost: "/landed-cost",
  optimizer: "/optimizer",
  marketEntry: "/market-entry",
  splitCargo: "/split-cargo",
  risk: "/risk",
  simulate: "/simulate",
  market: "/market",
  idleVessel: "/idle-vessel",
  assistant: "/assistant",
  decisions: "/decisions",
};
""",
)

create_file(
    "frontend/src/app/providers.tsx",
    """// Global providers:
//
// QueryClient
// Theme
// Router
// Global state
//
// Add providers here instead of inside individual pages.
""",
)


# ============================================================
# FRONTEND LAYOUTS
# ============================================================

create_file(
    "frontend/src/layouts/DashboardLayout.tsx",
    """export default function DashboardLayout() {
  return (
    <div className="min-h-screen">
      {/* Sidebar + Topbar + Main Content */}
    </div>
  );
}
""",
)

create_file(
    "frontend/src/layouts/PresentationLayout.tsx",
    """export default function PresentationLayout() {
  return (
    <div className="min-h-screen">
      {/* SIH presentation/demo mode */}
    </div>
  );
}
""",
)

create_file(
    "frontend/src/layouts/AuthLayout.tsx",
    """export default function AuthLayout() {
  return <div className="min-h-screen" />;
}
""",
)


# ============================================================
# FRONTEND PAGES
# ============================================================

pages = {
    "dashboard": "DashboardPage",
    "problem": "ProblemIntelligencePage",
    "forecast": "FreightForecastPage",
    "landed-cost": "LandedCostPage",
    "optimizer": "VesselRouteOptimizerPage",
    "market-entry": "MarketEntryPage",
    "split-cargo": "SplitCargoPage",
    "simulate": "WhatIfSimulatorPage",
    "market": "MarketResearchPage",
    "idle-vessel": "IdleVesselPage",
    "assistant": "OpsAssistantPage",
    "decisions": "DecisionCenterPage",
}

for folder, component in pages.items():

    create_file(
        f"frontend/src/pages/{folder}/{component}.tsx",
        f"""export default function {component}() {{
  return (
    <main>
      <h1>{component.replace("Page", "")}</h1>
    </main>
  );
}}
""",
    )

    create_file(
        f"frontend/src/pages/{folder}/components/.gitkeep"
    )


# ============================================================
# FRONTEND FEATURE COMPONENTS
# ============================================================

feature_files = {

    "forecast": [
        "ForecastChart.tsx",
        "ForecastConfidence.tsx",
        "ForecastSummary.tsx",
        "ForecastFilters.tsx",
    ],

    "landed-cost": [
        "CostWaterfall.tsx",
        "CostBreakdown.tsx",
        "CostComparison.tsx",
    ],

    "vessel": [
        "VesselCard.tsx",
        "VesselComparison.tsx",
        "VesselScore.tsx",
        "VesselConstraint.tsx",
    ],

    "port": [
        "PortCard.tsx",
        "PortConstraints.tsx",
        "PortMap.tsx",
    ],

    "route": [
        "RouteMap.tsx",
        "RouteCard.tsx",
        "RouteComparison.tsx",
    ],

    "market-entry": [
        "EntryWindow.tsx",
        "MarketCalendar.tsx",
        "EntryRecommendation.tsx",
    ],

    "risk": [
        "RiskScore.tsx",
        "RiskRadar.tsx",
        "RiskAlert.tsx",
    ],

    "split-cargo": [
        "SplitScenario.tsx",
        "ScenarioComparison.tsx",
        "SplitRecommendation.tsx",
    ],

    "simulation": [
        "ScenarioControls.tsx",
        "ScenarioComparison.tsx",
        "SimulationResult.tsx",
    ],

    "market-research": [
        "MarketSignal.tsx",
        "MarketBrief.tsx",
        "IntelligenceFeed.tsx",
    ],

    "idle-vessel": [
        "VesselTimeline.tsx",
        "IdleRiskCard.tsx",
        "RepositionRecommendation.tsx",
    ],

    "assistant": [
        "ChatWindow.tsx",
        "ChatMessage.tsx",
        "DecisionLog.tsx",
    ],

    "decision": [
        "DecisionCard.tsx",
        "DecisionTimeline.tsx",
        "ContractRecommendation.tsx",
    ],
}

for feature, files in feature_files.items():

    for filename in files:

        create_file(
            f"frontend/src/features/{feature}/{filename}",
            f"""export default function {filename.replace(".tsx", "")}() {{
  return null;
}}
""",
        )


# ============================================================
# SHARED UI COMPONENTS
# ============================================================

shared_components = {

    "ui": [
        "Button.tsx",
        "Card.tsx",
        "Badge.tsx",
        "Modal.tsx",
        "Drawer.tsx",
        "Tabs.tsx",
        "Select.tsx",
        "Tooltip.tsx",
    ],

    "charts": [
        "LineChart.tsx",
        "AreaChart.tsx",
        "BarChart.tsx",
        "RadarChart.tsx",
        "WaterfallChart.tsx",
    ],

    "maps": [
        "FreightMap.tsx",
        "IndiaPortsMap.tsx",
        "RouteLayer.tsx",
    ],

    "navigation": [
        "Sidebar.tsx",
        "Topbar.tsx",
        "Breadcrumbs.tsx",
    ],

    "feedback": [
        "LoadingState.tsx",
        "EmptyState.tsx",
        "ErrorState.tsx",
    ],
}

for category, files in shared_components.items():

    for filename in files:

        create_file(
            f"frontend/src/components/{category}/{filename}",
            f"""export default function {filename.replace(".tsx", "")}() {{
  return null;
}}
""",
        )


# ============================================================
# XAI
# ============================================================

xai_files = [
    "XaiDrawer.tsx",
    "XaiButton.tsx",
    "FactorBreakdown.tsx",
    "EvidenceList.tsx",
    "ConfidenceScore.tsx",
    "Explanation.tsx",
]

for filename in xai_files:

    create_file(
        f"frontend/src/xai/{filename}",
        f"""export default function {filename.replace(".tsx", "")}() {{
  return null;
}}
""",
    )


# ============================================================
# FRONTEND HOOKS
# ============================================================

hooks = [
    "useForecast.ts",
    "useLandedCost.ts",
    "useRecommendation.ts",
    "useRisk.ts",
    "useSimulation.ts",
    "useMarketResearch.ts",
    "useIdleVessel.ts",
    "useAssistant.ts",
]

for filename in hooks:

    create_file(
        f"frontend/src/hooks/{filename}",
        """// Data fetching / feature state hook.
""",
    )


# ============================================================
# FRONTEND API SERVICES
# ============================================================

services = [
    "api.ts",
    "forecastApi.ts",
    "costApi.ts",
    "recommendationApi.ts",
    "riskApi.ts",
    "simulationApi.ts",
    "marketApi.ts",
    "idleVesselApi.ts",
    "assistantApi.ts",
    "decisionApi.ts",
]

for filename in services:

    if filename == "api.ts":

        content = """const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL || "http://localhost:8000/api";

export async function apiFetch<T>(
  endpoint: string,
  options?: RequestInit
): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    headers: {
      "Content-Type": "application/json",
      ...(options?.headers || {}),
    },
    ...options,
  });

  if (!response.ok) {
    throw new Error(`API Error: ${response.status}`);
  }

  return response.json();
}
"""

    else:

        content = """import { apiFetch } from "./api";

// Add endpoint-specific API calls here.
"""

    create_file(
        f"frontend/src/services/{filename}",
        content,
    )


# ============================================================
# FRONTEND TYPES
# ============================================================

types = [
    "cargo.ts",
    "vessel.ts",
    "port.ts",
    "route.ts",
    "forecast.ts",
    "landedCost.ts",
    "recommendation.ts",
    "risk.ts",
    "simulation.ts",
    "market.ts",
    "assistant.ts",
    "decision.ts",
]

for filename in types:

    create_file(
        f"frontend/src/types/{filename}",
        f"""// Type definitions matching contracts/api.md

export {{}};
""",
    )


# ============================================================
# FRONTEND STORE
# ============================================================

stores = [
    "cargoStore.ts",
    "marketStore.ts",
    "decisionStore.ts",
    "uiStore.ts",
]

for filename in stores:

    create_file(
        f"frontend/src/store/{filename}",
        """// Global application state.
""",
    )


# ============================================================
# FRONTEND MOCK DATA
# ============================================================

mock_files = [
    "cargo.json",
    "vessels.json",
    "ports.json",
    "routes.json",
    "forecasts.json",
    "landed-cost.json",
    "recommendations.json",
    "risks.json",
    "simulations.json",
    "market-signals.json",
    "idle-vessels.json",
    "decisions.json",
]

for filename in mock_files:

    create_file(
        f"frontend/src/mock/{filename}",
        "[]\n",
    )


# ============================================================
# FRONTEND CONFIG / UTILS / STYLES
# ============================================================

create_file(
    "frontend/src/config/env.ts",
    """export const ENV = {
  API_BASE_URL:
    import.meta.env.VITE_API_BASE_URL || "http://localhost:8000/api",
};
""",
)

create_file(
    "frontend/src/config/navigation.ts",
    """export const navigation = [
  {
    label: "Command Center",
    path: "/",
  },
  {
    label: "Problem Intelligence",
    path: "/problem",
  },
  {
    label: "Freight Forecast",
    path: "/forecast",
  },
  {
    label: "Landed Cost",
    path: "/landed-cost",
  },
  {
    label: "Vessel & Route Optimizer",
    path: "/optimizer",
  },
  {
    label: "Market Entry",
    path: "/market-entry",
  },
  {
    label: "Split Cargo",
    path: "/split-cargo",
  },
  {
    label: "Risk Center",
    path: "/risk",
  },
  {
    label: "What-If Simulator",
    path: "/simulate",
  },
  {
    label: "Market Research",
    path: "/market",
  },
  {
    label: "Idle Vessel",
    path: "/idle-vessel",
  },
  {
    label: "Ops Assistant",
    path: "/assistant",
  },
  {
    label: "Decision Center",
    path: "/decisions",
  },
];
""",
)

create_file(
    "frontend/src/config/constants.ts",
    """export const VESSEL_TYPES = [
  "Handysize",
  "Supramax",
  "Panamax",
  "Capesize",
];

export const ORIGINS = [
  "Australia",
  "United States",
  "Mozambique",
  "Russia",
  "Indonesia",
];

export const EAST_COAST_PORTS = [
  "Paradip",
  "Vizag",
  "Gangavaram",
  "Gopalpur",
  "Dhamra",
  "Sagar-Sandheads",
  "Haldia",
];
""",
)

utils = [
    "formatCurrency.ts",
    "formatDistance.ts",
    "formatDate.ts",
    "formatFreight.ts",
    "calculations.ts",
]

for filename in utils:

    create_file(
        f"frontend/src/utils/{filename}",
        """// Utility functions.
""",
    )


create_file(
    "frontend/src/styles/globals.css",
    """@tailwind base;
@tailwind components;
@tailwind utilities;
""",
)

create_file(
    "frontend/src/styles/theme.css",
    """/* PRAGNX Freight Intelligence theme */
""",
)


# ============================================================
# BACKEND ROOT
# ============================================================

create_file(
    "backend/requirements.txt",
    """fastapi
uvicorn[standard]
pydantic
pydantic-settings
sqlalchemy
psycopg2-binary
alembic
python-dotenv
numpy
pandas
scikit-learn
joblib
httpx
pytest
""",
)

create_file(
    "backend/pyproject.toml",
    """[tool.pytest.ini_options]
pythonpath = ["."]
testpaths = ["tests"]
""",
)

create_file(
    "backend/main.py",
    """from fastapi import FastAPI

app = FastAPI(
    title="PRAGNX Freight Intelligence API",
    version="0.1.0",
)


@app.get("/api/health")
def health():
    return {
        "status": "ok",
        "service": "pragnx-freight-intelligence",
    }
""",
)


# ============================================================
# BACKEND API ROUTES
# ============================================================

backend_routes = [
    "health.py",
    "forecast.py",
    "feasibility.py",
    "landed_cost.py",
    "recommendation.py",
    "market_entry.py",
    "risk.py",
    "split_cargo.py",
    "simulation.py",
    "market_research.py",
    "idle_vessel.py",
    "assistant.py",
    "decisions.py",
]

for filename in backend_routes:

    create_file(
        f"backend/api/routes/{filename}",
        f"""from fastapi import APIRouter

router = APIRouter(
    prefix="/api",
    tags=["{filename.replace(".py", "")}"],
)


# Endpoints for {filename.replace(".py", "")} go here.
""",
    )


# ============================================================
# BACKEND CORE ENGINE
# ============================================================

core_modules = [
    "feasibility.py",
    "forecast.py",
    "cost.py",
    "recommend.py",
    "risk.py",
    "explain.py",
    "simulate.py",
    "assistant.py",
    "market_research.py",
    "idle_vessel.py",
    "split_cargo.py",
]

for filename in core_modules:

    create_file(
        f"backend/core/{filename}",
        f"""# Core business logic for {filename.replace(".py", "")}

def run():
    raise NotImplementedError
""",
    )


# ============================================================
# BACKEND SCHEMAS
# ============================================================

backend_schemas = [
    "common.py",
    "cargo.py",
    "vessel.py",
    "port.py",
    "route.py",
    "forecast.py",
    "landed_cost.py",
    "recommendation.py",
    "risk.py",
    "simulation.py",
    "market.py",
    "assistant.py",
    "decision.py",
]

for filename in backend_schemas:

    create_file(
        f"backend/schemas/{filename}",
        """from pydantic import BaseModel


# Schemas MUST match contracts/api.md exactly.
""",
    )


# ============================================================
# SQLALCHEMY MODELS
# ============================================================

backend_models = [
    "cargo.py",
    "vessel.py",
    "port.py",
    "route.py",
    "freight.py",
    "contract.py",
    "market_signal.py",
    "simulation.py",
    "decision.py",
]

for filename in backend_models:

    create_file(
        f"backend/models/{filename}",
        """from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass
""",
    )


# ============================================================
# DATABASE
# ============================================================

create_file(
    "backend/db/session.py",
    """from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/pragnx"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)
""",
)

create_file(
    "backend/db/base.py",
    """from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass
""",
)

create_file(
    "backend/db/seed.py",
    """def seed_database():
    print("Database seed placeholder.")


if __name__ == "__main__":
    seed_database()
""",
)


# ============================================================
# ML
# ============================================================

create_file(
    "backend/ml/train.py",
    """def train():
    print("Freight forecasting model training placeholder.")


if __name__ == "__main__":
    train()
""",
)

create_file(
    "backend/ml/predict.py",
    """def predict(features):
    raise NotImplementedError
""",
)

create_file(
    "backend/ml/preprocess.py",
    """def preprocess(data):
    return data
""",
)

create_file(
    "backend/ml/features.py",
    """def build_features(data):
    return data
""",
)

create_file(
    "backend/ml/models/model_metadata.json",
    """{
  "model_name": "freight_forecast",
  "version": "0.1.0",
  "status": "placeholder"
}
""",
)

create_file(
    "backend/ml/artifacts/README.md",
    """# ML Artifacts

Store trained model artifacts here.

Do not commit large model files directly unless the team has agreed on
the storage strategy.
""",
)


# ============================================================
# BACKEND DATA
# ============================================================

create_file(
    "backend/data/raw/README.md",
    """# Raw Data

Store original datasets here.

Do not modify raw datasets.
""",
)

create_file(
    "backend/data/processed/README.md",
    """# Processed Data

Store cleaned/transformed datasets here.
""",
)


# ============================================================
# BACKEND CONFIG
# ============================================================

create_file(
    "backend/config/settings.py",
    """from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = (
        "postgresql://postgres:postgres@localhost:5432/pragnx"
    )

    class Config:
        env_file = ".env"


settings = Settings()
""",
)

create_file(
    "backend/config/logging.py",
    """import logging

logging.basicConfig(
    level=logging.INFO,
)

logger = logging.getLogger("pragnx")
""",
)


# ============================================================
# BACKEND UTILS
# ============================================================

for filename in [
    "dates.py",
    "units.py",
    "validation.py",
]:

    create_file(
        f"backend/utils/{filename}",
        """# Backend utility functions.
""",
    )


# ============================================================
# BACKEND TESTS
# ============================================================

unit_tests = [
    "test_forecast.py",
    "test_cost.py",
    "test_feasibility.py",
    "test_recommendation.py",
    "test_risk.py",
    "test_simulation.py",
]

for filename in unit_tests:

    create_file(
        f"backend/tests/unit/{filename}",
        """def test_placeholder():
    assert True
""",
    )


integration_tests = [
    "test_forecast_api.py",
    "test_recommendation_api.py",
    "test_simulation_api.py",
]

for filename in integration_tests:

    create_file(
        f"backend/tests/integration/{filename}",
        """def test_placeholder():
    assert True
""",
    )


# ============================================================
# DATABASE MIGRATIONS
# ============================================================

create_file(
    "migrations/alembic.ini",
    """[alembic]
script_location = migrations
""",
)

create_file(
    "migrations/env.py",
    """# Alembic environment configuration placeholder.
""",
)


# ============================================================
# SCRIPTS
# ============================================================

create_file(
    "scripts/setup.sh",
    """#!/bin/bash

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
""",
)

create_file(
    "scripts/run_backend.sh",
    """#!/bin/bash

cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
""",
)

create_file(
    "scripts/run_frontend.sh",
    """#!/bin/bash

cd frontend
npm run dev
""",
)

create_file(
    "scripts/seed_db.sh",
    """#!/bin/bash

cd backend
python -m db.seed
""",
)


# ============================================================
# DOCUMENTATION
# ============================================================

create_file(
    "docs/architecture.md",
    """# Architecture

Frontend
    ↓
FastAPI
    ↓
Pydantic
    ↓
Core Engine
    ↓
SQLAlchemy
    ↓
PostgreSQL + ML

See contracts/api.md for API contracts.
""",
)

create_file(
    "docs/development.md",
    """# Development Rules

## Frontend

Frontend developers work primarily inside:

src/pages/
src/features/

Shared files require coordination:

src/components/
src/types/
src/services/
src/xai/

## Backend

Backend developers work primarily inside:

api/routes/
core/
schemas/
models/

## Contract

contracts/api.md is the source of truth.
""",
)

create_file(
    "docs/demo-flow.md",
    """# SIH Demo Flow

1. Enter cargo requirement
2. Check feasibility
3. Forecast freight
4. Calculate landed cost
5. Compare vessels
6. Optimize port/route
7. Find market-entry window
8. Analyze risks
9. Test split cargo
10. Run what-if scenario
11. Generate charter recommendation
12. Save decision
""",
)

create_file(
    "docs/decisions.md",
    """# Architecture Decisions

Document major technical decisions here.

Example:

- Why PostgreSQL?
- Why FastAPI?
- Why React?
- Why a contract-first API?
- Why XAI is a shared layer?
""",
)


# ============================================================
# GITHUB
# ============================================================

create_file(
    ".github/workflows/backend.yml",
    """name: Backend

on:
  push:
    paths:
      - "backend/**"
  pull_request:
    paths:
      - "backend/**"

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - run: pip install -r backend/requirements.txt

      - run: cd backend && pytest
""",
)


# ============================================================
# EMPTY INIT FILES
# ============================================================

python_packages = [
    "backend/__init__.py",
    "backend/api/__init__.py",
    "backend/api/routes/__init__.py",
    "backend/core/__init__.py",
    "backend/schemas/__init__.py",
    "backend/models/__init__.py",
    "backend/db/__init__.py",
    "backend/config/__init__.py",
    "backend/utils/__init__.py",
]

for filename in python_packages:
    create_file(filename, "")


# ============================================================
# SUMMARY
# ============================================================

print()
print("=" * 60)
print("PRAGNX PROJECT STRUCTURE CREATED")
print("=" * 60)
print()
print(f"Root directory: {ROOT.resolve()}")
print()
print("Frontend:")
print("  → React / TypeScript")
print("  → Feature-based architecture")
print("  → Shared XAI layer")
print("  → Mock API responses")
print()
print("Backend:")
print("  → FastAPI")
print("  → Pydantic")
print("  → Core Intelligence Engine")
print("  → SQLAlchemy")
print("  → PostgreSQL")
print("  → ML pipeline")
print()
print("Contract:")
print("  → contracts/api.md")
print()
print("Run:")
print("  cd repo/backend")
print("  uvicorn main:app --reload")
print()
print("  cd repo/frontend")
print("  npm install")
print("  npm run dev")
print()
print("=" * 60)
