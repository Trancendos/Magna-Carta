import os
import json
from pathlib import Path
from unittest.mock import patch, mock_open, MagicMock

import pytest

import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
from compliance_health_check import resolve_signal_states, ROOT


def test_resolve_signal_states_empty():
    assert resolve_signal_states({}) == {}
    assert resolve_signal_states({"signals": []}) == {}


@patch.dict(os.environ, {"MY_ENV_VAR": "True"})
def test_resolve_signal_states_env_active():
    signals_data = {
        "signals": [
            {
                "signal_id": "SIG-01",
                "detection": [
                    {
                        "source": "env",
                        "variable": "MY_ENV_VAR",
                        "active_values": ["true", "1", "yes"]
                    }
                ]
            }
        ]
    }
    expected = {"SIG-01": "active"}
    assert resolve_signal_states(signals_data) == expected


@patch.dict(os.environ, {"MY_ENV_VAR": "False"})
def test_resolve_signal_states_env_inactive():
    signals_data = {
        "signals": [
            {
                "signal_id": "SIG-01",
                "detection": [
                    {
                        "source": "env",
                        "variable": "MY_ENV_VAR",
                        "active_values": ["true", "1", "yes"]
                    }
                ]
            }
        ]
    }
    expected = {"SIG-01": "inactive"}
    assert resolve_signal_states(signals_data) == expected


@patch.dict(os.environ, clear=True)
def test_resolve_signal_states_env_missing():
    signals_data = {
        "signals": [
            {
                "signal_id": "SIG-01",
                "detection": [
                    {
                        "source": "env",
                        "variable": "MY_ENV_VAR",
                        "active_values": ["true", "1", "yes"]
                    }
                ]
            }
        ]
    }
    expected = {"SIG-01": "inactive"}
    assert resolve_signal_states(signals_data) == expected


def test_resolve_signal_states_config_active():
    signals_data = {
        "signals": [
            {
                "signal_id": "SIG-02",
                "detection": [
                    {
                        "source": "config",
                        "path": "test_config.json",
                        "json_path": "enabled",
                        "active_values": ["true", "1", "yes"]
                    }
                ]
            }
        ]
    }

    mock_file_content = json.dumps({"enabled": True})

    with patch("compliance_health_check.ROOT") as mock_root:
        mock_path = MagicMock()
        mock_root.__truediv__.return_value = mock_path
        mock_path.is_file.return_value = True
        mock_path.open = mock_open(read_data=mock_file_content)

        expected = {"SIG-02": "active"}
        assert resolve_signal_states(signals_data) == expected


def test_resolve_signal_states_config_inactive():
    signals_data = {
        "signals": [
            {
                "signal_id": "SIG-02",
                "detection": [
                    {
                        "source": "config",
                        "path": "test_config.json",
                        "json_path": "enabled",
                        "active_values": ["true", "1", "yes"]
                    }
                ]
            }
        ]
    }

    mock_file_content = json.dumps({"enabled": False})

    with patch("compliance_health_check.ROOT") as mock_root:
        mock_path = MagicMock()
        mock_root.__truediv__.return_value = mock_path
        mock_path.is_file.return_value = True
        mock_path.open = mock_open(read_data=mock_file_content)

        expected = {"SIG-02": "inactive"}
        assert resolve_signal_states(signals_data) == expected


def test_resolve_signal_states_config_missing_file():
    signals_data = {
        "signals": [
            {
                "signal_id": "SIG-02",
                "detection": [
                    {
                        "source": "config",
                        "path": "missing_config.json",
                        "json_path": "enabled",
                        "active_values": ["true", "1", "yes"]
                    }
                ]
            }
        ]
    }

    with patch("compliance_health_check.ROOT") as mock_root:
        mock_path = MagicMock()
        mock_root.__truediv__.return_value = mock_path
        mock_path.is_file.return_value = False

        expected = {"SIG-02": "inactive"}
        assert resolve_signal_states(signals_data) == expected
