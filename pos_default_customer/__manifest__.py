{
    "name": "POS Default Customer",
    "version": "18.0.1.0.0",
    "category": "Point of Sale",
    "summary": "Sélection automatique d’un client par défaut dans le POS",
    "author": "Prime Tech Services",
    "depends": ["point_of_sale"],
    "data": [
        "views/pos_config_view.xml",
    ],
    "assets": {
        "point_of_sale.assets": [
            "pos_default_customer/static/src/js/pos_default_customer.js",
        ],
    },
    "installable": True,
 
   "application": False,
}
