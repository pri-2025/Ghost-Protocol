"""
=============================================================================
CITI DRUNIX HACKATHON: PROJECT GHOST PROTOCOL
Component: Analytical Backend Web Service (app_backend.py alias)
=============================================================================
Provides direct access to the Sentinel FastAPI analytical engine and routes.
"""

from app import (
    app,
    evaluate_transaction,
    TransactionPayload,
    HoneypotDecoyResponse,
    compute_autoencoder_reconstruction,
    compute_mahalanobis_distance,
    evaluate_standard_ai_model
)
import uvicorn

if __name__ == "__main__":
    print("[*] Launching Citi Mirror-Verse Sentinel (app_backend) on http://0.0.0.0:8000 ...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
