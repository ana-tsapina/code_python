def main(): 
    get_student()
    print(f"{name} from {student["house"]}")


def get_student(): 
    name = input("Name")
    house = input("House: ")
    return (name, house) 


if __name__ == "__main__": 
    main()