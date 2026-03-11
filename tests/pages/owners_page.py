"""
Owners Page Object
"""
from .base_page import BasePage
import time


class OwnersPage(BasePage):
    """Owners page object"""
    
    # Selectors - Find Owners
    TITLE_SELECTOR = "h2"
    SEARCH_BOX_SELECTOR = "#lastName"
    SEARCH_BUTTON_SELECTOR = "button[type='submit']"
    NO_RESULTS_SELECTOR = ".alert-warning"
    
    # Selectors - Owners List
    OWNERS_TABLE_SELECTOR = "#owners"
    OWNER_ROW_SELECTOR = "#owners tbody tr"
    OWNER_LINK_SELECTOR = "#owners a[href*='/owners/']"
    
    # Selectors - Owner Details (using table structure)
    OWNER_NAME_SELECTOR = "table:nth-of-type(2) td b"
    OWNER_ADDRESS_SELECTOR = "table:nth-of-type(2) td:nth-of-type(2)"
    OWNER_CITY_SELECTOR = "table:nth-of-type(2) td:nth-of-type(3)"
    OWNER_TELEPHONE_SELECTOR = "table:nth-of-type(2) td:nth-of-type(4)"
    PETS_SELECTOR = ".table-condensed tr"
    
    # Selectors - Add/Edit Owner Form
    FIRST_NAME_SELECTOR = "#firstName"
    LAST_NAME_SELECTOR = "#lastName"
    ADDRESS_SELECTOR = "#address"
    CITY_SELECTOR = "#city"
    TELEPHONE_SELECTOR = "#telephone"
    SUBMIT_BUTTON_SELECTOR = "button[type='submit']"
    ADD_OWNER_LINK_SELECTOR = "a[href*='/owners/new']"
    EDIT_OWNER_LINK_SELECTOR = "a[href*='/owners/'][href*='/edit']"
    
    def __init__(self, page):
        super().__init__(page)
    
    # ========== Navigation ==========
    
    def goto(self):
        """Navigate to find owners page"""
        super().goto("/owners/find")
    
    def goto_add_owner(self):
        """Navigate to add owner page"""
        super().goto("/owners/new")
    
    # ========== Search Owners ==========
    
    def search_by_lastname(self, lastname: str):
        """Search owners by last name"""
        self.fill(self.SEARCH_BOX_SELECTOR, lastname)
        self.click(self.SEARCH_BUTTON_SELECTOR)
    
    def is_no_results(self) -> bool:
        """Check if no results message is shown"""
        return self.is_visible(self.NO_RESULTS_SELECTOR)
    
    # ========== Owners List ==========
    
    def get_owner_count(self) -> int:
        """Get number of owners in list"""
        return self.page.locator(self.OWNER_ROW_SELECTOR).count()
    
    def click_owner_link(self, index: int = 0):
        """Click on owner link by index"""
        self.page.locator(self.OWNER_LINK_SELECTOR).nth(index).click()
    
    # ========== Owner Details ==========
    
    def get_owner_name(self) -> str:
        """Get owner full name"""
        return self.get_text(self.OWNER_NAME_SELECTOR)
    
    def get_owner_address(self) -> str:
        """Get owner address"""
        return self.get_text(self.OWNER_ADDRESS_SELECTOR)
    
    def get_owner_city(self) -> str:
        """Get owner city"""
        return self.get_text(self.OWNER_CITY_SELECTOR)
    
    def get_owner_telephone(self) -> str:
        """Get owner telephone"""
        return self.get_text(self.OWNER_TELEPHONE_SELECTOR)
    
    def get_pet_count(self) -> int:
        """Get number of pets"""
        return self.page.locator(self.PETS_SELECTOR).count()
    
    def get_owner_info(self) -> dict:
        """Get complete owner information"""
        return {
            "name": self.get_owner_name(),
            "address": self.get_owner_address(),
            "city": self.get_owner_city(),
            "telephone": self.get_owner_telephone(),
            "pet_count": self.get_pet_count()
        }
    
    # ========== Add/Edit Owner ==========
    
    def fill_owner_form(self, first_name: str, last_name: str, address: str, city: str, telephone: str):
        """Fill owner form"""
        self.fill(self.FIRST_NAME_SELECTOR, first_name)
        self.fill(self.LAST_NAME_SELECTOR, last_name)
        self.fill(self.ADDRESS_SELECTOR, address)
        self.fill(self.CITY_SELECTOR, city)
        self.fill(self.TELEPHONE_SELECTOR, telephone)
    
    def submit_form(self):
        """Submit the form"""
        self.click(self.SUBMIT_BUTTON_SELECTOR)
    
    def create_owner(self, first_name: str, last_name: str, address: str, city: str, telephone: str):
        """Create a new owner"""
        self.goto_add_owner()
        self.fill_owner_form(first_name, last_name, address, city, telephone)
        self.submit_form()
