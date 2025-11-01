from pydantic import BaseModel
from typing import Optional, List
# from humps import camelize

# class CamelModel(BaseModel):
#     class Config:
#         alias_generator = camelize
#         allow_population_by_field_name = True

class RailcarForm(BaseModel):
    car_mark: Optional[str]
    car_number: Optional[int]
    is_repaired: List[bool]
    is_empty: List[bool]
    inspected_date: Optional[str]
    repair_description: Optional[str]
    is_bad_ordered: Optional[bool]
    # add more fields when I implement bad order schema
