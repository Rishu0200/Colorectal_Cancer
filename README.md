# Colorectal Cancer Prediction

A small end-to-end machine learning project that trains, evaluates, and serves a model to predict colorectal cancer from tabular clinical data. The repository includes preprocessing, model training, MLflow experiment tracking, a simple web UI, Docker packaging, and a Kubeflow pipeline for orchestration.

## Features
- Data preprocessing and feature engineering
- Model training, evaluation, and artifact saving
- MLflow experiment tracking (`mlruns/`)
- Simple Flask (or similar) web UI for inference (`application.py`, `templates/`, `static/`)
- Dockerfile for containerization
- Kubeflow pipeline definition for MLOps (`kubeflow_pipeline/`)

## Repository Layout

- `artifacts/` — raw, processed data and trained model artifacts
	- `artifacts/raw/data.csv` — source dataset
	- `artifacts/processed/` — processed dataset artifacts
	- `artifacts/models/` — saved model(s)
- `src/` — source modules
	- `src/data_processing.py` — data cleaning and preprocessing
	- `src/model_training.py` — training, evaluation and model saving
	- `src/logger.py` — logging utilities
	- `src/custom_exception.py` — custom exceptions
- `kubeflow_pipeline/` — Kubeflow pipeline script and helpers
	- `kubeflow_pipeline/mlops_pipeline.py`
- `application.py` — app entrypoint for serving the model
- `colorectal_cancer_pipeline.yaml` — pipeline manifest
- `requirements.txt`, `Dockerfile`, `setup.py` — packaging and dependencies
- `templates/`, `static/` — simple front-end for demo
- `mlruns/`, `logs/` — MLflow runs and log output

## Quick Start

1. Create a Python environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate   # use PowerShell/CMD equivalent on Windows
pip install -r requirements.txt
```

2. Preprocess the raw data (creates processed artifacts):

```bash
python -m src.data_processing
```

3. Train the model (saves model to `artifacts/models/` and logs runs to `mlruns/`):

```bash
python -m src.model_training
```

4. Run the demo app for inference:

```bash
python application.py
```

Visit `http://localhost:8080` (or port configured in `application.py`) to use the UI.

## Docker

Build and run the container locally:

```bash
docker build -t colorectal-cancer-app .
docker run -p 8080:8080 colorectal-cancer-app
```

## Kubeflow / MLOps

The repository includes a Kubeflow pipeline definition in `kubeflow_pipeline/` and `colorectal_cancer_pipeline.yaml`. Use your Kubeflow deployment to upload the pipeline and run experiments there. The pipeline code can be adapted to remote storage for artifacts and MLflow tracking.

## Notes & Next Steps

- Confirm the schema of `artifacts/raw/data.csv` before preprocessing.
- Add unit tests and CI to validate data-processing and training steps.
- Add hyperparameter tuning (Optuna / scikit-learn GridSearchCV) in `src/model_training.py`.
- Secure and externalize configuration (credentials, storage paths) for production runs.

## Contributing

Fork the repo, create a branch, and submit a PR. Please update `requirements.txt` when adding new packages and include tests for new functionality.

## License

Add a LICENSE file to specify terms for open-source release. If internal, document usage and sharing policies here.

---

If you want, I can (a) open any file and provide a concise summary, (b) run the preprocessing and training locally, or (c) commit and push these changes for you — tell me which next.

## Contact

Email- Rishabhanand0200@gmail.com



