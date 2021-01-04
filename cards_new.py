from faker import Faker
fake = Faker("pl_PL")

class BaseContact:
    def __init__(self, first_name, last_name, email_address, tel_priv):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.tel_priv = tel_priv

    def __repr__(self):
        return f"{self.first_name} {self.last_name}, {self.email_address}"

    def contact(self):
        return f"Wybieram numer domowy: {self.tel_priv} i dzwonię do {self.first_name} {self.last_name} "
    
    def workcontact(self):
        return f"Wybieram numer służbowy: {self.tel_work} i dzownię do {self.first_name} {self.last_name}"
    
    @property
    def label_lenght(self):
        return sum([len(self.first_name), len(self.last_name),+1])

class BusinessContact(BaseContact):
    def __init__(self, tel_work, company, occupation, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tel_work = tel_work
        self.company = company
        self.occupation = occupation

    def __repr__(self):
        return f"{self.first_name} {self.last_name}, {self.email_address}, {self.occupation}, {self.company}"

people = []
for i in range(5):
    person = BusinessContact(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        company=fake.company(),
        occupation=fake.job(),
        email_address=fake.email(),
        tel_priv=fake.phone_number(), 
        tel_work=fake.phone_number()
    )
    people.append(person)

for person in people:
    print(person)
    print(person.contact())
    print(person.workcontact())
    print(person.label_lenght, end="\n\n")

def generate_business_data():
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "company": fake.company(),
        "occupation": fake.job(),
        "email_address": fake.email(),
        "tel_priv": fake.phone_number(), 
        "tel_work": fake.phone_number()
    }

def generate_base_data():
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email_address": fake.email(),
        "tel_priv": fake.phone_number()
    }

def create_contacts(kind, how_many):
    contact_type = BusinessContact if kind == "b" else BaseContact
    generate_data = generate_business_data if kind == "b" else generate_base_data
    contacts = []

    for i in range(how_many):
        contact = contact_type(**generate_data())
        contacts.append(contact)

    return contacts

if __name__ == "__main__":
    kind = input("Jaki rodzaj wizytówki? b - biznesowa, d - domowa: ")
    how_many = int(input('Proszę podaj liczbę wizytówek do stworzenia '))
    contacts = create_contacts(kind, how_many)
    for contact in contacts:
        print(contact)