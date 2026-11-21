import httpx
from evidentia_cli.client import EvidentiaClient
from evidentia_cli.main import app
from typer.testing import CliRunner

runner = CliRunner()


def test_health_command(monkeypatch) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path == "/api/v1/health"
        return httpx.Response(200, json={"status": "ok"})

    def fake_client() -> EvidentiaClient:
        return EvidentiaClient(
            base_url="http://testserver",
            transport=httpx.MockTransport(handler),
        )

    monkeypatch.setattr(
        "evidentia_cli.main.get_client",
        fake_client,
    )

    result = runner.invoke(app, ["health"])

    assert result.exit_code == 0
    assert "API status: ok" in result.stdout


def test_info_command(monkeypatch) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path == "/api/v1/info"
        return httpx.Response(
            200,
            json={"name": "Evidentia API", "version": "0.1.0"},
        )

    def fake_client() -> EvidentiaClient:
        return EvidentiaClient(
            base_url="http://testserver",
            transport=httpx.MockTransport(handler),
        )

    monkeypatch.setattr(
        "evidentia_cli.main.get_client",
        fake_client,
    )

    result = runner.invoke(app, ["info"])

    assert result.exit_code == 0
    assert "Evidentia API" in result.stdout
    assert "0.1.0" in result.stdout


def test_unavailable_api(monkeypatch) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError(
            "Connection refused",
            request=request,
        )

    def fake_client() -> EvidentiaClient:
        return EvidentiaClient(
            base_url="http://testserver",
            transport=httpx.MockTransport(handler),
        )

    monkeypatch.setattr(
        "evidentia_cli.main.get_client",
        fake_client,
    )

    result = runner.invoke(app, ["health"])

    assert result.exit_code == 1
