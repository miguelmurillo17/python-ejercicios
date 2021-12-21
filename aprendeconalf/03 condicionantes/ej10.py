# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
ingredientes_base = ['mozzarella','tomate']
ingredientes_vegetarianos = ['pimiento','tofu']
ingredientes_no_vegetarianos = ['peperoni','jamon','salmon']
ingrediente_elegido = input('Ingrediente: ')
ingredientes_base.append(ingrediente_elegido)
for ingrediente in ingredientes_vegetarianos:
    if ingrediente == ingrediente_elegido:
        descripcion_pizza = 'Su pizza SI es vegetariana'
for ingrediente in ingredientes_no_vegetarianos:
    if ingrediente == ingrediente_elegido:
        descripcion_pizza = 'Su pizza NO es vegetariana'
print(descripcion_pizza)
print('Los ingredientes son los siguientes:')
for ingrediente in ingredientes_base:
    print('- ',ingrediente)
