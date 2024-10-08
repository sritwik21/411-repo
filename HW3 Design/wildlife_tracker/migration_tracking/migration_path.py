from typing import Optional
from wildlife_tracker.habitat_management.habitat import Habitat

class MigrationPath:
    def __init__(self, species: int,
                 start_location: Habitat,
                 destination: Habitat,
                 path_id: int,
                 start_date: str,
                 health_status: Optional[str]=None,
                 duration: Optional[int]=None
                 ):
        pass
    
    def update_migration_path_details(self, **kwargs) -> None:
        pass

    def get_migration_path_details(self) -> dict:
        pass

    