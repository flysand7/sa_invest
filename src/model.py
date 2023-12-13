
import enum
import datetime

class District:
    id:                 int
    name:               str

class City:
    id:                 int
    name:               str

class Address:
    id:                 int
    district_id:        int
    city_id:            int
    post_code:          str
    address:            str

class Business_Org:
    id:                 int
    name:               str
    name_short:         str
    inn:                str
    ogrn:               str
    address_id:         int

class Business_Man:
    id:                 int
    last_name:          str
    first_name:         str
    middle_name:        str
    inn:                str
    ogrn:               str
    address_id:         int

class Owner:
    id:                 int
    business_org_id:    int
    business_man_id:    int

class Owner_Contact:
    id:                 int
    owner_id:           int

class Industry:
    id:                 int
    name:               str

Support_Type = enum.StrEnum('Support_Type', [
    'Financial'
])

Unit = enum.StrEnum('Unit', [
    'RUB',
])

class Support:
    id:                 int
    project_id:         int
    support_program_id: int
    support_org_id:     int
    date_start:         datetime.date
    date_end:           datetime.date
    amount:             float
    unit:               Unit
    desc:               str

Decision_Type = enum.StrEnum('Decision_Type', [
    '',
])

class Decision:
    id:                 int
    project_id:         int
    decision_type:      Decision_Type
    decision_date:      datetime.date
    protocol_number:    str
    decision:           str

class Project:
    id:                 int
    user_id:            int
    owner_id:           int
    address_id:         int
    industry_id:        int
    name:               str
    app_own_amount:     float
    app_sup_amount:     float
    work_place_count:   int
    tax_amount:         int
    desk:               list[int]

User_Role = enum.StrEnum('User_Role', [
    'Normal',
    'Admin',
])

class User:
    id:                 int
    role:               User_Role
