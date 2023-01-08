from locale import currency
from pydantic import BaseModel, validator


class products(BaseModel):

    isjunior: bool
    lenscolor: str
    img: str
    isfindinstore: bool
    iscustomizable: bool
    roxablelabel: str
    brand: str
    imghover: str
    ispolarized: bool
    colorsnumber: int
    isoutofstock: bool
    modelname: str
    isengravable: bool
    localizedcolorlabel: str
    listprice: float
    offerprice: float
    extractdate: str

    @validator('modelname')
    def not_null_modelname(cls,modelname):
        if modelname == '':
            raise ValueError("modelname can't be null")
        return modelname
    
    @validator('lenscolor')
    def not_null_lenscolor(cls,lenscolor):
        if lenscolor == '':
            raise ValueError("lenscolor can't be null")
        return lenscolor
    
    @validator('localizedcolorlabel')
    def not_null_localizedcolorlabel(cls,localizedcolorlabel):
        if localizedcolorlabel == '':
            raise ValueError("localizedcolorlabel can't be null")
        return localizedcolorlabel
