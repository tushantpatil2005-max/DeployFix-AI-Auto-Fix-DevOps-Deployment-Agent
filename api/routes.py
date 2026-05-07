from fastapi import APIRouter
from pydantic import BaseModel

from agent.analyzer import LogAnalyzer
from agent.classifier import ErrorClassifier
from agent.fixer import FixGenerator
from agent.patch_generator import PatchGenerator

router = APIRouter()


class LogRequest(BaseModel):
    log: str


@router.post("/analyze")
def analyze_log(request: LogRequest):
    analyzer = LogAnalyzer(request.log)

    errors = analyzer.extract_errors()

    classifier = ErrorClassifier()
    fixer = FixGenerator()
    patcher = PatchGenerator()

    results = []

    for error in errors:
        category = classifier.classify(error)
        fix = fixer.generate_fix(error, category)
        patch = patcher.generate_patch(category)

        results.append(
            {
                "error": error,
                "category": category,
                "fix": fix,
                "patch": patch,
            }
        )

    return {
        "status": "success",
        "results": results,
    }