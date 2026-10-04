from aeris.config import load_config


def test_config_loads():
    cfg = load_config("config/config.yaml")
    assert cfg.camera["width"] == 640
    assert cfg.rendering["projector_resolution"] == [1280, 720]
