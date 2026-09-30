"""Execute the public Jupyter walkthrough in memory as a reproducibility check."""
from pathlib import Path

import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[2]
NOTEBOOK = ROOT / "analysis" / "notebooks" / "reproducible_yield_walkthrough.ipynb"


def main() -> None:
    notebook = nbformat.read(NOTEBOOK, as_version=4)
    client = NotebookClient(
        notebook,
        timeout=120,
        kernel_name="python3",
        resources={"metadata": {"path": str(ROOT)}},
    )
    client.execute()
    print("Notebook execution check passed.")


if __name__ == "__main__":
    main()
