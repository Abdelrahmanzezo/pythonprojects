import sqlite3
# Create  and Connect database
db = sqlite3.connect("appp.db")

# setting up courser
cr = db.cursor()


def commit_and_close():
    """commit changes and save connection to Database"""
    db.commit()
    db.close()
    print("database is Committed and closed")



uid = 1
input_message = """
What Do You Want To Do ?
"s" => Show All Skills
"a" => Add New Skill
"d" => Delete A Skill
"u" => Update Skill Progress
"q" => Quit The App
Choose Option:
"""

# Input Option Choose
user_input = input(input_message).strip().lower()

# Command List
commands_list = ["s", "a", "d", "u", "q"]

# Define The Methods

def show_skills():
    cr.execute(f"select * from skills where user_id ={uid} ")
    results = cr.fetchall()
    print(f"you have {len(results)} skills.....")
    if len(results) > 0:
       print("showing your skills")
    for row in results:
        print(f"skill {row[0]},", end=" ")
        print(f"progress => {row[1]}%")
    commit_and_close()

def add_skill(): 
        skl = input("Enter a skill :").strip().capitalize()
        prog = input("Enter the  progress of the skill ").strip()
        cr.execute(f"insert into skills (name, progress, user_id) values('{skl}','{prog}',{uid})")
        commit_and_close()
def delete_skill():
    skl = input("Enter the skill you want to delete ").strip()
    cr.execute(f"delete from skills where name = '{skl}' and user_id ={uid}")
    commit_and_close()
def update_skill():
    skl =input("Enter the skill you want to change ").strip().capitalize()
    prog =input("Enter the progress of the skill ").strip()
    cr.execute(f"update skills set name ='{skl}',progress ='{prog}' where user_id ={uid}")
    commit_and_close()


# Check If Command Is Exists
if user_input in commands_list:

  print(f"Command Found {user_input}")

  if user_input == "s":

    show_skills()

  elif user_input == "a":

    add_skill()

  elif user_input == "d":

    delete_skill()

  elif user_input == "u":

    update_skill()

  else:

    print("App Is Closed.")
    commit_and_close()
else:

  print(f"Sorry This Command \"{user_input}\" Is Not Found")
