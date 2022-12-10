# func to improve names of contract
def change_rts(name):
    if name == 'RIH':
        return 'RTS'
    else:
        return name
    
def get_br_type(name):
    br_list = ['BRH','BRG','BRJ'] #create list of barel
   
    if name in br_list:
        # if it is oil
        res = 'BR'
        return res
    else:
        return name    

def get_si_type(name):
    si_list = ['SIH','SIM','SIH','si','Si'] #create list of si 
   
    if name in si_list:
        # if it is dollar
        res = 'SI'
        return res
    else:
        return name 
    
def get_gd_type(name):
    gd_list = ['GDH','GDJ'] #create list of gold #create list of gd 
   
    if name in gd_list:
        # if it is gold
        res = 'GD'
        return res
    else:
        return name 

def get_sf_type(name):
    sf_list = ['SFH','Spyf'] #create list of gold #create list of sf 
   
    if name in sf_list:
        # if it is SP500
        res = 'SF'
        return res
    else:
        return name 
    