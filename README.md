

A containerized, production-ready REST API for banking operations built with **FastAPI**, fully tested with Python's unit testing framework, and structured for cloud native orchestration via **Docker** and **Kubernetes**.


* `app.py` - Core banking logic endpoints (Balance Check, Deposits, Validated Withdrawals).
* `test_app.py` - Automated software quality verification test suite.
* `requirements.txt` - Python runtime application dependencies.
* `Dockerfile` - Containerized lightweight compilation layer.
* `deployment.yaml` - Kubernetes standard deployment and internal service orchestration.


Ensure you have Python installed, then execute the following steps in your terminal:

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Launch the Server:**
   ```bash
   uvicorn app:app --reload
   ```
3. **Access Interactive API Documentation:** Open `http://127.0.0` in your browser.

To verify all transaction edge-cases, validation limits, and overdraft rules operate successfully, run:
```bash
python -m unittest test_app.py
```


* **Build Docker Image:** `docker build -t banking-app:latest .`
* **Run Docker Container:** `docker run -p 8000:8000 banking-app:latest`
* **Apply Kubernetes Orchestration:** `kubectl apply -f deployment.yaml`
