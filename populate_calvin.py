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
        {"title": "Teleoperation of Baxter robot using the HTC Vive",
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

         "video": "https://youtu.be/3GzbZMFeiFI"},
        {"title": "FishyDishy Web Application",
         "url": "https://github.com/flightlesskite/fishy_dishy_project",
         "description": "Group project.",
         "video": "https://youtu.be/UeZ-_Mk48a8" },
    ]

    java_projects = [
        {"title": "Top Trumps: Command Line and Online version",
         "url": "https://github.com/flightlesskite/TopTrumps",
         "description": "",
         "video": ""},
        {"title": "Car Intersection Simulator using Threads",
         "url": "https://github.com/flightlesskite/APAE",
         "description": "",
         "video": ""},
        {"title": "Bag Data Structure Implementation",
         "url": "https://github.com/flightlesskite/ADS",
         "description": "",
         "video": ""},
        {"title": "Cypher encyrpter and decrypter",
         "url": "https://github.com/flightlesskite/ProgAE2",
         "description": "",
         "video": ""},
        {"title": "Gym booking system with SQL database",
         "url": "https://github.com/flightlesskite/GymBookingJDBC",
         "description": "",
         "video": ""}
    ]

    other_projects = [
        {"title": "Teleoperation of Baxter robot using the HTC Vive",
         "url": "https://youtu.be/3GzbZMFeiFI",
         "description": "",
         "video":""},
        {"title": "FishyDishy Web Application",
         "url": "https://youtu.be/UeZ-_Mk48a8",
         "description": "",
         "video":""}
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
            add_page(c, p["title"], p["url"], p["description"], p["video"])

    #Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, description, video):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.description=description
    p.video=video
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