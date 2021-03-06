"""Unit Tests - test cli."""
import subprocess


def test_cli_help():
    out = subprocess.check_output(['python', 'libsast'])
    assert out


def test_cli_pattern_match():
    try:
        subprocess.check_output([
            'python',
            'libsast',
            '-p',
            'tests/unit/assets/rules/patterns.yaml',
            'tests/unit/assets/files/'],
            stderr=subprocess.STDOUT,
        )
    except subprocess.CalledProcessError as exc:
        assert exc.returncode == 1
        assert b'test_regex' in exc.output
