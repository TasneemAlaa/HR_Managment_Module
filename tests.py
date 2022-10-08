import unittest
import os

from flask_testing import TestCase
from flask import abort, url_for

from HR_website import create_app, db
from HR_website.models import User, Attendence


class TestBase(TestCase):

    def create_app(self):

        # pass in test configurations
        config_name = 'testing'
        app = create_app(config_name)
        app.config.update(
            SQLALCHEMY_DATABASE_URI=f'sqlite:///{"HRmanagmment.db"}'
        )
        return app

    def setUp(self):
        """
        Will be called before every test
        """

        db.create_all()

        # create test admin user
        admin =User(email = 'admin@mail.com', first_name = 'admin', password = 'admin12', isAdmin = True)

        # create test non-admin user
        employee = User(email = 'emp@mail.com', first_name = 'emp', password = 'test2022', isAdmin = True)

        # save users to database
        db.session.add(admin)
        db.session.add(employee)
        db.session.commit()
        print("admin added")

if __name__ == '__main__':
    unittest.main()