#  Project Ghost Protocol: Mirror-Verse Sentinel

**Securing Institutional AI Infrastructure Against Adversarial Machine Learning & Hallucination Viruses**  
*Citi Drunix Hackathon Flagship Submission*

---

##  Executive Summary & Problem Statement

As global tier-1 financial institutions like Citi migrate toward automated, high-throughput AI systems for risk assessment, liquidity management, and fraud detection, they introduce an insidious attack surface: **Adversarial Machine Learning (AML)**.

Sophisticated nation-state and cybercrime threat actors deploy **"Ghost Protocol"** attacks:
- **Structural Poisoning in High-Speed Feeds:** Adversaries inject micro-manipulated transaction payloads into real-time ISO 20022 feeds (Fedwire, CHIPS, SEPA).
- **Sub-perceptual Mathematical Tweaks:** Transactions appear mundane to human auditors and rule engines ($125,000 corporate transfers with minor $+0.003\%$ drift), but are mathematically engineered (via FGSM or PGD) to exploit the decision boundaries of core AI fraud models.
- **The Impact:** Inducing model hallucinations to either trigger systemic false-positive storms (freezing bank liquidity) or carving automated blind spots to mask multimillion-dollar capital exfiltrations in real time.

---

##  The Architecture: The Mirror-Verse Sentinel

Instead of patching static rules, Project Ghost Protocol builds a **Generative Immune System** that creates a parallel digital twin to isolate, analyze, and neutralize adversarial data manipulation before transactions reach the immutable ledger.

```
                  [ Global Inbound Transaction Stream ]
                                      │
                                      ▼
                        ┌───────────────────────────┐
                        │    Citibank API Gateway   │
                        └─────────────┬─────────────┘
                                      │
                   ┌──────────────────┴──────────────────┐
                   ▼ (Async Validation Mesh)             ▼ (Synchronous Path)
     ┌───────────────────────────┐         ┌───────────────────────────┐
     │   MIRROR-VERSE SENTINEL   │         │    CORE BANKING PLATFORM  │
     │      (Python Mesh)        │         │    (Java Spring Boot)     │
     ├───────────────────────────┤         ├───────────────────────────┤
     │ • FastAPI Gateway         │         │ • Transaction Controller  │
     │ • Autoencoder Engine      │         │ • Drunix Smart Contract   │
     │ • Mahalanobis Evaluator   │         │ • Honeypot Shifter        │
     │ • GAIS W-GAN Immune Sim   │         │ • State Mutation Blocker  │
     └─────────────┬─────────────┘         └─────────────┬─────────────┘
                   │                                     │
                   │ (Risk Context Callback)             │
                   └──────────────────┬──────────────────┘
                                      │
                                      ▼
                        ┌───────────────────────────┐
                        │ Security Operations Panel │
                        │  (Streamlit Control Hub)  │
                        └───────────────────────────┘
```

### Key Technical Pillars:
1. **The Mirror-Verse Twin:** A real-time, sandboxed digital twin of Citi's transaction scoring pipeline evaluating parallel data streams with $< 15\text{ ms}$ overhead.
2. **The Autoencoder & Perturbation Delta Engine:** Trained strictly on legitimate institutional settlement manifolds. When an adversarial Ghost payload arrives, high-dimensional latent reconstruction loss spikes ($> 8.5$), exposing the exploit.
3. **Generative Adversarial Immune System (GAIS):** Wasserstein GANs (W-GANs) proactively generate millions of synthetic attack perturbations against the model twin, discovering decision boundary blind spots before attackers do.
4. **The Honeypot SLM Decoy Sandbox:** Intercepted transactions are shunted to an isolated synthetic banking sandbox. A defensive Small Language Model (SLM) stalls the automated attacker and reverse-engineers their exploitation vector.
5. **Drunix DLT State Mutation Blocker:** Safe transactions are committed to the immutable Drunix Distributed Ledger (`COMMITTED_BLOCK_#`), while flagged attacks are frozen (`MUTATION_BLOCKED`).

---

##  Project Structure

```
Ghost-Protocol/
├── app.py                      # Mirror-Verse Sentinel (FastAPI, Autoencoder, Mahalanobis, GAIS)
├── dashboard.py                # Live Security Operations Center (Streamlit UI)
├── exploit_suite.py            # FGSM Adversarial Exploit Benchmark Generator
├── core-banking/               # Corporate Banking Hub (Java Spring Boot 3 & Drunix Bridge)
│   ├── pom.xml                 # Maven Build Specification
│   └── src/main/java/com/citi/drunix/ghostprotocol/
│       ├── GhostProtocolApplication.java
│       └── controller/TransactionController.java
├── tools/                      # Embedded Apache Maven 3.9.6 portable runtime
│   └── apache-maven-3.9.6/
├── run_sentinel.bat            # Quick Launcher: Python Sentinel (:8000)
├── run_banking.bat             # Quick Launcher: Java Spring Boot (:8080)
├── run_dashboard.bat           # Quick Launcher: Streamlit Operations Console (:8501)
├── run_exploit_benchmark.bat   # Quick Launcher: Exploit Benchmark Suite
└── start_all.bat               # Unified Single-Click Launcher
```

---

##  Quickstart Deployment

### 1. Initialize the Analytical Sentinel Node (Python)
In a terminal, run:
```bash
python app.py
```
*Service starts on `http://localhost:8000`.*

### 2. Boot the Corporate Banking Hub (Java Spring Boot)
In a second terminal, execute:
```bash
run_banking.bat
```
*Or using the included portable Maven:*
```bash
tools\apache-maven-3.9.6\bin\mvn.cmd -f core-banking\pom.xml spring-boot:run
```
*Service starts on `http://localhost:8080`.*

### 3. Launch the Security Operations Center (Streamlit)
In a third terminal, run:
```bash
streamlit run dashboard.py
```
*Dashboard opens automatically at `http://localhost:8501`.*

> **Single-Click Shortcut:** You can run `start_all.bat` to launch all three services simultaneously.

---

##  Running the Exploit Benchmark Suite

To mathematically demonstrate how the standard AI model is duped versus how Sentinel catches the attack:
```bash
python exploit_suite.py
```
**Results Demonstrated:**
- **Standard Fraud AI False Negative Rate:** $100\%$ (Adversarial payloads marked as legitimate!).
- **Mirror-Verse Sentinel Detection Rate:** $100\%$ (Latent reconstruction error spikes from $2.12$ to $14.85$, crossing the $8.50$ threshold).
- **Drunix Ledger State:** Attack mutation completely blocked.

---

##  Presentation Highlights for Hackathon Judges

1. **Dual-Track Comparison:**
   - In the Streamlit UI, toggle **"Inject Adversarial ML Micro-Perturbation (FGSM)"**.
   - Show Track 1 (Standard AI) displaying a naive green checkmark with high confidence ($95\%+$).
   - Show Track 2 (Ghost Protocol Sentinel) detecting the off-manifold perturbation, sounding the alarm, and shunting the request.
2. **Honeypot Reverse Engineering:**
   - Click the **"Honeypot SLM Decoy Sandbox"** tab to view the live synthetic settlement deception terminal stalling the adversary.
3. **Immutable DLT Security:**
   - Demonstrate the **"Drunix Distributed Ledger"** tab verifying that poisoned transactions never corrupt the core ledger state.
4. **Preemptive W-GAN Immune Defense:**
   - Click **"Run W-GAN Preemptive Stress Test"** in the GAIS tab to showcase proactive model vulnerability mapping.
