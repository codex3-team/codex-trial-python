from pydantic import BaseModel, ValidationError, validator, constr
import utils.errors as errors

class CarBase(BaseModel):
    make: constr(max_length=128)
    model: constr(max_length=128)
    year: constr(max_length=4)

class CarSerializer(CarBase):
    @validator('make')
    def make_size(cls, v):
        cls.check_size(v, 128)

    @validator('model')
    def model_size(cls, v):
        cls.check_size(v, 128)

    @validator('year')
    def year_is_digit(cls, v):
        cls.check_size(v, 4)
        v.isdigit()
        assert v.isdigit(), errors.year_format

    @classmethod
    def check_size(cls, v, size):
        if not v:
            raise ValueError(errors.empty)
        if len(v) > size:
            raise ValueError(errors.length)


    