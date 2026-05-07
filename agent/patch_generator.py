class PatchGenerator:
    def generate_patch(self, category: str):
        if category == "Node Build Failure":
            return """
- RUN npm install
+ RUN npm install --legacy-peer-deps
"""

        if category == "Missing Environment Variable":
            return """
+ env:
+   OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
"""

        if category == "Docker Build Failure":
            return """
- FROM python:3.8
+ FROM python:3.11
"""

        return "No patch available"