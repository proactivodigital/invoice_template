{
    # Name of the Odoo module. This is the name that will appear in the Odoo app list.
    'name': 'Invoice Template',

    # Version of the module. This field specifies the version of the module.
    # In this case, the module version is 17.0.21.12.050100.
    'version': '18.0',

    # List of modules that this module depends on.
    # In this case, the module depends on the 'base' and 'account' modules.
    # These dependencies must be installed for this module to work.
    'depends': ['base', 'account'],

    # Data files that will be loaded when the module is installed.
    # Here, it points to a 'view.xml' file which is likely to contain the views for the invoice template.
    'data': [
        'views/view.xml',
    ],

    # Boolean field that indicates if the module is installable.
    # Set to 'True' so the module can be installed.
    'installable': True,

    # Boolean field that indicates if the module should be automatically installed with its dependencies.
    # Set to 'False' meaning it will not be automatically installed.
    'auto_install': False,

    # License under which the module is released.
    # This module is released under the LGPL-3 (Lesser General Public License version 3).
    'license': "LGPL-3",
}
