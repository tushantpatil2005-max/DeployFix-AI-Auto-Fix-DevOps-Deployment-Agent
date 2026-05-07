from agent.analyzer import LogAnalyzer


def test_extract_errors():
    log = "ERROR: deployment failed"

    analyzer = LogAnalyzer(log)

    errors = analyzer.extract_errors()

    assert len(errors) > 0