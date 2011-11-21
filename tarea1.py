#!/usr/bin/python
# -*- coding: utf-8 -*-

nombre =raw_input ('Como te llamas?')
print 'Hola %s, cuantos años tienes?' % (nombre) 

def get_num_required_tables (nr_anios):
   return nr_anios + 1

anios= int(raw_input())
tables = get_num_required_tables(anios)
print 'El proximo años cumpliras %d' % (tables)
