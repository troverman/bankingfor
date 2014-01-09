################################################################
####menu.py#####################################################
################################################################

################################
####title#######################
################################  
if request.function == 'index':
    response.title = 'bankingfor'
else:
    response.title = request.function

################################
####meta########################
################################
response.meta.author = 'Trevor Overman'
response.meta.description = 'bankingfor everyone'
response.meta.keywords = 'banking, value, internet'
response.meta.generator = 'subjectivly objective value based banking'

response.logo = A(B('bankingfor'), _class="brand", _href="http://www.bankingfor.com/")