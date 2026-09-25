from fastapi import FastAPI
from app.config import settings
from app.models import PaperQuery, PaperAnalysisResponse
from app.services.paper_engine import analyze_paper

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

@app.post("/analyze", response_model=PaperAnalysisResponse)
def analyze(req: PaperQuery):
    p = analyze_paper(req.arxiv_id, req.question)
    return PaperAnalysisResponse(
        title=p["title"],
        authors=p["authors"],
        methodology_summary=p["methodology"],
        key_findings=p["findings"],
        bibtex=p["bibtex"]
    )
