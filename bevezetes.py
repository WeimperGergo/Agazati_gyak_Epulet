def jatekos():
    print(f"I/A:")
    jNev = input("\tJátékos neve: ")
    jSzerep = input("\tszerepkör: ")

    if jSzerep == "varázsló":
        print(f"\tÜdvözlünk {jNev}, 2 életed van!")
    elif jSzerep == "harcos":
        print(f"\tÜdvözlünk {jNev}, 10 életed van!")
    else:
        print(f"\tÜdvözlünk {jNev}, 8 életed van!")


