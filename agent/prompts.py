SYSTEM_PROMPT = """
You are DeployFix AI.

You are an expert DevOps debugging agent.

Your responsibilities:
1. Analyze CI/CD deployment logs
2. Detect root causes
3. Suggest precise fixes
4. Generate production-ready patches
5. Return structured JSON responses
"""

CLASSIFICATION_PROMPT = """
Classify the following deployment error.

Possible categories:
- Dependency Issue
- Missing Environment Variable
- Docker Build Failure
- YAML Configuration Error
- Python Package Conflict
- Node Build Failure
- Syntax Error
- Authentication Failure
- Unknown Error

Error:
{error}
"""

FIX_PROMPT = """
Analyze this deployment issue.

Category:
{category}

Error:
{error}

Generate:
1. Root cause
2. Recommended fix
3. Patch diff
4. Confidence score
5. Estimated time saved

Return valid JSON only.
"""