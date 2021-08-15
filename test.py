from data import data

def test_forloop():
    for i in range(10):
        print(i)


def print_titles():
    """

    method to learn for loops in python
    1 - import data
    2 - for loop for data list
    3 - print the object
    """
    for prod in data:
        print(prod["title"])

def print_sum():
    """
    Method to print the sum of catalog prices
    """

    sum = 0
    for item in data:
        sum += item["price"]

    print(f"The sum is: {sum}") 

def print_test2(limit): # can use paramaters
    """
    Method to price the title whose price is greater than 10 
    """  
    for item in data:
        if(item["price"] > limit):
            print(f"{item['title']} - ${item['price']}") #can be double or single quote marks   

def print_total_value():
    """
    method to print the total stock value
    """
    sum = 0.0
    for item in data:
        sum += (item['price'] * item['stock'])

    print(f"total stock value = {sum}")

def print_categories_list():
    """
    method to get and print the list of unique categories
    a - create a results list
    1 - travel the list
    2 - get the category
    3 - if the category is not in a results list, push it
    """

    categories = []
    for item in data:
        cat = item["category"]

        if cat not in categories:
            categories.append(cat)

    print(categories) # print the list





def run_test():
    print("Running tests")

    #test_forloop()
   # print_titles()
   # print_sum()
   # print_test2(10) #tests greater than 10 #dollars
   # print_test2(20) #tests greater than 20 dollars

   # print_total_value() # print the total stock value sum (price * stock)

    print_categories_list() #print a list with the #unique categories

run_test()