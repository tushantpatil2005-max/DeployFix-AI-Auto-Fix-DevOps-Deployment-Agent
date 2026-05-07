# DeployFix AI Architecture

DeployFix AI uses a modular AI-agent pipeline:

1. Log Analyzer Agent
2. Root Cause Classifier Agent
3. Fix Generation Agent
4. Patch Generation Agent

The system processes CI/CD logs and generates:
- root cause analysis
- fix recommendations
- patch-ready diffs
- structured JSON output