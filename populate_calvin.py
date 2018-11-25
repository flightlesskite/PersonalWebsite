import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'calvin_webpage.settings')

import django
django.setup()

from calvin.models import Category, Page

def populate():
    # First, create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then create a dictionary of dictionaries for categories.
    # May be confusing but allows us to iterate through
    # each data structure, and add the data to the models.

    python_projects = [
        {"title": "Teleoperation of Baxter Robot using the HTC Vive",
         "url": "https://github.com/flightlesskite/vive_teleoperation",
         "description": "A Masters Research Project involving the implementation of a VR "
                        "interface for the teleoperation of a Baxter robot on a single Linux "
                        "System. Movements of a user was tracked as a set of cartesian "
                        "co-ordinates using the HTC Vive HMD and controllers through the use "
                        "of the OpenVR API. These co-ordinates would then be subsequently translated "
                        "into ROS co-ordinate system and used to map to Baxter's limbs. "
                        "Finally, the implementation of a stereocamera was achieved "
                        "through using Unity (C#) to render video streaming on "
                        "the individual eyes of the user.",

         "video": "https://youtu.be/3GzbZMFeiFI",
         "file": ""},
        {"title": "FishyDishy Web Application",
         "url": "https://github.com/flightlesskite/fishy_dishy_project",
         "description": "A Group Project utilizing the Python and the Django framework to build "
                        "a web application for sharing fish recipes amongst a community of "
                        "different users.  Users are able to create a profile, save receipes "
                        "search for receipes, write reviews and identify nearby fishmongers. "
                        "Responsible for both front & back-end development – "
                        "implementing the Fish Map feature using Google Maps API, "
                        "connecting with database through Python Models, "
                        "creating Python Views to serve data rendered by templates "
                        "and testing the several functions of the web application.",
         "video": "https://youtu.be/UeZ-_Mk48a8",
         "file":""},
    ]

    java_projects = [
        {"title": "Top Trumps: Command Line and Online version",
         "url": "https://github.com/flightlesskite/TopTrumps",
         "description": "A Group Project utilizing Java to build a command line version "
                        "and online web application of the Top Trumps game.  "
                        "Responsible for creating the GameManager class used to control "
                        "flow/logic of game, designing the user interface for the "
                        "online version (using Javascript, CSS and HTML) and"
                        "implementing the RESTAPI methods used to "
                        "connect front-end with back-end.",
         "video": "",
         "file": ""},
        {"title": "Car Intersection Simulator using Threads",
         "url": "https://github.com/flightlesskite/APAE",
         "description": "An assessed Java exercise from my Advanced Programming "
                        "module which uses Threads and Locks to create a traffic "
                        "intersection simulation.  The cars cannot occupy the same "
                        "space at any given moment and can move in a straight line - "
                        "either left to right or up and down (& vice versa).",
         "video": "",
         "file": ""},
        {"title": "Bag Data Structure Implementation",
         "url": "https://github.com/flightlesskite/ADS",
         "description": "An assessed Java exercise from my Algorithms and Data "
                        "Structures module which utilises a BST to implement a "
                        "Bag Interface - a collection that is similar to a Set, "
                        "except that allows for multiple copies of the same element. "
                        "This specific implementation requires the use of lazy deletion.",
         "video": "",
         "file": ""},
        {"title": "Cypher Encyrpter and Decrypter",
         "url": "https://github.com/flightlesskite/ProgAE2",
         "description": "An assessed Java exercise from my Core Programming module "
                        "which uses a keyword to process either a Mono or Vigenere "
                        "cipher on a txt file to encrypt and decrypt its content.",
         "video": "",
         "file": ""},
        {"title": "Gym Booking System with SQL Database",
         "url": "https://github.com/flightlesskite/GymBookingJDBC",
         "description": "An assessed Java exercise from my Database module "
                        "which uses the JDBC API to connect to the University's"
                        "PostgreSQL database for a Gym Booking system that allows "
                        "users to be book a class or facility with double bookings "
                        "accounted for.  In addition to this, queries of the current "
                        "bookings can be returned and displayed on the GUI.",
         "video": "",
         "file": ""}
    ]

    other_projects = [
        {"title": "Cyber Security Policy Report",
         "url": "",
         "description": "A report highlighting the risks of Cloud Computing "
                        "in a professional setting and the Cyber Security Policy "
                        "proposal used to address any threats that may be faced "
                        "in adopting such a system.",
         "video": "",
         "file": "https://www.scribd.com/document/393880770/ECS-Report?secret_password=8Z8ahyPDd6jqtXP05bFT"},
        {"title": "Interface Experiment Car Infotainment System",
         "url": "",
         "description": "A report evaluating user tests comparing the traditional "
                        "touch controls in car infotainment system to a possible "
                        "interface controlled using voice control.  A paper prototype "
                        "was initially conceived to design the two systems to compare "
                        "the two setups.  The user evaluations utilised powerpoint to "
                        "simulate interactions with the two different versions of "
                        "the infotainment system.",
         "video":"https://youtu.be/-a3Lq6GeauU",
         "file":"https://www.scribd.com/document/393880820/HCI-Report?secret_password=BXODP83Cvb2AFHFIs4tz"},
        {"title": "Masters Software Development Dissertation",
         "url": "",
         "description": "Masters Disseration researching VR interfacing for teleoperation systems "
                "- the challenges faced in implementing such a system using the HTC Vive and "
                        "Baxter robot on a single Linux Computer.",
         "video": "",
         "file": "https://www.scribd.com/document/393881104/Software-Development-MSC?secret_password=2XoSiZk49xEslEzTprue"},
        {"title": "UG Marketing Dissertation",
         "url": "",
         "description": "Marketing dissertation discussing the diffusion and"
                "subsequent commercialisation of new, innovative technologies "
                "and how to achieve market acceptance:  Case study of the Nintendo "
                        "Switch console.",
         "video": "",
         "file": "https://www.scribd.com/document/393881351/Marketing-BA?secret_password=Zt0OAy2CCRcEJw4IuOlY"},
    ]

    cats = {"Python Projects": {"pages": python_projects,
                                "image":"static/images/pythonlogo.png"},
            "Java Projects": {"pages": java_projects,
                              "image":"static/images/javalogo.png"},
            "Other Projects": {"pages": other_projects,
                               "image":"static/images/otherlogo.png"} }

    # Add additional categories or pages to the dictionaries above
    # The code below goes through the cats dictionary, the adds each category,
    # and then adds all the associated pages for that category.

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data["image"])
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"], p["description"], p["video"],
                     p["file"])

    #Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, description, video, file):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.description=description
    p.video=video
    p.file=file
    p.save()
    return p

def add_cat(name, image):
    c= Category.objects.get_or_create(name=name)[0]
    c.image=image
    c.save()
    return c

# Start execution here!
#  Only executes when module is run as a standalone Python script.
# Importing the module will not run the code! But can access class/functions
if __name__ == '__main__':
    print("Starting population script...")
    populate()