"""
Base Page Object Model - Common methods for all pages
"""
from playwright.sync_api import Page, expect
from pathlib import Path
import json
import time


class BasePage:
    """Base class for all page objects"""
    
    def __init__(self, page: Page):
        self.page = page
    
    def goto(self, path: str = ""):
        """Navigate to a specific path"""
        from conftest import BASE_URL
        self.page.goto(f"{BASE_URL}{path}")
    
    def click(self, selector: str, **kwargs):
        """Click an element"""
        self.page.click(selector, **kwargs)
    
    def fill(self, selector: str, value: str, **kwargs):
        """Fill an input field"""
        self.page.fill(selector, value, **kwargs)
    
    def select_option(self, selector: str, value: str, **kwargs):
        """Select an option from dropdown"""
        self.page.select_option(selector, value, **kwargs)
    
    def get_text(self, selector: str) -> str:
        """Get text content of an element"""
        return self.page.text_content(selector)
    
    def get_attribute(self, selector: str, attr: str) -> str:
        """Get attribute value of an element"""
        return self.page.get_attribute(selector, attr)
    
    def wait_for_selector(self, selector: str, **kwargs):
        """Wait for an element to be visible"""
        self.page.wait_for_selector(selector, **kwargs)
    
    def wait_for_url(self, url: str, **kwargs):
        """Wait for URL to match pattern"""
        self.page.wait_for_url(url, **kwargs)
    
    def is_visible(self, selector: str) -> bool:
        """Check if element is visible"""
        return self.page.is_visible(selector)
    
    def screenshot(self, path: str, full_page: bool = True):
        """Take a screenshot"""
        self.page.screenshot(path=path, full_page=full_page)
    
    def get_current_url(self) -> str:
        """Get current URL"""
        return self.page.url
    
    def reload(self):
        """Reload the page"""
        self.page.reload()
    
    def load_test_data(self, filename: str) -> dict:
        """Load test data from JSON file"""
        data_dir = Path(__file__).parent / "data"
        file_path = data_dir / filename
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    
    def save_test_record(self, record: dict, filename: str = None):
        """Save test run record to JSON file"""
        from conftest import REPORT_DIR
        if filename is None:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"test_record_{timestamp}.json"
        
        report_path = REPORT_DIR / filename
        REPORT_DIR.mkdir(parents=True, exist_ok=True)
        
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(record, f, indent=2, ensure_ascii=False)
        
        return str(report_path)
