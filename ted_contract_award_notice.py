from pydantic import BaseModel
from typing import List, Optional

class Money(BaseModel):
    currency: str
    ammount: int

class Address(BaseModel):
    street: Optional[str] = None
    city: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    nuts_code: Optional[str] = None


class Contact(BaseModel):
    person: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    website: Optional[str] = None


class ContractingBody(BaseModel):
    official_name: str
    national_registration_number: Optional[str] = None
    address: Address
    contact: Contact
    main_activity:  Optional[str] = None


class Lot(BaseModel):
    lot_number: int
    title: Optional[str] = None
    nuts_code: Optional[str] = None
    description: str
    award_criteria: Optional[str] = None
    contract_awarded: bool
    non_award_reason:  Optional[str] = None


class Contractor(BaseModel):
    official_name: str
    address: Address
    sme: bool


class AwardedContract(BaseModel):
    contract_number: int
    date_of_award: str
    number_of_tenders_received: int
    sme_tenders: int
    contractor: Contractor
    total_value: Money


class ReviewBody(BaseModel):
    name: str
    address: Address
    email: Optional[str] = None
    website: Optional[str] = None


class ContractDetails(BaseModel):
    title: Optional[str] = None
    reference_number: str
    main_cpv_code: str
    type_of_contract: Optional[str] = None
    procedure: Optional[str] = None
    contract_value: Money
    lots: List[Lot]


class TedContractAwardNotice(BaseModel):
    notice_id: str
    publication_date: date
    url: str
    contracting_bodies: List[ContractingBody]
    contract_details: ContractDetails
    awarded_contract: Optional[AwardedContract] = None
    review_information: Optional[ReviewBody] = None
