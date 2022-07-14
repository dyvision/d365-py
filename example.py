from d365 import *

#initializes connection
d = d365(
    'cooldomain.crm.dynamics.com',
    'clientidfromazure',
    'clientsecretfromazure',
    'redirectthatyouapprovedinazure'
    )

#returns authorization url
d.authorize()

#returns token data using authorization code
d.authenticate('codeprovidedbytheredirect')

#returns token data using refresh token
d.refresh('refreshtokenprovidedbyauthenticatefunction')

#lists records with a possible query string
d.list('accounts','?$top=10&$select=name')

#gets specific record
d.get('accounts','56959192-354e-eb11-a813-000d3a1026fe')

#creates a record
d.create('contacts',{'lastname':'thisisatest'})

#updates a record
d.update('contacts','6e1900e0-ac03-ed11-82e4-000d3a124166',{'firstname':'cool'})

#deletes a record
d.delete('contacts','6e1900e0-ac03-ed11-82e4-000d3a124166')