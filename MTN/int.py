import mysql.connector

# Make sure the table name 'momo_users' matches exactly what is in your DB
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="MOMO"
)

cursor = conn.cursor()

def agent():
    print("""
      ---- Welcome to MTN Service Agent ----
      1. Kwandika umukiriya mushya
      2. Kubitsa
      3. Kubikuza
    """)
    
    # Fixed: added input() before int()
    try:
        hitamo = int(input("Hitamo service: "))
    except ValueError:
        print("Nyamuneka shyiramo umubare (1, 2, cyangwa 3).")
        return

    if hitamo == 1:
        print("Kwandikisha umukirya mushya...")
        # Add your registration logic here
        
    elif hitamo == 2:
        phonenumber = input("Shyiramo nimero ya telphone: ")

        
        check_query = "SELECT first_name, second_name FROM momo_users WHERE phone_number = %s"
        cursor.execute(check_query, (phonenumber,))
        user_data = cursor.fetchone()
      
        if user_data:
            first_name, second_name = user_data
            full_name = f"{first_name} {second_name}"
            print(f"Emeza: Ushaka koherereza {full_name} amafaranga.")
            
            to_send = int(input("Shyiramo amafaranga ushaka kohereza: "))
      
            update_query = "UPDATE momo_users SET balance = balance + %s WHERE phone_number = %s"
            cursor.execute(update_query, (to_send, phonenumber))
            conn.commit()
            
            print(f"Byagenze neza! Yoherereje {to_send} RWF kuri {full_name} ({phonenumber}).")
        else:
            print("Iyo nimero ntayo muri sisitemu (User not found).")
      
    elif hitamo == 3:
        print("Service yo kubikuza iri gutegurwa...")
        
    else:
        print("Wahisemo nabi. Hitamo hagati ya 1 na 3.")

# Run the function


def account():
    # 1. Get user input
    phonenumber = input("Enter your phone number: ")
    user_pin = input("Enter the Mobile Money PIN: ") # Keep as string to handle leading zeros

    # 2. Check both phone AND pin in the database query
    
    query = "SELECT first_name, second_name,balance ,PIN FROM momo_users WHERE phone_number = %s AND pin = %s"
    cursor.execute(query, (phonenumber, user_pin))
    
    user_account = cursor.fetchone()

    if user_account:
        
        first_name, second_name , user_balance ,sender_pin= user_account
        user_conv=int(user_balance)
        print(f"Welcome {first_name} {second_name}!")
        print(f"""
        ----- welcome {first_name} {second_name}--------
        1.kohereza
        2.kugura
        3.hindura pin
        4.reba balance
        
        """)
        choose=int(input("hitamo service ushaka: "))
        # koherza amafaranga
        if choose == 1:

           nimero=int(input("shyirani nimero ushaka koherereza amafaranga: "))
           check='SELECT first_name, second_name  FROM momo_users WHERE phone_number=%s'
           cursor.execute(check,(nimero,))
           user_data=cursor.fetchone()
           if user_data:
               first_name ,second_name =user_data
               amount=int(input("shyiramo umubare wamafaranga ushaka kohereza: "))
               print(f"ugiye kohereza {amount} kuri {first_name } {second_name}")
               if amount >user_conv:   
                   print("not enough money to send")
                   return
               

               sucess=False
               for i in range(3):
                  pin=int(input("shyiramo umubare wibanga wangawo: "))
                  if pin == sender_pin:
                    sucess=True
                    break
                  else:
                    print("shyiramo umubare wibanga wanyawo")
               if sucess:
                    cursor.execute('UPDATE momo_users SET balance=balance-%s WHERE phone_number=%s',(amount,phonenumber))  
                    cursor.execute('UPDATE momo_users SET balance=balance+%s WHERE phone_number=%s',(amount,nimero))
                    conn.commit()
                    print(f"wohereje {amount} kuri {nimero} amazina{first_name} {second_name} ")

            # kureba asigaye ho
               sucess=False
        elif choose ==4:
             for i in range(3):
                pin=int(input("shyiramo umubare wibanga kwemeza: "))
                if pin==sender_pin:
                    sucess=True
                    break
                else:
                    print("shyiramo umubare wibanga wanyawo")
             print(f"kuri konti yawe na MOMO ufiteho {user_balance} RWF")

        
        else:
            print("nta serevice wahisemo")
        
        
         

    else:
        
        print("Error: Invalid phone number or PIN.")
        return False

account() 