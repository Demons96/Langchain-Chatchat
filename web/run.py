import subprocess
from multiprocessing import Process, Queue
import os


def run_webui():
    p = subprocess.Popen(["streamlit", "run", "web_test.py"])
    p.wait()


if __name__ == "__main__":
    process = Process(
        target=run_webui,
        name=f"WEBUI Server{os.getpid()})",
        daemon=True,
    )
    process.start()
