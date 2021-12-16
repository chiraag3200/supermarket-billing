# Project Goal

To create REST APIS for a supermarket application. It is a self-service store offering a wide variety of food, beverages and household
products, organised into various categories.
The categories can have subcategories. Subcategories have items under them. Items can be sold by Units. Every item has a price for which it can be sold.

# Tasks Completed

- GET API's to search the items using various filters like category, subcategory and name of the items.
- POST API's to create new categories, subcategories and items.
- PATCH API's to update categories, subcategories and items.
  
 # How To Run the Project
 
Run `sudo docker-compose up` for dev server.

Navigate to `http://localhost:8000/admin`.

Superuser Credentials:

username : admin

password : admin#123

# How To Test the Project
GET API End Point : http://localhost:8000/api/items

Search API End Points : http://localhost:8000/api/items/?category=food&subcategory=fruit&name=apple

                      : http://localhost:8000/api/items/?category=food&subcategory=fruit

                      : http://localhost:8000/api/items/?category=food&name=apple
                      
                      : http://localhost:8000/api/items/?subcategory=fruit&name=apple
                      
                      : http://localhost:8000/api/items/?name=apple
                      
                      : http://localhost:8000/api/items/?category=food
                      
                      : http://localhost:8000/api/items/?subcategory=fruit


POST API End Points : http://localhost:8000/api/items/
                    
                    : http://localhost:8000/api/subcategory/
                    
                    : http://localhost:8000/api/category/ 

PATCH API End Points : http://localhost:8000/api/items/primaryKey/
                    
                     : http://localhost:8000/api/subcategory/primaryKey/
                    
                     : http://localhost:8000/api/category/primaryKey/
