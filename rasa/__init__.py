import logging
import os

# Rasa's TensorFlow-based components (DIETClassifier, TEDPolicy, etc.) are built
# against the Keras 2 API. TensorFlow 2.16+ defaults to Keras 3, so we opt back
# into the legacy Keras 2 implementation (provided by the `tf-keras` package).
# This must be set before TensorFlow is imported anywhere in the process.
os.environ.setdefault("TF_USE_LEGACY_KERAS", "1")

from rasa import version, plugin  # noqa: F401
from rasa.api import run, train, test  # noqa: F401

# define the version before the other imports since these need it
__version__ = version.__version__


logging.getLogger(__name__).addHandler(logging.NullHandler())
