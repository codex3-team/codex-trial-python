from flask import jsonify, request
from flask.views import MethodView
from playhouse.shortcuts import model_to_dict
from cars.serializers import CarSerializer
from cars.models import CarsModel
from pydantic import ValidationError


class CarsApi(MethodView):
    def get(self, car_id):
        if car_id:
            res = CarsModel.get(CarsModel.id==car_id)
            return jsonify(model_to_dict(res))
        return self._getAll()

    def _getAll(self):
        page = int(request.args.get('page', 0)) + 1
        per_page = 50
        cars_list = CarsModel.select().order_by(CarsModel.year.desc()).paginate(page, per_page).dicts()
        amount = CarsModel.select().count()
        return jsonify({"cars": list(cars_list), "amount": amount })

    def post(self, *args, **kwargs):
        data = request.json
        try:
            CarSerializer(**data)
        except ValidationError as e:
            return jsonify(e.json()), 400
        res = CarsModel.create(**data)
        return jsonify(model_to_dict(res)), 201

    # def put(self, car_id):
    #     data = request.json
    #     try:
    #         CarSerializer(**data)
    #     except ValidationError as e:
    #         return jsonify(e.json()), 400
    #     CarsModel.update(**data).where(CarsModel.id == car_id).execute()
    #     res = CarsModel.get(CarsModel.id==car_id)
    #     return jsonify(model_to_dict(res))

    # def delete(self, car_id):
    #     res = CarsModel.get(CarsModel.id==car_id)
    #     res.delete_instance()
    #     return jsonify(), 204

