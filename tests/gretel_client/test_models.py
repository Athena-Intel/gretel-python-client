import json
import tempfile

from pathlib import Path
from typing import Callable, List
from unittest.mock import MagicMock

import pytest
import yaml

from gretel_client.config import RunnerMode
from gretel_client.projects.models import Model, ModelConfigError, read_model_config


@pytest.fixture
def transform_model_path(get_fixture: Callable) -> Path:
    return get_fixture("transforms_config.yml")


@pytest.fixture
def transform_local_data_source(get_fixture: Callable) -> Path:
    return get_fixture("account-balances.csv")


@pytest.fixture
def create_model_resp(get_fixture: Callable) -> dict:
    return json.loads(get_fixture("api/create_model.json").read_text())


@pytest.fixture
def get_model_resp(get_fixture: Callable) -> dict:
    return json.loads(get_fixture("api/completed_model_details.json").read_text())


@pytest.fixture
def create_record_handler_resp(get_fixture: Callable) -> dict:
    return json.loads(get_fixture("api/create_record_handler.json").read_text())


@pytest.fixture
def model_logs() -> List[dict]:
    return [
        {
            "ts": "2021-05-12T03:15:36.609784Z",
            "msg": "Starting transforms model training",
            "ctx": {},
            "seq": 1,
            "stage": "pre",
        },
        {
            "ts": "2021-05-12T03:15:36.610693Z",
            "msg": "Loading training data",
            "ctx": {},
            "seq": 2,
            "stage": "pre",
        },
        {
            "ts": "2021-05-12T03:15:36.908586Z",
            "msg": "Training data loaded",
            "ctx": {"record_count": 302, "field_count": 9},
            "seq": 3,
            "stage": "pre",
        },
        {
            "ts": "2021-05-12T03:15:36.908854Z",
            "msg": "Beginning transforms model training",
            "ctx": {},
            "seq": 4,
            "stage": "train",
        },
        {
            "ts": "2021-05-12T03:15:48.247923Z",
            "msg": "Saving model archive",
            "ctx": {},
            "seq": 5,
            "stage": "train",
        },
        {
            "ts": "2021-05-12T03:15:48.249298Z",
            "msg": "Generating data preview",
            "ctx": {"num_records": 100},
            "seq": 6,
            "stage": "run",
        },
        {
            "ts": "2021-05-12T03:15:48.249561Z",
            "msg": "Uploading artifacts to Gretel Cloud",
            "ctx": {},
            "seq": 7,
            "stage": "post",
        },
        {
            "ts": "2021-05-12T03:15:48.495138Z",
            "msg": "Model creation complete!",
            "ctx": {},
            "seq": 8,
            "stage": "post",
        },
    ]


@pytest.fixture
def create_artifact_resp() -> dict:
    return {
        "data": {
            "url": "https://gretel-proj-artifacts-us-east-2.s3.amazonaws.com/5fdzfdsf",
            "key": "gretel_dd3a7853b06343f79e645d27ca722a9e_account-balances.csv",
            "method": "PUT",
        }
    }


@pytest.fixture()
def m(
    create_model_resp: dict,
    transform_model_path: Path,
    create_record_handler_resp: dict,
    get_model_resp: dict,
) -> Model:
    projects_api = MagicMock()
    projects_api.get_model.return_value = get_model_resp
    projects_api.create_model.return_value = create_model_resp
    projects_api.create_artifact.return_value = create_artifact_resp
    projects_api.create_record_handler.return_value = create_record_handler_resp
    projects_api.get_record_handler.return_value = {}  # todo
    m = Model(project=MagicMock(), model_config=transform_model_path)
    m._projects_api = projects_api
    return m


@pytest.mark.parametrize("runner_mode", [RunnerMode.CLOUD, "cloud"])
def test_model_create(m: Model, create_model_resp: dict, runner_mode):
    assert m.model_id is None
    m.submit(runner_mode=runner_mode)
    m._projects_api.create_model.assert_called_once()  # type:ignore
    assert isinstance(m._data, dict)
    assert m.model_id == create_model_resp["data"]["model"]["uid"]
    assert m.status == create_model_resp["data"]["model"]["status"]
    assert m.worker_key == create_model_resp["worker_key"]


