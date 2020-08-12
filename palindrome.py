def main():
    pal = input("Enter a word to determine if it is a palendrome: ");
    pal2 = pal.replace(" ","");
    pal2 = pal.lower();

    if pal == "quit":
        quit();

    if pal2 == pal2[::-1]:
        print(pal,"is a palendrome");
    else:
        print(pal,"is not a palendrome");

    main();


main()
