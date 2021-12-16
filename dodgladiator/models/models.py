# -*- coding: utf-8 -*-

from odoo import models, fields, api
import random
import array
import base64



class dodgladiator(models.Model):
    _name = 'dodgladiator.dodgladiator'
    _description = 'dodgladiator.dodgladiator'

    name = fields.Char()
    value = fields.Integer()
    edad = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.edad = float(record.value) / 100







class dodo(models.Model):   
    _name = 'dodgladiator.dodo'
    _description = 'dodgladiator.dodo'


    def _value_nombre_dodo(self):
            nombres = ['Pepe', 'Luis', 'Antonio', 'Fernando','Andres','Enrique', 'Edgar', 'Paco', 'Pablo', 'Carlos', 'Maria', 'Lucia', 'Ana', 'Silvia', 'Carol', 'Sento', 'Rafa', 'Fran', 'Ignacio', 'Alex', 'Tomas', 'Alba']
            numdenombres = len(nombres);
            numaleatorio = random.randrange(numdenombres)
            name = nombres[numaleatorio]
            return name

    name = fields.Char(default=_value_nombre_dodo)
    _sql_constraints = [ ('name_uniq','unique(name)','No se puede repetir el nombre')] 

    def _get_imagenes_dodo(self):
            imagenesdodos = random.choice(self.env['dodgladiator.imagenesdodos'].search([]).mapped(lambda t: t.id))
            print(imagenesdodos)
            return imagenesdodos
    
    image = fields.Many2one('dodgladiator.imagenesdodos', default=_get_imagenes_dodo)     
    image_dodo = fields.Image(related='image.image', max_width=200,
                               max_height=200)


    def _value_salud(self):
            salud = random.randrange(112,131)
            return salud

    salud = fields.Integer(default=_value_salud, readonly = True)



    def _value_ataque(self):
            ataque = random.randrange(15,37)
            return ataque

    ataque = fields.Integer(default=_value_ataque, readonly = True)
    description = fields.Text()
    datacreacion = fields.Date(default= lambda self: fields.Date.today() , readonly = True)


    level = fields.Integer(default="1", readonly=True)


    """ def porcentaje_mejora(self): """
        

    def subir_lvl(self):
            for record in self:
                record.level = record.level + 1
                porcentaje = random.randrange(3,5)
                record.ataque = record.ataque * porcentaje
                record.salud = record.salud * porcentaje
 

            

    reino = fields.Many2one('dodgladiator.reinos', ondelete='set null')



class imagenesdodos(models.Model):
    _name = 'dodgladiator.imagenesdodos'
    _description = 'dodgladiator.imagenesdodos'

    image = fields.Image(max_width=200, max_height=200)



class reinos(models.Model):
    _name = 'dodgladiator.reinos'
    _description = 'dodgladiator.reinos'

    name = fields.Char()
    value = fields.Integer()
    description = fields.Text()

    dodo = fields.One2many('dodgladiator.dodo', 'reino')



class comedor(models.Model):
    _name = 'dodgladiator.comedor'
    _descripcion = 'dodgladiator.comedor'

    def _value_nombre_comedor(self):
        nombres = ["Comedor del infierno", "Comedor de las montañas", "Comedor de las catacumbas", "Comedor del cielo", "Comedor de Dios", "Comedor de Odín", "Comedor de los asesinos", "Comedor de los mendigos", "Comedor de los topacios", "Comedor de las ratas"]
        
        numaleatorio = random.randrange(3)
        comedor = nombres[numaleatorio]
        return comedor
            

    name = fields.Char(default=_value_nombre_comedor)
    descripcion = fields.Text()

    def _value_max_dodos(self):
        numMax = 25
        return numMax
    nummaxdodos = fields.Integer(default=_value_max_dodos , readonly = True)

    def añadir_dodos(self):
        for record in self:
            record.nummaxdodos = record.nummaxdodos + 25


    
