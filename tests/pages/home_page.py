"""
Home Page Object
"""
from .base_page import BasePage


class HomePage(BasePage):
    """Home page object"""
    
    # Selectors
    TITLE_SELECTOR = "h2"
    WELCOME_TEXT_SELECTOR = ".heading-2"
    FIND_OWNERS_SELECTOR = "a[href*='owners']"
    VETS_SELECTOR = "a[href*='vets']"
    
    def __init__(self, page):
        super().__init__(page)
    
    def goto(self):
        """Navigate to home page"""
        super().goto("/")
    
    def is_loaded(self) -> bool:
        """Check if home page is loaded"""
        return self.is_visible(self.TITLE_SELECTOR)
    
    def get_title(self) -> str:
        """Get page title"""
        return self.get_text(self.TITLE_SELECTOR)
    
    def click_find_owners(self):
        """Click Find Owners link"""
        self.click(self.FIND_OWNERS_SELECTOR)
    
    def click_vets(self):
        """Click Veterinarians link"""
        self.click(self.VETS_SELECTOR)
