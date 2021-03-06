from json import load
names = []

if __name__ == '__main__':
    with open('names.json', 'r', encoding="utf-8") as f:
        names = load(f)
    int_names = []

    for n in names:
        res = ""
        for c in n:
            res += format(ord(c), '#010b')[2:]
        n = int(res, 2)
        int_names.append(n)

    # Chiffrement
    e = 3
    N = 220478789817846954008896827602146367603094186433902301475580185326213147774974463568692934890539198859855657088843791812533934329430965590114300437318317493890419646373788600314386915862469488995282327815811651143941633771533313955261186965943450155559547749180570873514941111463488772476223162962462970403644521663926858260772192374690667413278915622458501295488132742868927845060077023118972377392538762951151478892289332594612454083158506799745502768698226340978287299829036559684871978533451545448158415420055209724921039601333963345411636216097481662566260428364429674778488994313135030853675723
    rsa_names = []

    for n in int_names:
        rsa_names.append(pow(n, e) % N)

    # Recherche de correspondence
    for i in range(len(names)):
        if rsa_names[i] == 16250093121834914738489778721283850815023220823910545716502847730384833157965639674158854530545421681485384544525983824875:
            print(names[i])
            print(int_names[i])
            print(rsa_names[i])

    # Dump des listes pour le debuggage.
    print("\n--DUMP--")
    print(f'--NOM:{names[0]}--')
    print(f'--INT:{int_names[0]}--')
    print(f'--RSA:{rsa_names[0]}--')
    print(f'--INT:{len(int_names)}--')
    print(f'--INT:{len(int_names)}--')
    print(int_names)
    print(f"--RSA:{len(rsa_names)}--")
    print(rsa_names)
    print(f"--NAMES:{len(names)}--")
    print(names)
