def main():
    print("This program converts PAK Rupee to CAD")
    print()

    PAK_Rupee = eval(input("Enter ammount in Dollars "))
    CAD_dollars = convert_to_pak(PAK_Rupee)

    print("That is", CAD_dollars, "CAD dollars.")


convert_to_pak = lambda PAK_Rupee: PAK_Rupee * 224.62


main()