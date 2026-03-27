# -*- coding: utf-8 -*-
{
    "name": "Custom POS Branding",
    "version": "19.0.1.0.0",
    "summary": "Remove default branding from POS interfaces",
    "category": "Sales/Point of Sale",
    "depends": ["point_of_sale", "pos_restaurant"],
    "data": [
        "views/pos_branding_views.xml"
    ],
    "assets": {
        "point_of_sale._assets_pos": [
            "custom_pos_branding/static/src/xml/branding_overrides.xml",
            "custom_pos_branding/static/src/scss/branding_overrides.scss"
        ]
    },
    "installable": True,
    "application": False,
    "license": "LGPL-3"
}
