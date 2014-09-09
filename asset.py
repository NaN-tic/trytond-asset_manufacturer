#The COPYRIGHT file at the top level of this repository contains the full
#copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Asset']
__metaclass__ = PoolMeta


class Asset:
    __name__ = 'asset'
    manufacturer = fields.Many2One('party.party', 'Manufacturer',
        domain=[
            ('manufacturer', '=', True),
            ])
    manufacture_date = fields.Date('Manufacture Date')
    serial_number = fields.Char('Serial Number')
