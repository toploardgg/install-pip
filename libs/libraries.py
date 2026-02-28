# ──────────────────────────────────────────────
#  STDLIB PACKAGES — pip cannot install these
#  They ship with Python itself
# ──────────────────────────────────────────────
STDLIB_ONLY = {
    "asyncio", "configparser", "concurrent-futures",
    "tkinter", "sqlite3", "uuid", "pathlib",
}

# ──────────────────────────────────────────────
#  ~200 LIBRARIES LIST
# ──────────────────────────────────────────────
BASIC_LIBS = [
    # Web & HTTP
    "requests", "httpx", "aiohttp", "urllib3", "certifi", "charset-normalizer",
    "websockets", "httpcore", "h2", "h11",

    # Data Science & Math
    "numpy", "pandas", "scipy", "matplotlib", "seaborn", "plotly",
    "statsmodels", "sympy", "scikit-learn", "xgboost", "lightgbm",
    "catboost", "shap", "optuna", "mlflow",

    # Deep Learning
    "torch", "torchvision", "torchaudio", "tensorflow", "keras",
    "transformers", "diffusers", "accelerate", "datasets", "tokenizers",
    "onnx", "onnxruntime", "timm", "lightning",

    # NLP
    "nltk", "spacy", "gensim", "textblob", "langchain", "langchain-community",
    "openai", "anthropic", "tiktoken", "sentence-transformers",

    # Database
    "sqlalchemy", "psycopg2-binary", "pymysql", "pymongo", "redis",
    "motor", "aiomysql", "aiosqlite", "databases", "tortoise-orm",
    "alembic", "peewee", "tinydb", "elasticsearch",

    # Async & Concurrency
    "aiofiles", "trio", "anyio", "uvloop",

    # Web Frameworks
    "flask", "django", "fastapi", "uvicorn", "gunicorn", "starlette",
    "tornado", "sanic", "quart", "falcon", "bottle", "cherrypy",

    # Scraping & Parsing
    "beautifulsoup4", "lxml", "scrapy", "selenium", "playwright",
    "mechanize", "httplib2", "pyquery", "parsel", "fake-useragent",

    # Bots & Messaging
    "aiogram", "python-telegram-bot", "discord.py", "slack-sdk",
    "twilio", "vk-api", "telebot",

    # CLI & Terminal
    "click", "typer", "rich", "colorama", "termcolor", "tqdm",
    "alive-progress", "prompt-toolkit", "pyfiglet", "art",
    "tabulate", "prettytable", "blessed",

    # Config & Env
    "python-dotenv", "pydantic", "pydantic-settings", "dynaconf",
    "toml", "python-decouple",

    # Serialization
    "marshmallow", "orjson", "ujson", "msgpack", "protobuf",
    "avro-python3", "pyarrow", "fastavro",

    # Testing
    "pytest", "pytest-asyncio", "pytest-cov", "pytest-mock",
    "hypothesis", "faker", "factory-boy", "responses", "freezegun",
    "coverage", "mock", "unittest2",

    # Logging & Monitoring
    "loguru", "structlog", "sentry-sdk", "prometheus-client",
    "opentelemetry-sdk", "datadog",

    # Security & Auth
    "cryptography", "pycryptodome", "passlib", "bcrypt", "pyotp",
    "python-jose", "authlib", "pyjwt", "itsdangerous",

    # Files & IO
    "pillow", "pypdf2", "python-docx", "openpyxl", "xlrd",
    "xlwt", "python-pptx", "reportlab", "fpdf2", "img2pdf",
    "pyexcel", "chardet",

    # Scheduling & Tasks
    "celery", "apscheduler", "schedule", "rq", "dramatiq",
    "huey", "prefect",

    # Cloud & DevOps
    "boto3", "google-cloud-storage", "azure-storage-blob",
    "paramiko", "fabric", "docker",

    # Networking & Protocols
    "scapy", "pyzmq", "pika", "kafka-python", "nats-py",
    "grpcio", "pyserial", "netifaces",

    # Utils & Helpers
    "arrow", "pendulum", "python-dateutil", "pytz", "humanize",
    "more-itertools", "toolz", "cytoolz", "funcy", "boltons",
    "cachetools", "diskcache", "joblib", "dill", "cloudpickle",
    "attrs", "cattrs", "dacite", "dataclasses-json",

    # System & OS
    "psutil", "py-cpuinfo", "gputil", "watchdog",
    "pyautogui", "pynput", "keyboard", "mouse",

    # GUI
    "tkinter", "pyqt5", "wxpython", "kivy", "tkinter-tooltip",
    "customtkinter", "ttkthemes", "ttkbootstrap",

    # Image & Video
    "opencv-python", "imageio", "scikit-image", "wand",
    "pytesseract", "easyocr", "ffmpeg-python",

    # Audio
    "librosa", "soundfile", "pyaudio", "playsound", "pydub",
    "speechrecognition", "pyttsx3",

    # Geo & Maps
    "geopy", "shapely", "geopandas", "folium", "pyproj",

    # Graph & Network Analysis
    "networkx", "python-igraph", "python-louvain", "node2vec",

    # Code Tools
    "black", "isort", "flake8", "pylint", "mypy", "bandit",
    "autopep8", "pyupgrade", "pre-commit",

    # Misc
    "qrcode", "pybarcode", "pyperclip", "pyflakes", "regex",
    "fuzzywuzzy", "rapidfuzz", "python-Levenshtein", "unidecode",
    "translators", "deep-translator",
]
