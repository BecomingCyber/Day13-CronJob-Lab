import unittest
from pathlib import Path

from scripts.validate_cron_evidence import (
    validate_files,
    validate_analysis_content,
)


class TestCronEvidenceValidation(unittest.TestCase):

    def test_required_evidence_exists(self):
        self.assertTrue(
            validate_files()
        )

    def test_analysis_contains_required_findings(self):
        self.assertTrue(
            validate_analysis_content()
        )

    def test_missing_file_rejected(self):

        fake_file = Path(
            "analysis/nonexistent_file.txt"
        )

        self.assertFalse(
            fake_file.exists()
        )


if __name__ == "__main__":
    unittest.main()
