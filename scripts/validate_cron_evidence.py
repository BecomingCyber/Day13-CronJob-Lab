from pathlib import Path
import sys


REQUIRED_FILES = {
    "cron analysis": Path("analysis/cron_findings.txt"),
    "cleanup documentation": Path("cleanup/cleanup_commands.txt"),
    "cron log evidence": Path("logs/cron.log"),
    "screenshot evidence": Path("images"),
}


def validate_files():
    """Validate required investigation evidence exists."""

    valid = True

    for name, path in REQUIRED_FILES.items():

        if not path.exists():
            print(f"[FAIL] Missing {name}: {path}")
            valid = False

        else:
            print(f"[PASS] {name} exists.")

    return valid


def validate_analysis_content():
    """Validate investigation notes contain required findings."""

    findings = Path("analysis/cron_findings.txt")

    if not findings.exists():
        return False

    content = findings.read_text(
        encoding="utf-8"
    ).lower()

    required_terms = [
        "cron",
        "detection",
        "cleanup",
        "verification",
    ]

    valid = True

    for term in required_terms:

        if term not in content:
            print(
                f"[FAIL] Missing investigation keyword: {term}"
            )
            valid = False

        else:
            print(
                f"[PASS] Investigation contains: {term}"
            )

    return valid


def main():

    print("Cron Job Evidence Validation")
    print("============================")

    checks = [
        validate_files(),
        validate_analysis_content(),
    ]

    if all(checks):

        print(
            "\n[PASS] Evidence validation completed successfully."
        )

        return 0

    print(
        "\n[FAIL] Evidence validation failed."
    )

    return 1


if __name__ == "__main__":
    sys.exit(main())
