# Diabetes Prediction

Learning notebook and Flask application for the diabetes classification pipeline.

## Run

```powershell
python -m pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5001`. The JSON endpoint is `POST /predict`.

See [PROCESSING_AND_MODEL_RATIONALE.md](PROCESSING_AND_MODEL_RATIONALE.md) for the data-cleaning and algorithm choices.

See [diabetes_knowledge_graph.md](diabetes_knowledge_graph.md) for the Long Chau-based diabetes knowledge graph and its machine-readable [JSON](diabetes_knowledge_graph.json).
