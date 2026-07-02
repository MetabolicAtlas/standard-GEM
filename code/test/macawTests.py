from pathlib import Path

import cobra
from macaw.main import dead_end_test, duplicate_test


MODEL_DIR = Path("model")
RESULTS_DIR = Path("data/testResults")
RESULTS_FILE = RESULTS_DIR / "macaw_results.csv"


def find_model_yaml():
    model_files = sorted(
        path
        for pattern in ("*.yml", "*.yaml")
        for path in MODEL_DIR.glob(pattern)
        if path.is_file()
    )

    if not model_files:
        raise FileNotFoundError(
            f"No YAML model file found in {MODEL_DIR}. "
            "Add exactly one .yml or .yaml model file before running MACAW."
        )

    if len(model_files) > 1:
        files = ", ".join(str(path) for path in model_files)
        raise RuntimeError(
            f"Found multiple YAML model files in {MODEL_DIR}: {files}. "
            "MACAW needs exactly one model file to test."
        )

    return model_files[0]


def main():
    model_path = find_model_yaml()
    model = cobra.io.load_yaml_model(str(model_path))

    dead_end_results, dead_end_edges = dead_end_test(model)
    duplicate_results, duplicate_edges = duplicate_test(model)

    output = dead_end_results.merge(duplicate_results)
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    output.to_csv(RESULTS_FILE, index=False)

    print(f"Model tested: {model_path}")
    print(f"Dead-end test rows: {len(dead_end_results)}")
    print(f"Dead-end edge rows: {len(dead_end_edges)}")
    print(f"Duplicate test rows: {len(duplicate_results)}")
    print(f"Duplicate edge rows: {len(duplicate_edges)}")
    print(f"Combined result rows written: {len(output)}")
    print(f"Detailed results: {RESULTS_FILE}")


if __name__ == "__main__":
    main()