def test_model_submit_bad_runner_modes(m: Model):
    with pytest.raises(ValueError) as err:
        m.submit(runner_mode="foo")
    assert "Invalid runner_mode: foo" in str(err)

    with pytest.raises(ValueError) as err:
        m.submit(runner_mode=123)
    assert "Invalid runner_mode type" in str(err)


def test_model_submit_no_local_mode(m: Model):
    with pytest.raises(ValueError) as err:
        m.submit(runner_mode="local")
    assert "local" in str(err)


def test_does_poll_status_and_logs(m: Model, model_logs: List[dict]):
    m._submit(runner_mode=RunnerMode.LOCAL, _default_manual=True)
    m._projects_api.get_model.side_effect = [  # type:ignore
        {"data": {"model": {"status": "created"}}},
        {"data": {"model": {"status": "pending"}}},
        {"data": {"model": {"status": "active"}, "logs": model_logs[0:1]}},
        {"data": {"model": {"status": "active"}, "logs": model_logs[0:2]}},
        {"data": {"model": {"status": "active"}, "logs": model_logs[0:5]}},
        {"data": {"model": {"status": "active"}, "logs": model_logs[0:6]}},
        {"data": {"model": {"status": "active"}, "logs": model_logs}},
        {"data": {"model": {"status": "completed"}}},
    ]
    updates = list(m.poll_logs_status())
    assert len(updates) == 8


def test_does_read_remote_model():
    synthetics_blueprint_raw_path = "https://raw.githubusercontent.com/gretelai/gretel-blueprints/main/config_templates/gretel/synthetics/default.yml"  # noqa
    assert read_model_config(synthetics_blueprint_raw_path)
    with pytest.raises(ModelConfigError):
        read_model_config(f"{synthetics_blueprint_raw_path}/dsfljk")


def test_does_read_model_short_path():
    synthetics_blueprint_short_path = "synthetics/default"
    assert read_model_config(synthetics_blueprint_short_path)
    with pytest.raises(ModelConfigError):
        read_model_config("notfound")


def test_does_not_read_bad_local_data():
    with tempfile.NamedTemporaryFile() as tmp_config:
        tmp_config.write(b"\tfoo")  # a regular string loads as YAML
        tmp_config.seek(0)
        with pytest.raises(ModelConfigError) as err:
            read_model_config(tmp_config.name)
        assert "YAML or JSON" in str(err)


def test_does_read_in_memory_model(transform_model_path: Path):
    config = yaml.safe_load(transform_model_path.read_bytes())
    assert read_model_config(config)


def test_does_read_local_model(transform_model_path: Path):
    assert read_model_config(transform_model_path)
    assert read_model_config(str(transform_model_path))


def test_does_populate_record_details(m: Model, create_record_handler_resp: dict):
    m._poll_job_endpoint()
    record_handler = m.create_record_handler_obj()
    record_handler.submit(
        action="transform",
        runner_mode=RunnerMode.LOCAL,
        data_source="path/to/datasource.csv",
        _default_manual=True,
    )
    assert (
        record_handler.status.value
        == create_record_handler_resp["data"]["handler"]["status"]
    )
    assert record_handler.worker_key == create_record_handler_resp["worker_key"]


def test_billing_output(m: Model):
    m._poll_job_endpoint()
    # assert m.billing_details == {"total_billed_seconds": 60, "task_type": "cpu"}
    assert isinstance(m.billing_details, dict)


def test_xf_report_output(m: Model, get_fixture: Callable):
    report_json = get_fixture("xf_report_json.json.gz")
    peek = m.peek_report(str(report_json))
    expected_fields = [
        "training_time_seconds",
        "record_count",
        "field_count",
        "field_transforms",
    ]
    for field in expected_fields:
        assert field in peek.keys()


def test_synth_report_output(m: Model, get_fixture: Callable):
    report_json = get_fixture("synth_report_json.json.gz")
    m.model_config["models"][0] = {
        "synthetics": []
    }  # pretend the model stub is a synthetics model
    peek = m.peek_report(str(report_json))
    expected_fields = [
        "synthetic_data_quality_score",
        "field_correlation_stability",
        "principal_component_stability",
        "field_distribution_stability",
    ]
    for field in expected_fields:
        assert field in peek.keys()
