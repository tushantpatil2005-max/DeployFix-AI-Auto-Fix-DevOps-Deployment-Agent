class ErrorClassifier:
    def classify(self, error: str):
        error_lower = error.lower()

        if "npm" in error_lower:
            return "Node Build Failure"

        if "module" in error_lower:
            return "Dependency Issue"

        if "env" in error_lower:
            return "Missing Environment Variable"

        if "docker" in error_lower:
            return "Docker Build Failure"

        if "yaml" in error_lower:
            return "YAML Configuration Error"

        if "traceback" in error_lower:
            return "Python Package Conflict"

        return "Unknown Error"