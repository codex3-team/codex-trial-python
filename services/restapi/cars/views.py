from flask import jsonify, request
from db.models import CarsModel
from utils.utils import RESPONSE_200, RESPONSE_204, RESPONSE_400
from flask.views import MethodView
from playhouse.shortcuts import model_to_dict
from cars.serializers import CarSerializer
from pydantic import ValidationError


class CarsApi(MethodView):
    def get(self, car_id):
        if car_id:
            res = CarsModel.get(CarsModel.id==car_id)
            return model_to_dict(res)
        return self._getAll()

    def _getAll(self):
        page = int(request.args.get('page', 0)) + 1
        per_page = 50
        cars_list = CarsModel.select().order_by(CarsModel.year.desc()).paginate(page, per_page).dicts()
        amount = CarsModel.select().count()
        return RESPONSE_200({"cars": list(cars_list), "amount": amount })

    def post(self, *args, **kwargs):
        data = request.json
        try:
            CarSerializer(**data)
        except ValidationError as e:
            return RESPONSE_400(e.json())
        res = CarsModel.create(**data)
        return RESPONSE_200(model_to_dict(res))

    # def put(self, car_id):
    #     data = request.json
    #     try:
    #         CarSerializer(**data)
    #     except ValidationError as e:
    #         return RESPONSE_400(e)
    #     CarsModel.update(**data).where(CarsModel.id == car_id).execute()
    #     res = CarsModel.get(CarsModel.id==car_id)
    #     return RESPONSE_200(model_to_dict(res))

    # def delete(self, car_id):
    #     res = CarsModel.get(CarsModel.id==car_id)
    #     res.delete_instance()
    #     return RESPONSE_204

