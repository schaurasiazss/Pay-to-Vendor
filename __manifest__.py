
{
    'name': 'Pay_to_Vendor',
    'version': '1.2',
    'summary': 'Architect',
    'description': """
This module contains all the common features of Hospital Management .
    """,
    # 'depends':[
    #     'base'
    # ],
    'data': [
         'views/pay_to_vendor_wizard.xml',
         'views/Pay_to_Vendor_menus.xml',
         'security/ir.model.access.csv',
        
     
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
