from pydantic import BaseModel
from typing import List, Optional

class PaperQuery(BaseModel):
    arxiv_id: Optional[str] = "2305.18290"
    question: str

class PaperAnalysisResponse(BaseModel):
    title: str
    authors: List[str]
    methodology_summary: str
    key_findings: str
    bibtex: str
