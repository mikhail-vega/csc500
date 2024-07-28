def create_get_class():
    """
    Prompts user to create a class or get class information
    """

    # dictionaries to store class information
    course_room = {}
    course_instructor = {}
    course_meeting_time = {}

    def create_class(course_number: str, room_number: int, instructor: str, meeting_time: str):
        """
        Helper function to update the various dictionaries for class information

        Parameters
        ----------
        course_number: str
        room_number: int
        instructor: str
        meeting_time: str
        """
        course_room[course_number] = room_number
        course_instructor[course_number] = instructor
        course_meeting_time[course_number] = meeting_time

        return

    while True:
        try:
            print("Please select an option: ")
            print("1 to create/update a class")
            print("2 to get class information")
            print("3 to exit")
            selection = int(input("Choose an option: "))
        except ValueError:
            print("Incorrect input - please input a valid response")
        else:
            match selection:
                case 1:
                    try:
                        course = str(input("Please input course number: "))
                        course = course.upper()
                        if course in course_room:
                            while True:
                                update = str(input("Course already exists, update? 'Y' for yes, 'N' for no: "))
                                if update in ["Y", "y"]:
                                    continue
                                elif update in ["N", "n"]:
                                    break
                                else:
                                    print("Please input a valid selction")
                    except ValueError:
                        print("Please input a valid string")
                    try:
                        room_number = int(input("Please input room number: "))
                    except ValueError:
                        print("Please input a valid number")
                    try:
                        instructor = str(input("Please input the instructors name: "))
                    except ValueError:
                        print("Please input a valid string")
                    try:
                        meeting_time = str(input("Please input meeting time: "))
                    except ValueError:
                        print("Please input a valid time")
                    
                    create_class(course, room_number, instructor, meeting_time)
                    
                    print()
                case 2:
                    try:
                        course = str(input("Please input course number: "))
                        course = course.upper()

                        if course in course_room:
                            print(f"Course Number: {course}, Room Number: {course_room[course]}, Instructor: {course_instructor[course]}, Meeting Time: {course_meeting_time[course]}")
                        else:
                            print("Course number not found.")

                        print()
                    except ValueError:
                        print("Please input a valid string")
                case 3:
                    break
                case _:
                    print("Please input a valid selction\n")


    return

create_get_class()