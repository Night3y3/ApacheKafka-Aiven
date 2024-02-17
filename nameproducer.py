import random
from faker.providers import BaseProvider

class NameProvider(BaseProvider):
    def name(self):
        names = [
                    "John", "Mary", "James", "Jennifer", "Robert", "Linda", "Michael", "Elizabeth", "William", "Patricia",
                    "David", "Barbara", "Richard", "Susan", "Joseph", "Jessica", "Thomas", "Sarah", "Charles", "Karen",
                    "Christopher", "Nancy", "Daniel", "Lisa", "Matthew", "Betty", "Anthony", "Dorothy", "Donald", "Sandra",
                    "Mark", "Ashley", "Paul", "Kimberly", "Steven", "Donna", "Andrew", "Emily", "Kenneth", "Carol",
                    "George", "Michelle", "Joshua", "Amanda", "Kevin", "Melissa", "Brian", "Deborah", "Edward", "Stephanie",
                    "Ronald", "Rebecca", "Timothy", "Laura", "Jason", "Sharon", "Jeffrey", "Cynthia", "Ryan", "Kathleen",
                    "Gary", "Amy", "Jacob", "Shirley", "Nicholas", "Angela", "Eric", "Helen", "Stephen", "Anna",
                    "Jonathan", "Brenda", "Larry", "Pamela", "Justin", "Nicole", "Scott", "Emma", "Brandon", "Samantha",
                    "Benjamin", "Katherine", "Gregory", "Christine", "Samuel", "Debra", "Frank", "Rachel", "Patrick", "Carolyn",
                    "Alexander", "Janet", "Raymond", "Ruth", "Jack", "Maria", "Dennis", "Heather", "Jerry", "Diane"
                ]
        
        return names[random.randint(0,len(names) - 1)]