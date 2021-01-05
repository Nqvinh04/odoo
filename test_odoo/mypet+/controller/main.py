import odoo
import json
import logging
_logger = logging.getLogger(__name__)

class MyPetAPIInherit(odoo.addons.mypet.controllers.main.MyPetAPI):
    @odoo.http.route()

