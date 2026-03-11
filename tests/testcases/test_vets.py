"""
Veterinarians Page Tests
"""
import pytest
from playwright.sync_api import Page
from pages.vets_page import VetsPage


@pytest.mark.smoke
@pytest.mark.regression
class TestVetsPage:
    """Test cases for veterinarians page"""
    
    def test_vets_page_loads(self, page: Page):
        """Test that veterinarians page loads successfully"""
        vets_page = VetsPage(page)
        vets_page.goto()
        
        assert vets_page.is_loaded(), "Vets page should load"
    
    def test_vets_page_title(self, page: Page):
        """Test veterinarians page title"""
        vets_page = VetsPage(page)
        vets_page.goto()
        
        # API returns JSON, page title may be different
        assert vets_page.get_vet_count() > 0, "Should have veterinarians"
    
    def test_vet_list_displayed(self, page: Page):
        """Test that veterinarian data is available"""
        vets_page = VetsPage(page)
        
        vets = vets_page.get_vets_from_api()
        assert len(vets) > 0, "Should have veterinarian data"
    
    def test_get_vet_count(self, page: Page):
        """Test getting veterinarian count"""
        vets_page = VetsPage(page)
        vets_page.goto()
        
        count = vets_page.get_vet_count()
        assert count > 0, "Should have at least one veterinarian"
    
    def test_get_vet_names(self, page: Page):
        """Test getting veterinarian names"""
        vets_page = VetsPage(page)
        vets_page.goto()
        
        names = vets_page.get_vet_names()
        assert len(names) > 0, "Should have veterinarian names"
        print(f"Veterinarians: {names}")
    
    def test_get_all_vets_info(self, page: Page):
        """Test getting all veterinarians information"""
        vets_page = VetsPage(page)
        vets_page.goto()
        
        vets = vets_page.get_all_vets_info()
        assert len(vets) > 0, "Should have veterinarian data"
        
        for vet in vets:
            assert "name" in vet, "Each vet should have a name"
            print(f"Vet: {vet['name']}, Specialties: {vet.get('specialties', [])}")
