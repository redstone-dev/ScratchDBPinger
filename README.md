# ScratchDBPinger

A simple server to connect to a Scratch project that tells it (using cloud variables) if ScratchDB is up or down.

## Downloading
> Make sure you have Python 3.10 or above installed.

Just clone the repo into your favourite directory and run `pip install -r requirements.txt`.
> Try `python -m pip install -r requirements.txt` if that doesn't work.
> If that last one doesn't work, try `py` instead of `python`.

Then, make a `.env` file in the same directory as `main.py` and add this to `.env`:

```.env
USER="<insert scratch username>"
PASS="<insert scratch password>"
```

Finally, run `py main.py` or `python main.py`.
