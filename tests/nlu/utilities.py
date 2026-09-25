import tempfile
import rasa.shared.utils.io


def write_file_config(file_config):
    with tempfile.NamedTemporaryFile(
        "w+", suffix="_tmp_config_file.yml", delete=False
    ) as f:
        f.write(rasa.shared.utils.io.dump_obj_as_yaml_to_string(file_config))
        f.flush()
        return f


class ResponseTest:
    def __init__(self, endpoint, expected_response, payload=None):
        self.endpoint = endpoint
        self.expected_response = expected_response
        self.payload = payload
