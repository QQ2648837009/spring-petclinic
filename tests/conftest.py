"""
pytest configuration for Spring PetClinic automation tests
"""
import pytest
import os
import json
from datetime import datetime
from pathlib import Path

# Test configuration
BASE_URL = os.getenv("BASE_URL", "http://localhost:8080")
SCREENSHOT_DIR = Path(__file__).parent / "reports" / "screenshots"
REPORT_DIR = Path(__file__).parent / "reports"


@pytest.fixture(scope="session")
def browser_type_args(browser_type_launch_args):
    """Configure browser launch arguments"""
    return {
        **browser_type_launch_args,
        "headless": True,
    }


@pytest.fixture(scope="session")
def base_url():
    """Base URL for the application"""
    return BASE_URL


@pytest.fixture
def screenshot_dir():
    """Create and return screenshot directory"""
    SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
    return SCREENSHOT_DIR


@pytest.fixture
def save_screenshot(page, screenshot_dir):
    """Fixture to save screenshots on test failure"""
    test_name = os.environ.get("PYTEST_CURRENT_TEST", "unknown").split("::")[-1].split("[")[0]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def _save_screenshot(name="error"):
        screenshot_path = screenshot_dir / f"{test_name}_{timestamp}_{name}.png"
        page.screenshot(path=str(screenshot_path), full_page=True)
        return str(screenshot_path)
    
    return _save_screenshot


@pytest.fixture
def test_data_dir():
    """Return the data directory path"""
    return Path(__file__).parent / "data"


def pytest_configure(config):
    """Configure pytest"""
    # Register custom markers
    config.addinivalue_line("markers", "smoke: smoke tests")
    config.addinivalue_line("markers", "regression: regression tests")


def pytest_runtest_makereport(item, call):
    """Hook to capture screenshot on test failure"""
    if call.when == "call" and call.excinfo is not None:
        # Test failed - screenshot will be saved by save_screenshot fixture
        pass
