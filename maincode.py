import mysql.connector as ms
from mysql.connector.errors import IntegrityError as e

# Database Connection
db = ms.connect(user='election_user', host='localhost', password='election_pass', database='Election')
mycursor = db.cursor()

# Creating Database and Tables
mycursor.execute('CREATE DATABASE IF NOT EXISTS Election')
mycursor.execute('USE Election')
mycursor.execute(
    'CREATE TABLE IF NOT EXISTS Candidates (Candidate_ID int Primary Key, Name'
    ' varchar(100) NOT NULL, Age int NOT NULL, Party varchar(100))'
)
mycursor.execute(
    'CREATE TABLE IF NOT EXISTS Votes(Voter_ID int Primary Key, Candidate_ID'
    ' int, FOREIGN KEY(Candidate_ID) references Candidates(Candidate_ID))'
)
mycursor.execute(
    'CREATE TABLE IF NOT EXISTS Result(Candidate_ID int, Name varchar(100) NOT'
    ' NULL, Age int NOT NULL, Party varchar(100), Votes int NOT NULL, FOREIGN'
    ' KEY(Candidate_ID) references Candidates(Candidate_ID))'
)


def add_candidate():
  while True:
    try:
      candid = int(input("Enter the Candidate ID:"))
      name = input("Enter the Candidate Name:")
      age = int(input("Enter the Age of Candidate:"))
      if not (age >= 25):
        print("A Candidate should be atleast 25 years old")
        continue
      party = input("Enter the Party Name:")
      mycursor.execute(
          "Insert into Candidates values({}, '{}',{},'{}')".format(
              candid, name, age, party
          )
      )
      mycursor.execute(
          "Insert into Result values({},'{}', {},'{}',0)".format(
              candid, name, age, party
          )
      )
      db.commit()
      print("Candidate added")
      break
    except e:
      print("Enter a unique Candidate ID !!")


def vote():
  print(
      "Candidates Information given below in the format (Candidate ID, Name,"
      " Party)"
  )
  mycursor.execute("select Candidate_ID, Name, Party from Candidates")
  data = mycursor.fetchall()
  for x in data:
    print(x)
  while True:
    try:
      voterid = int(input("Enter your Voter ID:"))
      candid = int(input("Enter the Candidate ID of the candidate:"))
      mycursor.execute(
          "Insert into Votes values({}, {})".format(voterid, candid)
      )
      mycursor.execute(
          "Update Result SET Votes=Votes+1 WHERE Candidate_ID={}".format(candid)
      )
      db.commit()
      print("Vote added")
      break
    except e:
      print("You have already voted(VOTER ID repetition)!!")


def candidate_info():
  mycursor.execute("Select * from Candidates")
  data = mycursor.fetchall()
  print(
      "The below info is in the format (Candidate ID, Name, Age, Party Name)"
  )
  for x in data:
    print(x)


def votes_info():
  mycursor.execute("Select * from Votes")
  data = mycursor.fetchall()
  print("The below info is in the format (Voter ID, Candidate ID)")
  for x in data:
    print(x)


def update_candidate():
  mycursor.execute("Select Candidate_ID from Candidates")
  data = mycursor.fetchall()
  t = ()
  for x in data:
    t += x
  while True:
    candid = int(input("Enter Candidate ID:"))
    if candid in t:
      print("1.Update Name")
      print("2.Update Age")
      print("3.Update Party Name")
      opt = int(input("Enter your choice:"))
      if opt == 1:
        name = input("Enter the new name:")
        mycursor.execute(
            "Update Candidates set Name='{}' where Candidate_ID={}".format(
                name, candid
            )
        )
        mycursor.execute(
            "Update Result set Name='{}' where Candidate_ID={}".format(
                name, candid
            )
        )
        print("Name updated")
        db.commit()
        break
      elif opt == 2:
        age = int(input("Enter the new age:"))
        if not (age >= 25):
          print("A Candidate must be atleast 25 years old")
          continue
        mycursor.execute(
            "Update Candidates set Age={} where Candidate_ID={}".format(
                age, candid
            )
        )
        mycursor.execute(
            "Update Result set Age={} where Candidate_ID={}".format(age, candid)
        )
        print("Age updated")
        db.commit()
        break
      elif opt == 3:
        party = input("Enter the new party name:")
        mycursor.execute(
            "Update Candidates set Party='{}' where Candidate_ID={}".format(
                party, candid
            )
        )
        mycursor.execute(
            "Update Result set Party='{}' where Candidate_ID={}".format(
                party, candid
            )
        )
        print("Party Name update")
        db.commit()
        break
      else:
        print("Invalid choice!!")
    else:
      print("Candidate ID does not exist !!")


def delete_candidate():
  mycursor.execute("Select Candidate_ID from Candidates")
  data = mycursor.fetchall()
  t = ()
  s = "y"
  for x in data:
    t += x
  while s == "y" or s == "Y":
    candid = int(input("Enter the Candidate ID:"))
    if candid in t:
      mycursor.execute(
          "Delete from Votes where Candidate_ID={}".format(candid)
      )
      mycursor.execute(
          "Delete from Result where Candidate_ID={}".format(candid)
      )
      mycursor.execute(
          "Delete from Candidates where Candidate_ID={}".format(candid)
      )
      db.commit()
      s = "n"
    else:
      print("Candidate ID not found!!")


def result():
  mycursor.execute("Select * from Result order by Votes desc")
  data = mycursor.fetchall()
  print(
      "The Result displayed below is in the format (Candidate ID, Name, Age,"
      " Party, Votes)"
  )
  for x in data:
    print(x)


# Main Menu Loop
print("Welcome to Election Management System")
while True:
  print("---------------------------------")
  print("1.Add Candidate")
  print("2.Update Candidate")
  print("3.Delete Candidate")
  print("4.Display Candidate information")
  print("5.Vote")
  print("6.Display Vote insertion details")
  print("7.Display Result")
  print("8.Exit")
  x = int(input("Enter your choice:"))
  if x == 1:
    add_candidate()
  elif x == 2:
    update_candidate()
  elif x == 3:
    delete_candidate()
  elif x == 4:
    candidate_info()
  elif x == 5:
    vote()
  elif x == 6:
    votes_info()
  elif x == 7:
    result()
  elif x == 8:
    print("Thank you !!")
    break
  else:
    print("Invalid choice !!")

db.close()