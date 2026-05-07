import re


class LogAnalyzer:
    def __init__(self, log_content: str):
        self.log_content = log_content

    def extract_errors(self):
        error_patterns = [
            r"ERROR:.*",
            r"Error:.*",
            r"ModuleNotFoundError:.*",
            r"npm ERR!.*",
            r"failed.*",
            r"exception.*",
            r"Traceback.*",
        ]

        errors = []

        for pattern in error_patterns:
            matches = re.findall(pattern, self.log_content, re.IGNORECASE)
            errors.extend(matches)

        return list(set(errors))

    def summarize(self):
        errors = self.extract_errors()

        return {
            "total_errors": len(errors),
            "errors": errors,
        }