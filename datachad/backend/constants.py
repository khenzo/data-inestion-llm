from pathlib import Path

MODEL_PATH = Path("models")
DATA_PATH = Path("data")
DEFAULT_VECTOR_STORE = "hub://khenzo/data-quantum-supremacy-pdf_512-15_text-embedding-ada-002_admin"

DEFAULT_USER = "admin"

CHUNK_SIZE = 512
CHUNK_OVERLAP_PCT = 15
TEMPERATURE = 0.0
MAX_TOKENS = 2560
MAXIMAL_MARGINAL_RELEVANCE = True
DISTANCE_METRIC = "cos"
K_FETCH_K_RATIO = 3

ENABLE_ADVANCED_OPTIONS = True
STORE_DOCS_EXTRA = False
LOCAL_DEEPLAKE = False
