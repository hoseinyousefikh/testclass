import json

file_name = "karvands.json"


try:
    file = open(file_name, "r")
    karvands = json.load(file)
    file.close()
except:
    karvands = []


while True:
    print("\n1. Add Karvand")
    print("2. Show Karvands")
    print("3. Edit Karvand")
    print("4. Delete Karvand")
    print("5. Report")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Full name: ")
        email = input("Email: ")
        city = input("City: ")
        education = input("Education: ")

        skills = []
        number = int(input("Number of skills: "))

        i = 0
        while i < number:
            skill = input("Skill: ")
            skills.append(skill)
            i += 1

        karvand = {
            "name": name,
            "email": email,
            "city": city,
            "education": education,
            "skills": skills,
        }

        karvands.append(karvand)

        file = open(file_name, "w")
        json.dump(karvands, file, indent=4)
        file.close()

        print("Karvand added.")

    elif choice == "2":
        if len(karvands) == 0:
            print("No Karvands found.")
        else:
            i = 0

            while i < len(karvands):
                print("\nKarvand", i + 1)
                print("Name:", karvands[i]["name"])
                print("Email:", karvands[i]["email"])
                print("City:", karvands[i]["city"])
                print("Education:", karvands[i]["education"])
                print("Skills:", karvands[i]["skills"])
                i += 1

    elif choice == "3":
        number = int(input("Karvand number: ")) - 1

        if number >= 0 and number < len(karvands):
            karvands[number]["name"] = input("Full name: ")
            karvands[number]["email"] = input("Email: ")
            karvands[number]["city"] = input("City: ")
            karvands[number]["education"] = input("Education: ")

            skills = []
            skill_number = int(input("Number of skills: "))

            i = 0
            while i < skill_number:
                skill = input("Skill: ")
                skills.append(skill)
                i += 1

            karvands[number]["skills"] = skills

            file = open(file_name, "w")
            json.dump(karvands, file, indent=4)
            file.close()

            print("Karvand updated.")
        else:
            print("Invalid number.")

    elif choice == "4":
        number = int(input("Karvand number: ")) - 1

        if number >= 0 and number < len(karvands):
            new_karvands = []

            i = 0
            while i < len(karvands):
                if i != number:
                    new_karvands.append(karvands[i])
                i += 1

            karvands = new_karvands

            file = open(file_name, "w")
            json.dump(karvands, file, indent=4)
            file.close()

            print("Karvand deleted.")
        else:
            print("Invalid number.")

    elif choice == "5":
        print("\nTotal Karvands:", len(karvands))

    elif choice == "6":
        break

    else:
        print("Invalid choice.")
