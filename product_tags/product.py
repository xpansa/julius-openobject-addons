# -*- coding: utf-8 -*-
###############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013 Julius Network Solutions SARL <contact@julius.fr>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from openerp.osv import fields, orm
from openerp.tools.translate import _

class product_tag(orm.Model):
    _name = "product.tag"
    _columns = {
        'name': fields.char('Tag Name', required=True, size=64),
    }


class product_template(orm.Model):
    _inherit = "product.template"

    _columns = {
        'tag_ids' : fields.many2many('product.tag',
        'product_product_tag_rel',
        'tag_id',
        'product_id',
        'Tags'
        ),
    }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
