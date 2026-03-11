"""
Home Page Tests
"""
import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.vets_page import VetsPage
from pages.owners_page import OwnersPage


@pytest.mark.smoke
class TestHomePage:
    """Test cases for home page"""
    
    def test_home_page_loads(self, page: Page):
        """Test that home page loads successfully"""
        home_page = HomePage(page)
        home_page.goto()
        
        assert home_page.is_loaded(), "Home page should load"
        assert "PetClinic" in home_page.get_title() or home_page.is_visible("h2")
    
    def test_navigate_to_vets(self, page: Page):
        """Test navigation to veterinarians page"""
        home_page = HomePage(page)
        home_page.goto()
        
        home_page.click_vets()
        
        vets_page = VetsPage(page)
        assert vets_page.is_loaded(), "Should navigate to vets page"
    
    def test_navigate_to_find_owners(self, page: Page):
        """Test navigation to find owners page"""
        home_page = HomePage(page)
        home_page.goto()
        
        home_page.click_find_owners()
        
        owners_page = OwnersPage(page)
        assert owners_page.is_visible(owners_page.SEARCH_BOX_SELECTOR), "Should show search box"
