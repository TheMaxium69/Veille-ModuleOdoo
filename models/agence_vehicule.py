from odoo import models, fields


class AgenceVehiculeStatus(models.Model):
    _name = 'agence.vehicule.status'
    _description = 'Statut du Véhicule'

    name = fields.Char('Nom du Statut', required=True)
    color = fields.Integer('Couleur')


class AgenceVehicule(models.Model):
    _name = 'agence.vehicule'

    marque = fields.Char('Marque', required=True)
    modele = fields.Char('Modèle', required=True)
    date_achat = fields.Date('Date d Achat')

    status_id = fields.Many2one('agence.vehicule.status', string='Statut')

    chaffeur_ids = fields.Many2many('res.partner', string='Chaffeurs')

    notes = fields.Text('Notes Internes')
    description_web = fields.Html('Description Riche')