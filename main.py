import os
import threading
from flask import Flask, render_template

# ─── Configuration ──────────────────────────────────────────────────────────
# Source quiz URL — shown openly to users (not hidden/cloaked).
QUIZ_URL = "https://studyspark.study/batches/6a38f418034b8baed508e6e4/tests/6a64654ddaa4c5ff3482bb00"

# ─── Flask app ──────────────────────────────────────────────────────────────
flask_app = Flask(__name__)


@flask_app.route('/')
def index():
    return render_template('index.html', quiz_url=QUIZ_URL)


def run_flask():
    port = int(os.environ.get("PORT", 8000))
    flask_app.run(host="0.0.0.0", port=port)


if __name__ == "__main__":
    # Started directly (no separate bot process here), so just run Flask
    # in the main thread. If you later add a bot/worker loop, start Flask
    # in a background thread instead (see run_flask above) and keep this
    # thread for the worker.
    run_flask()
