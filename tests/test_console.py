from models.base_model import BaseModel
from myconsole import MyConsole  # Updated import

def test_myconsole():
    # Create an instance of the MyConsole class
    console = MyConsole()

    # Create three instances of the BaseModel class
    console.onecmd("create BaseModel")
    console.onecmd("create BaseModel")
    console.onecmd("create BaseModel")

    # Create two instances of the User class
    console.onecmd("create User")
    console.onecmd("create User")

    # List all instances (BaseModel and User)
    console.onecmd("myall")

    # Count instances of BaseModel and User
    console.onecmd("mycount BaseModel")
    console.onecmd("mycount User")

    # Show details of a BaseModel instance
    console.onecmd("myshow BaseModel {}".format(console.models['MyBaseModel'][0].id))

    # Show details of another BaseModel instance
    console.onecmd("myshow BaseModel {}".format(console.models['MyBaseModel'][1].id))

    # Show details of a User instance
    console.onecmd("myshow User {}".format(console.models['MyUser'][0].id))

    # Update a property of a BaseModel instance
    console.onecmd("myupdate BaseModel {} name John".format(console.models['MyBaseModel'][0].id))

    # Update a property of a User instance
    console.onecmd("myupdate User {} first_name John".format(console.models['MyUser'][0].id))

    # Show updated details of the BaseModel instance
    console.onecmd("myshow BaseModel {}".format(console.models['MyBaseModel'][0].id))

    # Show updated details of the User instance
    console.onecmd("myshow User {}".format(console.models['MyUser'][0].id))

    # Destroy a BaseModel instance
    console.onecmd("mydestroy BaseModel {}".format(console.models['MyBaseModel'][1].id))

    # Destroy a User instance
    console.onecmd("mydestroy User {}".format(console.models['MyUser'][0].id))

    # Attempt to show the destroyed BaseModel instance (should not exist)
    console.onecmd("myshow BaseModel {}".format(console.models['MyBaseModel'][1].id))

    # Attempt to show the destroyed User instance (should not exist)
    console.onecmd("myshow User {}".format(console.models['MyUser'][0].id))

    # List all instances again (BaseModel and User)
    console.onecmd("myall")

    # Count instances of BaseModel and User again
    console.onecmd("mycount BaseModel")
    console.onecmd("mycount User")

if __name__ == "__main__":
    test_myconsole()
