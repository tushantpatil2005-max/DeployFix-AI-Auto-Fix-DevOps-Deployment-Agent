from fastapi import FastAPI
import uvicorn

from agent.analyzer import LogAnalyzer
from agent.classifier import ErrorClassifier
from agent.fixer import FixGenerator
from agent.patch_generator import PatchGenerator
from agent.utils import save_json, pretty_print

from api.routes import router

app = FastAPI(title="DeployFix AI")

app.include_router(router)


def run_cli():
    print("\nDeployFix AI Starting...\n")

    with open("examples/docker_build_failure.log", "r") as file:
        log_content = file.read()

    analyzer = LogAnalyzer(log_content)
    errors = analyzer.extract_errors()

    classifier = ErrorClassifier()
    fixer = FixGenerator()
    patcher = PatchGenerator()

    final_results = []

    for error in errors:
        category = classifier.classify(error)
        fix = fixer.generate_fix(error, category)
        patch = patcher.generate_patch(category)

        result = {
            "issue": error,
            "category": category,
            "fix": fix,
            "patch": patch,
        }

        final_results.append(result)

    save_json(final_results)

    pretty_print(final_results)


if __name__ == "__main__":
    run_cli()

    uvicorn.run(app, host="0.0.0.0", port=8000)