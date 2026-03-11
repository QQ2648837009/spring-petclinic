"""
Veterinarians Page Object - Uses JSON API
"""
from .base_page import BasePage
import requests
import json


class VetsPage(BasePage):
    """Veterinarians page object"""
    
    # API endpoint
    API_URL = "/vets"
    
    def __init__(self, page):
        super().__init__(page)
        self.base_url = "http://localhost:8080"
    
    def goto(self):
        """Navigate to veterinarians page"""
        super().goto(self.API_URL)
    
    def is_loaded(self) -> bool:
        """Check if vets page is loaded"""
        return "PetClinic" in self.page.title() or self.page.url.endswith("/vets")
    
    def get_title(self) -> str:
        """Get page title"""
        return self.page.title()
    
    def get_vets_from_api(self) -> list:
        """Get veterinarians data from API"""
        response = requests.get(f"{self.base_url}{self.API_URL}")
        data = response.json()
        
        vets = []
        for vet in data.get("vetList", []):
            specialties = [s.get("name") for s in vet.get("specialties", []) if s.get("name")]
            
            vets.append({
                "id": vet.get("id"),
                "name": f"{vet.get('firstName', '')} {vet.get('lastName', '')}".strip(),
                "first_name": vet.get("firstName"),
                "last_name": vet.get("lastName"),
                "specialties": specialties,
                "nr_of_specialties": vet.get("nrOfSpecialties", 0)
            })
        
        return vets
    
    def get_vet_count(self) -> int:
        """Get number of veterinarians"""
        vets = self.get_vets_from_api()
        return len(vets)
    
    def get_vet_names(self) -> list:
        """Get list of veterinarian names"""
        vets = self.get_vets_from_api()
        return [v["name"] for v in vets]
    
    def get_all_vets_info(self) -> list:
        """Get all veterinarians information"""
        return self.get_vets_from_api()
