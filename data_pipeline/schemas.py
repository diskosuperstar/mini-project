from pydantic import BaseModel

class MetadataBase(BaseModel):
    table_name: str
    column_name: str
    data_type: str
    is_active: bool

class MetadataCreate(MetadataBase):
    pass

class MetadataRead(MetadataBase):
    id: int