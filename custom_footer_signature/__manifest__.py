{
    "name": "Signature vendeur / client sur documents",
    "version": "18.0.1.0.0",
    "category": "Accounting",
    "summary": "Ajoute un tableau de signature vendeur et client sur factures, devis, proforma et reçus",
    "description": """
Ajoute en bas des documents Odoo :
- Facture
- Proforma
- Devis / Commande
- Reçu de paiement

Un tableau avec :
LE VENDEUR | LE CLIENT
pour signature manuscrite.
    """,
    "author": "Prime Tech Services",
    "website": "https://primetechservices.com",
    "license": "LGPL-3",
    "depends": [
        "account",
        "sale"
    ],
    "data": [
        "views/report_footer_signature.xml"
    ],
    "installable": True,
    "application": False,
    "auto_install": False
}
