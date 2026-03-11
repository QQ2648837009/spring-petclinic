"""
Pets Page Object
"""
from .base_page import BasePage


class PetsPage(BasePage):
    """Pets page object"""
    
    # Selectors - Pet Details (using table structure)
    PET_NAME_SELECTOR = "table:nth-of-type(2) td b"
    PET_BIRTH_DATE_SELECTOR = "table:nth-of-type(2) td:nth-of-type(2)"
    PET_TYPE_SELECTOR = "table:nth-of-type(2) td:nth-of-type(3)"
    VISITS_SECTION_SELECTOR = ".table-condensed"
    VISIT_ITEM_SELECTOR = ".table-condensed tbody tr"
    
    # Selectors - Add Pet Form
    NAME_SELECTOR = "#name"
    BIRTH_DATE_SELECTOR = "#birthDate"
    TYPE_SELECTOR = "#type"
    ADD_PET_LINK_SELECTOR = "a[href*='/pets/new']"
    SUBMIT_BUTTON_SELECTOR = "button[type='submit']"
    
    # Selectors - Add Visit Form
    VISIT_DATE_SELECTOR = "#date"
    VISIT_DESCRIPTION_SELECTOR = "#description"
    ADD_VISIT_LINK_SELECTOR = "a[href*='/visits/new']"
    
    # Pet types
    PET_TYPES = ["bird", "cat", "dog", "hamster", "lizard", "snake", "rabbit"]
    
    def __init__(self, page):
        super().__init__(page)
    
    # ========== Pet Details ==========
    
    def get_pet_name(self) -> str:
        """Get pet name"""
        return self.get_text(self.PET_NAME_SELECTOR)
    
    def get_pet_birth_date(self) -> str:
        """Get pet birth date"""
        return self.get_text(self.PET_BIRTH_DATE_SELECTOR)
    
    def get_pet_type(self) -> str:
        """Get pet type"""
        return self.get_text(self.PET_TYPE_SELECTOR)
    
    def get_visit_count(self) -> int:
        """Get number of visits"""
        return self.page.locator(self.VISIT_ITEM_SELECTOR).count()
    
    def get_pet_info(self) -> dict:
        """Get complete pet information"""
        return {
            "name": self.get_pet_name(),
            "birth_date": self.get_pet_birth_date(),
            "type": self.get_pet_type(),
            "visit_count": self.get_visit_count()
        }
    
    # ========== Add Pet ==========
    
    def goto_add_pet(self, owner_id: int):
        """Navigate to add pet page for owner"""
        super().goto(f"/owners/{owner_id}/pets/new")
    
    def fill_pet_form(self, name: str, birth_date: str, pet_type: str):
        """Fill pet form"""
        self.fill(self.NAME_SELECTOR, name)
        self.fill(self.BIRTH_DATE_SELECTOR, birth_date)
        self.select_option(self.TYPE_SELECTOR, pet_type)
    
    def submit_pet_form(self):
        """Submit pet form"""
        self.click(self.SUBMIT_BUTTON_SELECTOR)
    
    def add_pet(self, owner_id: int, name: str, birth_date: str, pet_type: str):
        """Add a new pet"""
        self.goto_add_pet(owner_id)
        self.fill_pet_form(name, birth_date, pet_type)
        self.submit_pet_form()
    
    # ========== Add Visit ==========
    
    def goto_add_visit(self, owner_id: int, pet_id: int):
        """Navigate to add visit page"""
        super().goto(f"/owners/{owner_id}/pets/{pet_id}/visits/new")
    
    def fill_visit_form(self, date: str, description: str):
        """Fill visit form"""
        self.fill(self.VISIT_DATE_SELECTOR, date)
        self.fill(self.VISIT_DESCRIPTION_SELECTOR, description)
    
    def submit_visit_form(self):
        """Submit visit form"""
        self.click(self.SUBMIT_BUTTON_SELECTOR)
    
    def add_visit(self, owner_id: int, pet_id: int, date: str, description: str):
        """Add a new visit"""
        self.goto_add_visit(owner_id, pet_id)
        self.fill_visit_form(date, description)
        self.submit_visit_form()
