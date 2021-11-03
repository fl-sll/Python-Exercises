dict = {
    "Python": "It is an interpreted high-level general-purpose programming language.",
    "Javascript": "It has dynamic typing, prototype-based object-orientation and first-class functions.",
    "Java": "It is a high-level, class-based, object-oriented programming language",
    "C++": "It is a general-purpose programming language created by Bjarne Stroustrup as an extension of the C programming language.",
    "PHP": "It is a general-purpose scripting language geared towards web development."
}

for key in ["Java", "Javascript", "C++", "Python",  "PHP"]:
    print(key, "\n", dict.get(key), "\n", sep="",)