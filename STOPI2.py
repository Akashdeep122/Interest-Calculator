
import sqlite3

def view():
    conn = sqlite3.connect("warnings.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM warns")
    rows = cur.fetchall()
    conn.close()
    return rows
def delete(name):
    conn = sqlite3.connect("warnings.db")
    cur = conn.cursor()
    cur.execute(f"DELETE FROM warns WHERE name=?",(name,))
    conn.commit()
    conn.close()

def update(name,amount,interest,final):
    conn = sqlite3.connect("warnings.db")
    cur = conn.cursor()
    cur.execute(f"UPDATE warns SET amount={amount},interest={interest},final={final} WHERE name={name}")
    conn.commit()
    conn.close()

def Ask():
  a = input("Hey its The Database manager, you can use Commands like view,delete here, you can mess up with uppercase and lowercase :)")
  if a == "view":
    
    val = view()
    if val == []:
        print("There are no values in the database")
        Ask()
    print("Name , Amount , Interest , Final Value")
    for x in val:
      x=str(x).replace("(","")
      x=x.replace(")"," ")
      print(x)
    Ask()
  if a == "delete":
    val = view()
    if val == []:
        print("There are no values in the database")
        Ask()
    for x in val:
      x=str(x).replace("(","")
      x=x.replace(")","")
      print(x,"/n")
    try:
      a = int(input("Whose name Would you Like to Delete in These Keys, write the number"))
    except:
        print("Please write the number of which entry you want to be deleted")
        Ask()
    a=a-1
    try:
      delete(val[a][0])
      print("Successfully Deleted The Value")
      Ask()
    except:
        print("The value doesnt exist")
        Ask()
  else:
    print("Please write it correctly")
    Ask()


Ask()
    
    
    
    
