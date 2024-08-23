# Task 1: Code Correction
attendee_input = int(input("Enter number of attendees: "))
venue = "large hall" if attendee_input > 100 else "conference room"
print("Use a", venue, "for your event!")

# Task 2: Venue Selection
print("Install an audio system and projector!" if attendee_input > 100 else "No need to rent other equipment!")
print("Bring in additional tables and chairs!" if attendee_input > 50 else "Don't worry about extra tables or chairs!")

# Task 3: Catering Choices
veg_input = input("Do you prefer vegetarian food for your event?(yes/no) ").lower()
caterer = "Veggie Delight Caterers" if veg_input == "yes" else "Gourmet Meals Caterers"
print(f"Hire {caterer}!")