sword_charge = 50
shield_energy = 88

if (sword_charge < 90 and shield_energy < 50):
    print("Your sword charge is too low to battle this dragon. Also, beware of low shield energy.")

elif (sword_charge >= 90 and shield_energy < 50):
    print("Beware of low shield energy. Sword charge is spot on!")

elif (sword_charge < 90 and shield_energy >= 50):
    print("Beware of low sword charge. Shield energy is spot on!")
else:
    print("May be the force be with you!")


