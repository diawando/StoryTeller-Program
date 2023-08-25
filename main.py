

print("Welcome to the Azubi Tech School Adventure!")
print("Let's create a story about your amazing experience at Azubi Tech School.")
name = input("Enter your name: ")
age = input("Enter your age: ")
hometown = input("Enter your hometown: ")
favorite_activity = input("Enter your favorite tech activity at Azubi Tech School: ")
memorable_moment = input("Share a memorable tech moment from your experience: ")
emotion = input("Describe how you felt during this tech adventure: ")

    

def generate_story(name, age, hometown, favorite_activity, memorable_moment, emotion):
    story_template = f"Once upon a time, in the world of tech brilliance, there lived a young prodigy named {name}. At just {age} years old, {name} hailed from the thriving town of {hometown}. Their heart would race with excitement every time they thought about their favorite tech activity at Azubi Tech School: {favorite_activity}."

    story_template += f"\n\nOne day, as the digital realm buzzed with energy, something extraordinary happened. While {name} was {favorite_activity}, they stumbled upon a hidden vault of knowledge filled with cutting-edge tech secrets. This was a moment that would forever be etched in {name}'s memory. The sparkle in their eyes and the rush of {emotion} was something words cannot fully capture."

    story_template += f"\n\nAs lines of code flowed like poetry and algorithms danced to the rhythm of innovation, {name} couldn't help but reflect on their amazing journey at Azubi Tech School. It was a place where dreams met code, where ideas sparked revolutions, and where the future unfolded one line at a time."

    story_template += f"\n\nAnd so, {name} left Azubi Tech School with a mind ablaze with knowledge and a heart filled with determination. Their tech adventures were far from over, but Azubi Tech School would forever hold a special place in their journey. The end."

    return story_template

def main():
    completed_story = generate_story(name, age, hometown, favorite_activity, memorable_moment, emotion)

    print("\nHere's your Azubi Tech School Adventure story:")
    print(completed_story)

if __name__ == "__main__":
    main()



