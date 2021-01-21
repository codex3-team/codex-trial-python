from django.test import TestCase, Client, RequestFactory
from rest_framework.test import APIRequestFactory

from app_cars import models as app_cars_models
from app_cars import views as app_cars_views
from django.conf import settings





class CarTest(TestCase):


    def setUp(self):
        self.factory = APIRequestFactory()

        for i in range(20):
            app_cars_models.Car.objects.create(
                make='TestMake' + str(i),
                model='TestModel' + str(i),
                year='2021')


    def tearDown(self):
        pass

    def test_car_list(self):
        """Testing:
            — response status
            — pagination - items on page
            — response structure
        """
        request = self.factory.get('/car_list/')
        response = app_cars_views.car_list(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 10)
        self.assertTrue('make' in response.data[0])
        self.assertTrue('model' in response.data[0])
        self.assertTrue('year' in response.data[0])

    def test_car_entry(self):
        """Testing:
            — response status
            — object creation
            — required fields
            — year length validation
        """
        data = {
            'make': 'newmake',
            'model': 'newmodel',
            'year': '1900'
        }
        request = self.factory.post('/car_list/',data)
        response = app_cars_views.car_list(request)

        self.assertEqual(response.status_code, 200)

        car = app_cars_models.Car.objects.last()
        self.assertEqual(car.make, 'newmake')
        self.assertEqual(car.model, 'newmodel')
        self.assertEqual(car.year, '1900')



        data = {
            'make': 'newmake',
            'model': 'newmodel',
            'year': ''
        }
        request = self.factory.post('/car_list/',data)
        response = app_cars_views.car_list(request)
        self.assertEqual(response.status_code, 400)

        data = {
            'make': 'newmake',
            'model': '',
            'year': '1900'
        }
        request = self.factory.post('/car_list/',data)
        response = app_cars_views.car_list(request)
        self.assertEqual(response.status_code, 400)


        data = {
            'make': '',
            'model': 'newmodel',
            'year': '1900'
        }
        request = self.factory.post('/car_list/',data)
        response = app_cars_views.car_list(request)
        self.assertEqual(response.status_code, 400)

        data = {
            'make': 'newmake',
            'model': 'newmodel',
            'year': '19001'
        }
        request = self.factory.post('/car_list/',data)
        response = app_cars_views.car_list(request)
        self.assertEqual(response.status_code, 400)

    def test_car_access(self):
        """Testing:
            — allowed methods
        """
        request = self.factory.put('/car_list/')
        response = app_cars_views.car_list(request)
        self.assertEqual(response.status_code, 405)

        request = self.factory.delete('/car_list/')
        response = app_cars_views.car_list(request)
        self.assertEqual(response.status_code, 405)
