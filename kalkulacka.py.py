print("Kalkulačka Mechaniky")

while True:
    print("\nVyber Operaci:")
    print("1. Vypočítej Sílu")
    print("2. Vypočítej Výkon")
    print("3. Vypočítej Rychlost")
    print("4. Odejít")

    choice = int(input("Vyber Číslo (1-4): "))

    if choice == 1:
        force = float(input("Vlož Sílu (in Newtons): "))
        velocity = float(input("Vlož Rychlost (v metrech za sekundu): "))
        power = force * velocity
        print("Výkon = ", power, " Watů")

    elif choice == 2:
        power = float(input("Vlož Výkon (ve Watech): "))
        velocity = float(input("Vlož rychlost (v metrech za sekundu): "))
        force = power / velocity
        print("Síla = ", force, " Newton")

    elif choice == 3:
        power = float(input("Vlož Výkon (ve Watech): "))
        force = float(input("Vlož Sílu (v Newtonech): "))
        velocity = power / force
        print("Rychlost = ", velocity, " metry za sekundu")

    elif choice == 4:
        break

    else:
        print("Nesprávná volba")

print("Díks Bráško")
