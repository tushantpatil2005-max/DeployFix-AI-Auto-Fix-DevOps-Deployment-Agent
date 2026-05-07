from agent.classifier import ErrorClassifier


def test_classifier():
    classifier = ErrorClassifier()

    result = classifier.classify("npm ERR! dependency issue")

    assert result == "Node Build Failure"