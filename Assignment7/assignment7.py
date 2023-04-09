import pyodbc
import tkinter as tk
from tkinter import ttk
import secrets
import string

conn = #something
cur = conn.cursor()
#__hr-GtD9qh8_sYSGTRqXw

class DMBS_GUI():
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("1200x700")
        self.login_window()
        s = ttk.Style()
        s.theme_use('clam')
        self.window.mainloop()
    # ----------------------Windows:-----------------------------------------
    def login_window(self):
        self.clear_window()
        self.window.title("DBMS Login Page")
        self.user_id = None

        tk.Label(self.window, text ="Yelp Database Application",font=("Helvetica",30) ).place(relx=.5, rely=.35,anchor= 'center')

        #tk.Label(self.window, text ="User ID -", ).place(relx=.35, rely=.5,anchor= 'center')
        
        username = ttk.Entry(self.window, width = 35, name="username")
        username.place(relx=.5, rely=.5,anchor= 'center')
        #username.insert(0, "__hr-GtD9qh8_sYSGTRqXw")

        ttk.Button(self.window, text ="Login", command = self.submit_account).place(relx=.5, rely=.55,anchor= 'center')
    
    def menu_window(self):
        self.clear_window()
        self.window.title("Menu")
        businessbtn = ttk.Button(self.window, text ="Search Business", command = self.search_business_window, name="search business")
        businessbtn.place(relx=.35, rely=.5,anchor= 'center', width=150)

        userbtn = ttk.Button(self.window, text ="Search User", command = self.search_user_window, name="search user")
        userbtn.place(relx=.65, rely=.5,anchor= 'center', width=150)

        reviewbtn = ttk.Button(self.window, text ="Write Review", command = self.enter_busines_id_window, name="write review button")
        reviewbtn.place(relx=.35, rely=.6,anchor= 'center', width=150)

        friendbtn = ttk.Button(self.window, text ="Make Friend", command = self.enter_friend_id_window, name="make friend button")
        friendbtn.place(relx=.65, rely=.6,anchor= 'center', width=150)
        
        self.navigation_bar(False)
    
    def enter_busines_id_window(self):
        self.clear_window()
        self.window.title("Enter Business ID")
        self.navigation_bar(True)
        window = self.get_window()

        # Create labels for business information
        business_id_label = tk.Label(window, text="Enter Business ID" , font=("Arial", 14))
        business_id_entry = ttk.Entry(window, name="business_id_entry")
        #business_id_entry.insert(0, "__qZrCESIQTMEtXTIhcXsw")

        # Pack labels and entry boxes
        business_id_label.pack(pady=5)
        business_id_entry.pack(pady=5)

        # Button to submit the review
        submit_button = ttk.Button(window, text="Search Business", command=lambda: self.submit_business_id(business_id_entry.get()), name ="submit_business_id")
        submit_button.pack()

    def enter_friend_id_window(self):
        self.clear_window()
        self.window.title("Enter Friend ID")
        self.navigation_bar(True)
        window = self.get_window()

        # Create labels for business information
        user_id_label = tk.Label(window, text="Enter User ID" , font=("Arial", 14))
        user_id_entry = ttk.Entry(window, name="user_id_entry")
        #user_id_entry.insert(0, "_0sLD4DAA6cAW1buYv6miA")

        # Pack labels and entry boxes
        user_id_label.pack(pady=5)
        user_id_entry.pack(pady=5)

        # Button to submit the review
        submit_button = ttk.Button(window, text="Search User", command=lambda: self.submit_user_id(user_id_entry.get()), name ="submit_user_id")
        submit_button.pack()

    def search_business_window(self):
        """
        1. This function allows the user to search for businesses that satisfy certain criteria.
        2. A user should be able to set the following filters as their search criteria: minimum and
        maximum number of stars, city, and name (or a part of the name). The search is not case-
        sensitive. It means that the search for upper or lower case must return the same results.
        3. After the search is complete, a list of search results must be shown to the user. The list
        must include the following information for each business: id, name, address, city and
        number of stars. The results must be ordered by name. The results can be shown on the
        terminal or in a GUI.
        4. If the search result is empty, an appropriate message should be shown to the user.
        """
        self.clear_window()
        self.window.title("Search Business")
        self.navigation_bar(True)

        options_frame = tk.Frame(self.window, name = "business options")

        minLabel = ttk.Label(options_frame, text ="Min Stars:", )
        maxLabel = ttk.Label(options_frame, text ="Max Stars:", )
        cityLabel = ttk.Label(options_frame, text ="City:", )
        nameLabel = ttk.Label(options_frame, text ="Name:", )

        minStars = ttk.Entry(options_frame, width = 5,name="min stars")
        maxStars = ttk.Entry(options_frame, width = 5, name ="max stars")
        city = ttk.Entry(options_frame, width = 30, name="city")
        name = ttk.Entry(options_frame, width = 30,name="business name")

        minLabel.pack(padx=5,pady=5,side='left')
        minStars.pack(padx=5,pady=5,side='left')
        maxLabel.pack(padx=5,pady=5,side='left')
        maxStars.pack(padx=5,pady=5,side='left')
        cityLabel.pack(padx=5,pady=5,side='left')
        city.pack(padx=5,pady=5,side='left')
        nameLabel.pack(padx=5,pady=5,side='left')
        name.pack(padx=5,pady=5,side='left')

        searchbtn = ttk.Button(options_frame, text ="Search", command = self.search_business)
        searchbtn.pack(padx=5,pady=5,side='left')
        
        options_frame.pack(side='top', anchor='nw')

        errorLabel = tk.Label(self.window, text ="", name="business_error")
        errorLabel.pack()

        self.create_business_tree()
    
    def search_user_window(self):
        """
        5. This function allows the user to search for users that satisfy certain criteria.
        6. A user should be able to set the following filters as their search criteria: name (or a part of
        the name), useful (yes/no), funny (yes/no) and cool (yes/no). The search is not case-
        sensitive. The user is considered useful, funny or cool if has value greater than zero for the
        corresponding attribute.
        7. After the search is complete, a list of search results must be shown to the user. The list
        must include the following information for each user: id, name, useful (yes/no), funny
        (yes/no), cool (yes/no) and the date when the user was registered at Yelp. The results must
        be ordered by name. The results can be shown on the terminal or in a GUI.
        8. If the search result is empty, an appropriate message should be shown to the user.
        """
        self.clear_window()
        self.window.title("Search User")
        self.navigation_bar(True)

        options_frame = tk.Frame(self.window, name="user options")
        
        # Create a list of options for the dropdown menu
        select = ["","", "Yes", "No"]

        # Create a variable to store the selected option
        useful = tk.StringVar(options_frame)
        funny = tk.StringVar(options_frame)
        cool = tk.StringVar(options_frame)
        useful.set(select[0])  # set the default value
        funny.set(select[0])  # set the default value
        cool.set(select[0])  # set the default value

        # Create the dropdown menu
        useful_dropdown = ttk.OptionMenu(options_frame, useful, *select)
        funny_dropdown = ttk.OptionMenu(options_frame, funny, *select)
        cool_dropdown = ttk.OptionMenu(options_frame, cool, *select)

        useful_label = ttk.Label(options_frame, text="Useful:")
        funny_label = ttk.Label(options_frame, text="Funny:")
        cool_label = ttk.Label(options_frame, text="Cool:")

        useful_label.pack(padx=5, pady=5, side='left')
        useful_dropdown.pack(padx=5, pady=5, side='left')
        funny_label.pack(padx=5, pady=5, side='left')
        funny_dropdown.pack(padx=5, pady=5, side='left')
        cool_label.pack(padx=5, pady=5, side='left')
        cool_dropdown.pack(padx=5, pady=5, side='left')

        options = [useful, funny, cool]

        namelabel = ttk.Label(options_frame, text ="Name:", )
        namelabel.pack(padx=5,pady=5,side='left')
        userName = ttk.Entry(options_frame, width = 35, name="user name")
        userName.pack(padx=5,pady=5,side='left')
        
        searchbtn = ttk.Button(options_frame, text ="Search", command = lambda: self.search_user(options))
        searchbtn.pack(padx=5,pady=5,side='left')
        options_frame.pack(side='top', anchor='nw')

        errorLabel = tk.Label(self.window, text ="", name="user_error")
        errorLabel.pack()

        self.create_user_tree()
    
    def friendship_window(self, info):
        """
        1. A user must be able to select another user from the results of the function Search Users and
        create a friendship. This can be done by entering the user’s ID in a terminal or by clicking
        on a user in a GUI. The selected user will be a friend of the user that is logged in the
        interface.
        2. The friendship should be recorded in the Friendship table.
        """
        self.clear_window()
        self.window.title("Add friend")
        self.navigation_bar(True)
        user_id, name, useful, funny, cool, date= info
        window = self.get_window()

        # Name label
        name_label = tk.Label(self.window, text=name, font=('Arial', 14))
        name_label.pack(pady=5)

        # User ID label
        user_id_label = tk.Label(self.window, text=f"User ID: {user_id}")
        user_id_label.pack(pady=5)

        # Cool, funny, and helpful labels
        stats_frame = tk.Frame(self.window)
        cool_label = tk.Label(stats_frame, text=f"Cool: {cool}")
        funny_label = tk.Label(stats_frame, text=f"Funny: {funny}")
        useful_label = tk.Label(stats_frame, text=f"Useful: {useful}")

        cool_label.pack(side=tk.LEFT)
        funny_label.pack(side=tk.LEFT)
        useful_label.pack(side=tk.LEFT)
        stats_frame.pack()

        # Date label
        date_label = tk.Label(self.window, text=f"Yelping Since: {date}")
        date_label.pack(pady=5)

        if self.check_if_friend(user_id):
            friendbtn = ttk.Button(window, text ="Add Friend", command = lambda: self.on_add_friend(user_id), name="add_friend")
            friendbtn.pack(padx=5,pady=5)
            window.children['add_friend'].configure(text="Friend Added", state="disabled")
        else:
            friendbtn = ttk.Button(window, text ="Add Friend", command = lambda: self.on_add_friend(user_id), name="add_friend")
            friendbtn.pack(padx=5,pady=5)
    
    def write_review_window(self, info):
        """
        1. A user should be able to write a review of a business.
        2. To write a review, a user must enter the business’s ID in a terminal or by clicking on a  
            business in a GUI in Search Business.
        3. The user must provide the number of stars (integer between 1 and 5).
        4. The review should be recorded in the Review table. Consider the ID of the logged user and
            the current date.
        5. The program should update the number of stars and the count of reviews for the business.
            You need to make sure that the triggers you implemented in assignment 4 are working
            properly with your application program.
        """
        self.clear_window()
        self.window.title("Write Review")
        self.navigation_bar(True)
        business_id, name, address, city, stars = info
        window = self.get_window()

        # Create labels for business information
        name_label = tk.Label(window, text= name, font=("Arial", 14))
        business_id_label = tk.Label(window, text="Business ID: " + business_id)
        address_label = tk.Label(window, text="Address: " + address)
        city_label = tk.Label(window, text="City: " + city)
        stars_label = tk.Label(window, text="Average stars: " + str(stars), name="average_stars_label")
        
        # Get review count
        query = f"SELECT COUNT(*) FROM dbo.review WHERE business_id LIKE ?"
        params = (business_id)
        cur.execute(query, params)
        row = cur.fetchone()
        review_count = row[0]
        review_label = tk.Label(window, text="Review Count: "+ str(review_count), name="review_count")

        # Create label and entry box for number of stars
        num_stars_label = tk.Label(window, text="Enter number of stars (1-5): ")
        num_stars_entry = ttk.Entry(window, name="num_stars_entry")

        # Pack labels and entry boxes
        name_label.pack(pady=5)
        business_id_label.pack(pady=5)
        address_label.pack(pady=5)
        city_label.pack(pady=5)
        stars_label.pack(pady=5)
        review_label.pack(pady=5)
        num_stars_label.pack(pady=5)
        num_stars_entry.pack(pady=5)

        # Button to submit the review
        submit_button = ttk.Button(window, text="Submit Review", command=lambda: self.submit_review(business_id, num_stars_entry.get()), name ="submit_review_button")
        submit_button.pack()

    def navigation_bar(self, include_menu):
        button_frame = tk.Frame(self.window)
        loginbtn = ttk.Button(button_frame, text ="Log Out", command = self.login_window, name ="log out")
        loginbtn.pack(padx=5,pady=5,side='right')

        if include_menu:
            menunbtn = ttk.Button(button_frame, text ="Menu", command = self.menu_window, name ="menu")
            menunbtn.pack(padx=5,pady=5,side='right')
        button_frame.pack(side='top', anchor='ne')
    
    # -----------------------------Commands On Button Click---------------------------------------------
    def submit_account(self):
        """
        Command for submitting username in login window
        """
        user_id = self.window.children['username'].get()
        # print(f"The name entered by you is {user_id}")
        if self.validate_user(user_id):
            self.user_id = user_id # for later use
            self.menu_window()
        else:
            # print(f"The user_id is incorrect")
            lblsecrow = ttk.Label(self.window, text ="Please enter a valid User ID.")
            lblsecrow.place(relx=.5, rely=.6,anchor= 'center')
    
    def submit_business_id(self, business_id):
        if self.validate_business_id(business_id):
            query = f"SELECT business_id, name, address, city, stars FROM dbo.business WHERE business_id LIKE ?"
            cur.execute(query, (business_id))
            fetched = cur.fetchone()
            item_values = fetched
            self.write_review_window(item_values)
        else:
            # print(f"The user_id is incorrect")
            lblsecrow = ttk.Label(self.window, text ="Please enter a valid Business ID.")
            lblsecrow.place(relx=.5, rely=.6,anchor= 'center')
    
    def submit_user_id(self, user_id):
        if self.validate_user(user_id):
            #print(user_id, self.user_id, user_id== self.user_id)
            if user_id == self.user_id:
                # print(f"The user_id is incorrect")
                lblsecrow = ttk.Label(self.window, text ="This is your own User ID.")
                lblsecrow.place(relx=.5, rely=.6,anchor= 'center')
                return
            query = f"SELECT user_id, name, useful, funny, cool, yelping_since FROM dbo.user_yelp WHERE user_id LIKE ?"
            cur.execute(query, (user_id))
            fetched = cur.fetchone()
            item_values = fetched
            self.friendship_window(item_values)
        else:
            # print(f"The user_id is incorrect")
            lblsecrow = ttk.Label(self.window, text ="Please enter a valid User ID.")
            lblsecrow.place(relx=.5, rely=.6,anchor= 'center')

    def search_business(self):
        """
        Command for searching for a business given the parameters chosen
        """
        window = self.get_window()
        options = window.nametowidget("business options")
        minstars = options.children['min stars'].get()
        maxstars =  options.children['max stars'].get()
        city =  options.children['city'].get()
        name =  options.children['business name'].get()
        tree = window.nametowidget("business_tree_box").children['business_tree']
        errorLabel = window.children['business_error']
        errorLabel.config(text="", fg='red')

        self.clear_tree(tree)
            
        def isfloat(element):
            try:
                float(element)
            except ValueError:
                return False 
            return True

        if ((minstars and (not isfloat(minstars) or float(minstars) < 1 or float(minstars) > 5))\
        or  (maxstars and (not isfloat(maxstars) or float(maxstars) < 1 or float(maxstars) > 5))):
            # print("Stars must be a decimal number.")
            errorLabel.config(text="Stars must be a number (1-5).", fg='red')
            return 
        
        # Initialize variables
        params = []
        where_clauses = []

        # Build WHERE clauses for the SQL query
        if minstars:
            where_clauses.append(f"stars >= {minstars}")
        if maxstars:
            where_clauses.append(f"stars <= {maxstars}")
        if city:
            city_sanitized = self.sanitize_input(city)
            params.append(city_sanitized)
            where_clauses.append("city LIKE ?")
        if name:
            name_sanitized = self.sanitize_input(name)
            params.append(f"%{name_sanitized}%")
            where_clauses.append("name LIKE ?")

        # Combine the WHERE clauses with "AND"
        if where_clauses:
            search_string = "WHERE " + " AND ".join(where_clauses)
        else:
            search_string = ""

        # Construct and execute the SQL query
        query = f"SELECT business_id, name, address, city, stars FROM dbo.business {search_string} ORDER BY name"
        cur.execute(query, tuple(params))
        fetched = cur.fetchall()

        if not fetched:
            # print("No businesses match the search description.")
            self.clear_tree(tree)
            errorLabel.config(text="No businesses match the search description.", fg='red')
            return
        
        self.inset_into_tree(tree, fetched)
        tree.bind("<<TreeviewSelect>>", self.on_select_business)
        tree.pack(padx=5,pady=5,fill="x")

    def search_user(self, variables):
        """
        Command for searching for a user
        """
        window = self.get_window()
        options = window.nametowidget('user options')
        name = options.children['user name'].get()
        useful, funny, cool = [v.get() for v in variables]
        tree = window.nametowidget('user_tree_box').children['user_tree']
        errorLabel = window.children['user_error']
        errorLabel.config(text="", fg='red')
        self.clear_tree(tree)

        def search_string_append(search_string, variable, option):
            if variable == "Yes":
                search_string += f"{option} > 0"
            elif variable == "No":
                search_string += f"{option} = 0"
            else:
                search_string += f"{option} >= 0"
            return search_string

        params = [self.user_id]
        search_string = f"WHERE user_id <> ? AND "
        search_string = search_string_append(search_string, useful, 'useful')
        search_string += " AND "
        search_string = search_string_append(search_string, funny, 'funny')
        search_string += " AND "
        search_string = search_string_append(search_string, cool, 'cool')
        
        if search_string and name: search_string += " AND "
        
        if name: 
            search_string += f"name LIKE ?"
            params.append('%'+self.sanitize_input(name)+'%')

        query = f"SELECT user_id, name, useful, funny, cool, yelping_since FROM dbo.user_yelp {search_string} ORDER BY name"
        # print(query, tuple(params))
        cur.execute(query, params)
        fetched = cur.fetchall()
        
        if not fetched:
            # print("No users match the search description.")
            errorLabel.config(text="No users match the search description.", fg='red')
            return
            
        #print(fetched)
        self.inset_into_tree(tree, fetched)
        tree.bind("<<TreeviewSelect>>", self.on_select_user)
        tree.pack(padx=5,pady=5,fill="x")

    def on_select_business(self,event):
        """
        Command for clicking on a business in the business search window, will lead to write review window
        """
        # Get the selected item's ID
        item_id = event.widget.focus()
        # Get the values of the selected item's columns
        item_values = event.widget.item(item_id)['values']
        self.write_review_window(item_values)

        # Do something with the selected item's values
        # print(item_values)
    
    def submit_review(self, business_id, stars):
        """
        Command for submitting the business review
        """    
        window = self.get_window()  
        submit_button = window.children['submit_review_button']
        submit_button.config(state="disabled")
        num_stars_entry = window.children['num_stars_entry']
        stars_label = window.children['average_stars_label']
        review_label = window.children['review_count']
        num_stars_entry.delete(0, 'end')  # Clear the entry box

        if self.valid_stars(stars):
            valid_key = False
            while not valid_key:
                key = self.generate_key()
                query = f"SELECT * FROM dbo.review WHERE review_id LIKE ?"
                params = (key)
                cur.execute(query,params)
                row = cur.fetchone ()
                valid_key = True if not row else False
            
            query = f"INSERT INTO dbo.review (review_id, user_id, business_id, stars, date, useful, funny, cool) VALUES (?,?,?,?,GETDATE(),0,0,0) "
            params =(key,self.user_id,business_id, stars)
            # print(query, params)
            cur.execute(query, params)
            conn.commit()

            # Update stars:
            query = f"SELECT stars FROM dbo.business WHERE business_id LIKE ?"
            params = (business_id)
            cur.execute(query, params)
            row = cur.fetchone()
            new_stars = row[0]

            stars_label.config(text="New average stars: " + str(new_stars))
            review = tk.Label(window, text="Review Submitted.")
            review.pack(pady=10)

            #Update review count:
            query = f"SELECT COUNT(*) FROM dbo.review WHERE business_id LIKE ?"
            params = (business_id)
            cur.execute(query, params)
            row = cur.fetchone()
            review_count = row[0]
            review_label.config(text="New review count: " + str(review_count))

        else:
            review = tk.Label(window, text="Invalid number of stars.",fg="red")
            review.pack(pady=10)
            # print("invalid stars")
        # Destroy label after 1 second    
        window.after(1000, review.destroy)    
        # Schedule a function to enable the button after 1 second
        window.after(1000, submit_button.config, {"state": "normal"})  
    
    def on_select_user(self,event):
        """
        Command for clicking on a user in the user search window, will lead to add friend window
        """
        # Get the selected item's ID
        item_id = event.widget.focus()
        # Get the values of the selected item's columns
        item_values = event.widget.item(item_id)['values']
        self.friendship_window(item_values)
        #print(item_values)

    def on_add_friend(self, friend_id):
        """
        Command for adding a friend
        """
        window = self.get_window()
        query = f"INSERT INTO dbo.friendship VALUES (?, ?)"
        params = (self.user_id, friend_id)
        cur.execute(query, params)
        conn.commit()
        window.children['add_friend'].configure(text="Friend Added", state="disabled")


    #------------------------Helper Functions-----------------------------------------------------------
    def generate_key(self):
        alphabet = string.ascii_letters + string.digits
        random_string = ''.join(secrets.choice(alphabet) for i in range(22))
        return random_string

    def check_if_friend(self, friend):
        query = f"SELECT user_id, friend FROM dbo.friendship WHERE friend LIKE ? AND user_id LIKE ?"
        params = (friend, self.user_id)
        cur.execute(query, params)
        fetched = cur.fetchall()
        return True if fetched else False

    def sanitize_input(self, input_string):
        # Remove leading/trailing white spaces
        input_string = input_string.strip()

        # Replace special characters with escape sequences
        input_string = input_string.replace("%", "\%")  # Escape percent sign

        return input_string

    def validate_business_id(self, business_id):
        if '%' in business_id: return False
        cur.execute( f"SELECT business_id FROM dbo.business WHERE business_id LIKE ?", (business_id) )
        row = cur.fetchone ()
        return True if row else False

    def validate_user(self, user_id):
        if '%' in user_id: return False
        cur.execute( f"SELECT user_id FROM dbo.user_yelp WHERE user_id LIKE ?", (user_id))
        row = cur.fetchone ()
        return True if row else False

    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def clear_tree(self, tree):
        for item in tree.get_children():
            tree.delete(item)
        
    def create_business_tree(self):
        window = self.get_window()
        box = tk.Frame(window,name='business_tree_box')
        tree = ttk.Treeview(box, column=("c1", "c2", "c3","c4","c5"), show='headings', height=30,name='business_tree')
        # Create a vertical scrollbar and attach it to the Treeview widget
        scrollbar = ttk.Scrollbar(box, orient='vertical', command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side='right', fill='y')
        
        tree.column("# 1", anchor="center")
        tree.heading("# 1", text="Business ID")
        tree.column("# 2", anchor="center")
        tree.heading("# 2", text="Name")
        tree.column("# 3", anchor="center")
        tree.heading("# 3", text="Address")
        tree.column("# 4", anchor="center")
        tree.heading("# 4", text="City")
        tree.column("# 5", anchor="center")
        tree.heading("# 5", text="Stars")
        tree.pack(padx=5,pady=5,fill='x')
        box.pack(pady=5, fill='x')

    def create_user_tree(self):
        window = self.get_window()
        # Add a Treeview widget
        box = tk.Frame(window, name='user_tree_box')
        tree = ttk.Treeview(box, column=("c1", "c2", "c3","c4","c5","c6"), show='headings', height=30, name='user_tree')

        tree.column("# 1", anchor="center")
        tree.heading("# 1", text="User ID")
        tree.column("# 2", anchor="center")
        tree.heading("# 2", text="Name")
        tree.column("# 3", anchor="center",width=50)
        tree.heading("# 3", text="Useful")
        tree.column("# 4", anchor="center",width=50)
        tree.heading("# 4", text="Funny")
        tree.column("# 5", anchor="center",width=50)
        tree.heading("# 5", text="Cool")
        tree.column("# 6", anchor="center")
        tree.heading("# 6", text="Date Registered")

        # Create a vertical scrollbar and attach it to the Treeview widget
        scrollbar = ttk.Scrollbar(box, orient='vertical', command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(pady=5,side='right', fill='y')

        tree.pack(padx=5,pady=5, fill='x')
        box.pack(fill='x')

    def inset_into_tree(self, tree, fetched):
        # Insert the data in Treeview widget
        for i, row in enumerate(fetched):
            row[-1] = str(row[-1])
            vals = tuple(' '.join(str(elem).split()) for elem in row)
            tree.insert('', i, text=f"{i+1}", values= vals)

    def get_window(self):
        return self.window

    def valid_stars(self,stars):
        if not stars: return False
        try:
            int(stars)
        except ValueError:
            return False 
        stars = int(stars)
        if stars < 1 or stars > 5: return False
        return True
    

DMBS_GUI()
conn.close()
