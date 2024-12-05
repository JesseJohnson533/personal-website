def set_menu(section):
    
    menuconfig = {}
    
    if len(section)>0:
        menuconfig[section]="active"

    return menuconfig