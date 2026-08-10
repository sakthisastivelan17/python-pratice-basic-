materials=['steel','iron','carbonfiber']
remover=(input('enter the material toremove:'))
if remover in materials:
    materials.remove(remover)
    print(materials)

else:
    print('material not found')
