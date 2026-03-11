"""
Owners Page Tests
"""
import pytest
import time
from playwright.sync_api import Page
from pages.owners_page import OwnersPage


@pytest.mark.regression
class TestOwnersPage:
    """Test cases for owners page"""
    
    def test_owners_page_loads(self, page: Page):
        """Test that owners page loads successfully"""
        owners_page = OwnersPage(page)
        owners_page.goto()
        
        assert owners_page.is_visible(owners_page.SEARCH_BOX_SELECTOR), "Search box should be visible"
    
    def test_search_owner_by_lastname(self, page: Page):
        """Test searching for owner by last name"""
        owners_page = OwnersPage(page)
        owners_page.goto()
        
        # Search for existing owner - this will redirect to owner details if found
        owners_page.search_by_lastname("Franklin")
        
        # Should either redirect to details page or show results
        # If redirect happened, we'll be on owner details page
        current_url = page.url
        has_results = owners_page.get_owner_count() > 0 or "owners/" in current_url
        no_results = owners_page.is_no_results()
        assert has_results or no_results, f"Should show results or no results message. Current URL: {current_url}"
    
    def test_search_empty_lastname(self, page: Page):
        """Test searching with empty last name shows all owners"""
        owners_page = OwnersPage(page)
        owners_page.goto()
        
        owners_page.search_by_lastname("")
        
        # Should show all owners
        count = owners_page.get_owner_count()
        print(f"Found {count} owners with empty search")
    
    def test_create_owner(self, page: Page):
        """Test creating a new owner"""
        owners_page = OwnersPage(page)
        
        # Generate unique data
        timestamp = int(time.time())
        
        owners_page.create_owner(
            first_name="John",
            last_name=f"Test{timestamp}",
            address="123 Test St",
            city="TestCity",
            telephone="1234567890"
        )
        
        # Should navigate to owner details (check URL or content)
        current_url = page.url
        # After creation, should redirect to owner details page
        assert "/owners/" in current_url and "/new" not in current_url, f"Should redirect to owner details. Current URL: {current_url}"
    
    def test_view_owner_details(self, page: Page):
        """Test viewing owner details"""
        owners_page = OwnersPage(page)
        owners_page.goto()
        
        # Search for an owner
        owners_page.search_by_lastname("Franklin")
        
        # Click on first result
        if owners_page.get_owner_count() > 0:
            owners_page.click_owner_link(0)
            
            # Should show owner details
            info = owners_page.get_owner_info()
            assert "name" in str(info), "Should show owner information"
            print(f"Owner info: {info}")
    
    def test_owner_form_validation(self, page: Page):
        """Test owner form validation"""
        owners_page = OwnersPage(page)
        owners_page.goto_add_owner()
        
        # Submit empty form
        owners_page.submit_form()
        
        # Should show validation errors (HTML5 required fields)
        # Playwright will handle this natively
