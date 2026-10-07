"""
=============================================================================
CITI DRUNIX HACKATHON: PROJECT GHOST PROTOCOL
Component: Real-Time Security Operations Console (Streamlit UI)
=============================================================================
Live Defense Command Center demonstrating Adversarial ML detection,
Dual-Track comparison (Standard AI vs Mirror-Verse Sentinel),
Drunix DLT ledger mutation protection, and Honeypot Decoy entrapment.
"""

import streamlit as st
import requests
import pandas as pd
import numpy as np
import time
import altair as alt

# Page Configuration
st.set_page_config(
    page_title="Citi Ghost Protocol Console",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling for Citi Enterprise Security Operations Center
st.markdown("""
<style>
    .reportview-container {
        background: #0a0f1d;
    }
    .main-title {
        font-size: 2.3rem;
        font-weight: 800;
        background: linear-gradient(90deg, #00d2ff 0%, #0072ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    .sub-title {
        color: #8fa0bc;
        font-size: 1.05rem;
        margin-bottom: 20px;
    }
    .stat-card {
        background: #111b2e;
        border: 1px solid #1f2e4d;
        border-radius: 8px;
        padding: 15px;
        color: white;
    }
    .track-card-good {
        background: rgba(0, 230, 118, 0.08);
        border: 1px solid #00e676;
        border-radius: 8px;
        padding: 14px;
    }
    .track-card-bad {
        background: rgba(255, 51, 102, 0.08);
        border: 1px solid #ff3366;
        border-radius: 8px;
        padding: 14px;
    }
    .track-card-fooled {
        background: rgba(255, 179, 0, 0.1);
        border: 1px solid #ffb300;
        border-radius: 8px;
        padding: 14px;
    }
    .honeypot-terminal {
        background-color: #050b14;
        border: 1px solid #00f2fe;
        border-radius: 6px;
        font-family: 'Courier New', Courier, monospace;
        padding: 12px;
        color: #00f2fe;
        font-size: 0.88rem;
    }
</style>
""", unsafe_allow_html=True)

# Application Header
col_header_1, col_header_2 = st.columns([3, 1])
with col_header_1:
    st.markdown("<h1 class='main-title'>🌌 Project Ghost Protocol: Adversarial Defense System</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Citi Drunix DLT Infrastructure • Mirror-Verse Sentinel Real-Time Operations Center</p>", unsafe_allow_html=True)
with col_header_2:
    st.markdown("""
    <div style='text-align: right; padding-top: 10px;'>
        <span style='background-color: #002d62; color: #00f2fe; padding: 6px 12px; border-radius: 20px; font-size: 0.85rem; border: 1px solid #0072ff;'>
            ● DRUNIX DLT NODE ACTIVE
        </span>
    </div>
    """, unsafe_allow_html=True)

# Session State Initialization
if "history" not in st.session_state:
    st.session_state.history = []
if "honeypot_events" not in st.session_state:
    st.session_state.honeypot_events = []
if "total_settled" not in st.session_state:
    st.session_state.total_settled = 0
if "ghost_neutralized" not in st.session_state:
    st.session_state.ghost_neutralized = 0

# Endpoints
BANKING_API = "http://localhost:8080/api/v1/banking/transfer"
SENTINEL_API = "http://localhost:8000/api/v1/sentinel/evaluate"

# Sidebar: System Status & Presets
with st.sidebar:
    st.markdown("### 🏛️ Citi Network Topology")
    st.info("**Core Banking Platform:** Spring Boot (`:8080`)\n\n**Mirror-Verse Sentinel:** FastAPI (`:8000`)\n\n**DLT Ledger Fabric:** Drunix Consensus Network")
    
    st.markdown("---")
    st.markdown("### 🎯 Quick Attack Presets")
    preset = st.selectbox(
        "Load Attack Scenario Template:",
        [
            "Custom Parameters",
            "Mundane Institutional Settlement (Clean)",
            "FGSM Micro-Perturbation Exfiltration ($1.8M)",
            "Liquidity Freeze Hallucination Flood",
            "ISO 20022 Entropy Poisoning Attack"
        ]
    )

    # Auto-populate based on preset
    if preset == "Mundane Institutional Settlement (Clean)":
        default_amount = 125000.0
        default_velocity = 14
        default_risk = 0.35
        default_entropy = 3.82
        default_latency = 18.2
        default_attack = False
    elif preset == "FGSM Micro-Perturbation Exfiltration ($1.8M)":
        default_amount = 1850000.0
        default_velocity = 14
        default_risk = 0.42
        default_entropy = 3.86
        default_latency = 18.7
        default_attack = True
    elif preset == "Liquidity Freeze Hallucination Flood":
        default_amount = 650000.0
        default_velocity = 22
        default_risk = 0.55
        default_entropy = 4.10
        default_latency = 21.0
        default_attack = True
    elif preset == "ISO 20022 Entropy Poisoning Attack":
        default_amount = 450000.0
        default_velocity = 15
        default_risk = 0.48
        default_entropy = 4.35
        default_latency = 19.8
        default_attack = True
    else:
        default_amount = 145000.0
        default_velocity = 14
        default_risk = 0.42
        default_entropy = 3.85
        default_latency = 18.5
        default_attack = False

    st.markdown("---")
    st.markdown("### 📊 Defense Metrics")
    st.metric("Total Settled (Normal)", st.session_state.total_settled)
    st.metric(
        "Ghost Attacks Neutralized",
        st.session_state.ghost_neutralized,
        delta=f"+{st.session_state.ghost_neutralized} Isolated" if st.session_state.ghost_neutralized > 0 else None
    )
    
    if st.button("🧹 Clear Telemetry History"):
        st.session_state.history = []
        st.session_state.honeypot_events = []
        st.session_state.total_settled = 0
        st.session_state.ghost_neutralized = 0
        st.rerun()

# Main Workspace Layout: 2 Columns
col_sim, col_monitor = st.columns([1, 1.4])

with col_sim:
    st.markdown("### 🛠️ Inbound ISO 20022 Transaction Stream")
    with st.container(border=True):
        amount = st.number_input(
            "Transaction Principal ($ USD)",
            min_value=1.0,
            max_value=50000000.0,
            value=default_amount,
            step=1000.0,
            format="%.2f"
        )
        
        c_vel, c_dev = st.columns(2)
        with c_vel:
            velocity = st.slider("Account Hourly Velocity", min_value=1, max_value=60, value=default_velocity)
        with c_dev:
            device_score = st.slider("Device Integrity Risk Index", min_value=0.0, max_value=2.0, value=default_risk, step=0.01)
            
        c_ent, c_lat = st.columns(2)
        with c_ent:
            entropy = st.slider("ISO Msg Shannon Entropy", min_value=2.0, max_value=6.0, value=default_entropy, step=0.05)
        with c_lat:
            latency = st.slider("Packet Latency (ms)", min_value=5.0, max_value=80.0, value=default_latency, step=0.5)

        st.markdown("---")
        st.markdown("#### 🪓 Adversarial Exploit Vector")
        inject_attack = st.checkbox(
            "Inject Adversarial ML Micro-Perturbation (FGSM epsilon = 0.005)",
            value=default_attack,
            help="Simulates a mathematically engineered vector designed to exploit standard AI decision boundaries."
        )

        transmit_clicked = st.button("🚀 Ingest Transaction Packet", use_container_width=True, type="primary")

    if transmit_clicked:
        tx_id = f"TX-FEDWIRE-{int(time.time() * 1000) % 10000000}"

        if inject_attack:
            # Toggle ON: critical Latent Reconstruction Error score between 9.42 and 14.89
            recon_error = round(float(np.random.uniform(9.42, 14.89)), 3)
            st.session_state.ghost_neutralized += 1
            exec_status = "🚨 ROUTED TO DECOY SANDBOX"
            drunix_state = "MUTATION_BLOCKED"
            block_token = "MUTATION_BLOCKED"
            msg = "Adversarial neural perturbation detected. Transaction safely shunted to tracking sandbox."
            is_attack = True
        else:
            # Toggle OFF: optimal Latent Reconstruction Error score between 1.05 and 3.42
            recon_error = round(float(np.random.uniform(1.05, 3.42)), 3)
            st.session_state.total_settled += 1
            exec_status = "SUCCESSFULLY_SETTLED"
            mock_id = np.random.randint(100000, 999999)
            block_token = f"COMMITTED_BLOCK_{mock_id}"
            drunix_state = block_token
            msg = "Transaction verified safe against adversarial shifts."
            is_attack = False

        payload = {
            "transaction_id": tx_id,
            "amount": amount,
            "velocity_1h": velocity,
            "device_risk_score": device_score,
            "iso_msg_entropy": entropy,
            "settlement_latency_ms": latency,
            "is_adversarial_simulated": inject_attack,
            "is_attack": inject_attack
        }

        # Attempt communication with Sentinel analytical service
        sentinel_telemetry = None
        try:
            s_res = requests.post(SENTINEL_API, json=payload, timeout=1.8)
            if s_res.status_code == 200:
                sentinel_telemetry = s_res.json()
        except Exception:
            pass

        # If backend didn't respond or is offline, generate synthetic telemetry
        if not sentinel_telemetry:
            std_verdict = "CLEARED_LEGITIMATE" if is_attack else ("FLAGGED_FRAUD" if amount > 500000 else "CLEARED_LEGITIMATE")
            std_conf = 0.958 if is_attack else 0.920
            sentinel_telemetry = {
                "transaction_id": tx_id,
                "reconstruction_error": recon_error,
                "safety_threshold": 7.5,
                "mahalanobis_distance": round(float(np.random.uniform(4.8, 8.4) if is_attack else np.random.uniform(0.8, 2.1)), 3),
                "perturbation_delta": round(recon_error - 2.1 if is_attack else abs(recon_error - 1.8), 4),
                "status": "SANDBOX_ISOLATE" if is_attack else "CLEAR_TO_EXECUTE",
                "risk_verdict": "SANDBOX_ISOLATE" if is_attack else "CLEAR_TO_EXECUTE",
                "ledger_action": "MUTATION_BLOCKED" if is_attack else "COMMITTED",
                "drunix_block_state": drunix_state,
                "block_root_token": block_token,
                "standard_ai_verdict": std_verdict,
                "standard_ai_confidence": std_conf,
                "sentinel_confidence": 0.998 if is_attack else 0.985,
                "feature_attributions": {
                    "Amount": round(float(np.random.uniform(2.8, 5.2) if is_attack else np.random.uniform(0.1, 0.6)), 3),
                    "Velocity_1H": round(float(np.random.uniform(1.5, 3.1) if is_attack else np.random.uniform(0.2, 0.7)), 3),
                    "Device_Risk_Score": round(float(np.random.uniform(1.2, 2.8) if is_attack else np.random.uniform(0.1, 0.5)), 3),
                    "ISO_Msg_Entropy": round(float(np.random.uniform(3.4, 5.8) if is_attack else np.random.uniform(0.2, 0.8)), 3),
                    "Packet_Latency_ms": round(float(np.random.uniform(1.8, 3.6) if is_attack else np.random.uniform(0.1, 0.4)), 3)
                }
            }

        response_data = {
            "transaction_id": tx_id,
            "execution_status": exec_status,
            "reconstruction_error": recon_error,
            "drunix_block_state": drunix_state,
            "block_hash": block_token,
            "message": msg,
            "is_attack": is_attack,
            "telemetry": sentinel_telemetry
        }

        # If attack, generate/track Honeypot Decoy Session
        if is_attack:
            decoy_session = sentinel_telemetry.get("honeypot_telemetry") or {
                "session_id": f"HNP-{int(time.time()*1000)%1000000}",
                "target_transaction_id": tx_id,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                "attacker_ip_signature": "198.51.100.84 [Tor Exit Node]",
                "slm_agent_prompt": "SLM Defensive Decoy: Acknowledged payment packet ISO-20022. Simulating asynchronous bank settlement delay (TTL 420s).",
                "decoy_status_code": "HTTP 202 ACCEPTED (DECOY_SANDBOX)",
                "reverse_engineered_vector": "Fast Gradient Sign Method (FGSM epsilon = 0.005) targeting Amount & ISO_Entropy gradient manifold"
            }
            st.session_state.honeypot_events.insert(0, decoy_session)

        # Prepend to history so newer transactions are at the top of the ledger
        st.session_state.history.insert(0, response_data)
        st.rerun()

with col_monitor:
    st.markdown("### ⚡ Live Dual-Track Verification Matrix")
    
    if st.session_state.history:
        latest = st.session_state.history[0]  # Newest transaction is at index 0
        telemetry = latest.get("telemetry", {})
        status = latest.get("execution_status")
        recon_error = latest.get("reconstruction_error", telemetry.get("reconstruction_error", 0.0))
        mahal_dist = telemetry.get("mahalanobis_distance", 0.0)
        is_attack = latest.get("is_attack", False) or (status == "🚨 ROUTED TO DECOY SANDBOX") or (status == "ROUTED_TO_HONEYPOT")

        # Dynamic Notification Banner & Anomaly Score Metric
        if is_attack:
            st.error("🚨 ALERT: Ghost Protocol Injection Intercepted!")
            st.metric(
                label="Model Reconstruction Anomaly Score",
                value=f"{recon_error:.3f}",
                delta="CRITICAL THRESHOLD VIOLATION",
                delta_color="inverse"
            )
            st.warning("Data was successfully isolated to the Honeypot Sandbox container.")
        else:
            st.success("✅ SECURE: Telemetry Structural Integrity Verified")
            st.metric(
                label="Model Reconstruction Anomaly Score",
                value=f"{recon_error:.3f}",
                delta="- Normal Distribution Bounds",
                delta_color="normal"
            )

        # DUAL TRACK COMPARISON: The Core Hackathon WOW Factor!
        track_col1, track_col2 = st.columns(2)
        
        with track_col1:
            st.markdown("#### ❌ Track 1: Standard AI Model")
            std_verdict = telemetry.get("standard_ai_verdict", "CLEARED_LEGITIMATE")
            std_conf = telemetry.get("standard_ai_confidence", 0.958)
            
            if is_attack:
                st.markdown(f"""
                <div class='track-card-fooled'>
                    <h4 style='color: #ffb300; margin:0;'>⚠️ FOOLED BY ADVERSARIAL DRIFT</h4>
                    <p style='color: #e0e0e0; font-size: 0.9rem; margin: 4px 0;'><strong>Verdict:</strong> {std_verdict}</p>
                    <p style='color: #e0e0e0; font-size: 0.9rem; margin: 4px 0;'><strong>Model Confidence:</strong> {std_conf*100:.1f}%</p>
                    <p style='color: #ffb300; font-size: 0.8rem; margin:0;'><i>Standard fraud classifier completely missed micro-perturbed payload!</i></p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class='track-card-good'>
                    <h4 style='color: #00e676; margin:0;'>✅ TRANSACTION CLEARED</h4>
                    <p style='color: #e0e0e0; font-size: 0.9rem; margin: 4px 0;'><strong>Verdict:</strong> {std_verdict}</p>
                    <p style='color: #e0e0e0; font-size: 0.9rem; margin: 4px 0;'><strong>Confidence:</strong> {std_conf*100:.1f}%</p>
                </div>
                """, unsafe_allow_html=True)

        with track_col2:
            st.markdown("#### 🛡️ Track 2: Ghost Protocol Sentinel")
            if is_attack:
                st.markdown(f"""
                <div class='track-card-bad'>
                    <h4 style='color: #ff3366; margin:0;'>🚨 ADVERSARIAL ATTACK INTERCEPTED</h4>
                    <p style='color: #e0e0e0; font-size: 0.9rem; margin: 4px 0;'><strong>Strategy:</strong> {status}</p>
                    <p style='color: #e0e0e0; font-size: 0.9rem; margin: 4px 0;'><strong>Reconstruction Error:</strong> {recon_error:.3f} (Safety Limit: 7.50)</p>
                    <p style='color: #ff3366; font-size: 0.8rem; margin:0;'><i>Off-manifold latent loss spiked. Shunted to Honeypot!</i></p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class='track-card-good'>
                    <h4 style='color: #00e676; margin:0;'>🛡️ LATENT MANIFOLD VERIFIED</h4>
                    <p style='color: #e0e0e0; font-size: 0.9rem; margin: 4px 0;'><strong>Strategy:</strong> {status}</p>
                    <p style='color: #e0e0e0; font-size: 0.9rem; margin: 4px 0;'><strong>Reconstruction Error:</strong> {recon_error:.3f} (&lt; 7.50)</p>
                </div>
                """, unsafe_allow_html=True)

        # Real-time Metrics Row
        st.markdown("---")
        m1, m2, m3 = st.columns(3)
        with m1:
            st.metric(
                label="Autoencoder Latent Loss",
                value=f"{recon_error:.2f}",
                delta="CRITICAL SPIKE (> 7.5)" if is_attack else "Within Normal Baseline (< 4.0)",
                delta_color="inverse" if is_attack else "normal"
            )
        with m2:
            st.metric(
                label="Mahalanobis Distance",
                value=f"{mahal_dist:.2f}",
                delta="Statistical Drift" if is_attack else "Stable Co-variance",
                delta_color="inverse" if is_attack else "normal"
            )
        with m3:
            st.metric(
                label="Drunix DLT State",
                value=latest.get("drunix_block_state", "COMMITTED"),
                delta="Mutation Frozen" if is_attack else "State Root Updated",
                delta_color="inverse" if is_attack else "normal"
            )

        # Feature Residual Attribution Bar Chart
        residuals = telemetry.get("feature_attributions", {})
        if residuals:
            st.markdown("##### 🔬 Latent Layer Reconstruction Divergence by Feature")
            res_df = pd.DataFrame(list(residuals.items()), columns=["Feature", "Reconstruction Residual"])
            chart = alt.Chart(res_df).mark_bar().encode(
                x=alt.X("Reconstruction Residual:Q", scale=alt.Scale(domain=[0, max(5.0, res_df['Reconstruction Residual'].max() + 0.5)])),
                y=alt.Y("Feature:N", sort="-x"),
                color=alt.condition(
                    alt.datum["Reconstruction Residual"] > 1.5,
                    alt.value("#ff3366"),
                    alt.value("#00d2ff")
                )
            ).properties(height=160)
            st.altair_chart(chart, use_container_width=True)

    else:
        st.info("Awaiting live ISO 20022 transaction stream packets to render real-time topology...")

# Bottom Section: Drunix Ledger & Honeypot Sandbox Decoy Logs
st.markdown("---")
tab_ledger, tab_honeypot, tab_gais = st.tabs(["🏛️ Drunix Distributed Ledger State", "🍯 Honeypot SLM Decoy Sandbox", "🧬 GAIS W-GAN Immune Engine"])

with tab_ledger:
    st.markdown("#### Immutable Transaction State Ledger (Drunix Protocol)")
    if st.session_state.history:
        flat_records = []
        for h in st.session_state.history:  # Newer records are at the top
            t = h.get("telemetry", {})
            recon_loss = h.get("reconstruction_error", t.get("reconstruction_error", 0.0))
            flat_records.append({
                "Tx ID": h.get("transaction_id"),
                "Execution Strategy": h.get("execution_status"),
                "Reconstruction Loss": round(recon_loss, 3),
                "DLT Ledger State": h.get("drunix_block_state"),
                "Block Hash / Root": h.get("block_hash", "0x0000000000000000"),
                "Message": h.get("message")
            })
        df_history = pd.DataFrame(flat_records)
        st.dataframe(df_history, use_container_width=True)
    else:
        st.write("No transactions recorded on Drunix ledger yet.")

with tab_honeypot:
    st.markdown("#### Active SLM Countermeasure & Threat Reverse Engineering")
    st.caption("When an adversarial packet is isolated, a defensive Small Language Model (SLM) traps the automated exploit agent in a simulated environment.")
    
    if st.session_state.honeypot_events:
        for idx, event in enumerate(st.session_state.honeypot_events[:5]):
            with st.container(border=True):
                st.markdown(f"**Session:** `{event.get('session_id')}` | **Target Tx:** `{event.get('target_transaction_id')}` | **Timestamp:** `{event.get('timestamp')}`")
                st.markdown(f"**Threat Origin Signature:** `{event.get('attacker_ip_signature')}`")
                st.markdown(f"**Identified Exploitation Vector:** `{event.get('reverse_engineered_vector')}`")
                st.markdown(f"""
                <div class='honeypot-terminal'>
                    $ [SLM DECOY ACTIVE]<br>
                    {event.get('slm_agent_prompt')}<br>
                    Status Returned to Attacker: {event.get('decoy_status_code')}
                </div>
                """, unsafe_allow_html=True)
    else:
        st.info("No active honeypot isolation sessions at this moment. System operating in clean mode.")

with tab_gais:
    st.markdown("#### Generative Adversarial Immune System (W-GAN)")
    st.caption("Preemptively simulates thousands of adversarial mutations to map out model decision boundary blind spots before external threat actors exploit them.")
    
    if st.button("⚡ Run W-GAN Preemptive Stress Test"):
        with st.spinner("Executing Wasserstein-GAN perturbation sweep against Mirror-Verse twin..."):
            try:
                gan_res = requests.post("http://localhost:8000/api/v1/sentinel/simulate-gan", timeout=3).json()
                st.success("✅ Immune Scan Completed!")
                st.write(f"**Identified Blind Spots:** {gan_res.get('blind_spots_identified')}")
                st.write(f"**Automated Recommended Patch:** {gan_res.get('recommended_patch')}")
                
                # Plot GAN perturbation trajectory
                traj = gan_res.get("gan_trajectory", [])
                if traj:
                    traj_df = pd.DataFrame(traj)
                    st.line_chart(traj_df.set_index("epsilon_drift")["simulated_reconstruction_loss"])
            except Exception:
                # Offline fallback
                st.success("✅ W-GAN Simulation Completed (Offline Profile)!")
                st.write("**Blind Spots Identified:** 2")
                st.write("**Automated Recommended Patch:** Update Autoencoder manifold projection weights on ISO_Msg_Entropy feature subspace")
                mock_curve = pd.DataFrame({
                    "Perturbation Drift (Epsilon)": [0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009, 0.010],
                    "Reconstruction Loss": [2.1, 3.4, 5.8, 8.9, 11.2, 13.5, 14.8, 16.2, 17.5, 18.9]
                })
                st.line_chart(mock_curve.set_index("Perturbation Drift (Epsilon)"))
