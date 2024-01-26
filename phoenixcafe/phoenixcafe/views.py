# NEW - standard library imports go on top
import datetime    # NEW
import random
from django.utils import timezone

# imports from Django
from django.shortcuts import render
from django.http import HttpResponse

# This view will return "Welcome to the Phoenix Cafe!" as text
def welcome(request):
    return HttpResponse("Welcome to the Phoenix Cafe!")

def sleepy(request):
    return HttpResponse("Z-z-z-z-z-z-z!")

def rand(request):
    random_number = random.randint(1, 100)  # Change the range as needed
    return HttpResponse(f"Random number: {random_number}")

def greetings(request):
    current_hour = timezone.now().hour

    if 6 <= current_hour < 12:
        greeting_message = "Good morning!"
    elif 12 <= current_hour < 18:
        greeting_message = "Good afternoon!"
    else:
        greeting_message = "Good night!"

    return HttpResponse(greeting_message)

def cake(request):
    # You can replace this with an actual cake recipe
    cake_recipe = """
    Ingredients:
    - 2 cups all-purpose flour
    - 1 3/4 cups granulated sugar
    - 3/4 cup unsweetened cocoa powder
    - 1 1/2 teaspoons baking powder
    - 1 1/2 teaspoons baking soda
    - 1 teaspoon salt
    - 2 large eggs
    - 1 cup whole milk
    - 1/2 cup vegetable oil
    - 2 teaspoons vanilla extract
    - 1 cup boiling water

    Instructions:
    1. Preheat oven to 350°F (175°C). Grease and flour two 9-inch round cake pans.
    2. In a large bowl, sift together flour, sugar, cocoa powder, baking powder, baking soda, and salt.
    3. Add eggs, milk, oil, and vanilla extract. Beat on medium speed for 2 minutes.
    4. Stir in boiling water until well combined (batter will be thin).
    5. Pour batter evenly into prepared pans.
    6. Bake for 30 to 35 minutes, or until a toothpick inserted into the center comes out clean.
    7. Allow cakes to cool in pans for 10 minutes, then transfer to a wire rack to cool completely.
    8. Frost and decorate as desired.

    Enjoy your delicious cake!
    """
    return HttpResponse(cake_recipe)



# your custom code will be here


# NEW - new view that returns the current date and time
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)  # we are not returning a static string

