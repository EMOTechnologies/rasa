import sys
from importlib.metadata import distributions


def test_tensorflow_text_install():
    installed_packages_list = [d.metadata["Name"].lower().replace("_", "-") for d in distributions()]
    tf_text_installed = "tensorflow-text" in installed_packages_list

    if sys.platform == "win32":
        assert not tf_text_installed
    else:
        assert tf_text_installed
