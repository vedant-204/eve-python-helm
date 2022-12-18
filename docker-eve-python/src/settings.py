import os
MONGO_HOST= 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME='yourdb'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

CACHE_CONTROL = 'max-age=20'
CACHE_EXPIRES = 20
SORTING = True

people = {
    'item_title': 'person',

    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'lastname'
    },

    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    'resource_methods': ['GET', 'POST'],

    'schema': {
    'firstname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 10,
    },
    'lastname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 15,
        'required': True,
        'unique': True,
    },
    'role': {
        'type': 'list',
        'allowed': ["author", "contributor", "copy"],
    },
    'location': {
        'type': 'dict',
        'schema': {
            'address': {'type': 'string'},
            'city': {'type': 'string'}
        },
    },
    'born': {
        'type': 'datetime',
    },
}
}
works = {    
'cache_control': 'max-age=10,must-revalidate',    
'cache_expires': 10,     
'schema': {        
       'title': {            
         'type': 'string',            
         'required': True,        
      },        
      'description': {   'type': 'string',   },        
      'owner': {            
          'type': 'objectid',            
          'required': True,            
          'data_relation': {                
               'resource': 'people',                
               'embeddable': True            
           },        
       },    
    }
}
DOMAIN = {
    'people': people,
    'works': works,
}
