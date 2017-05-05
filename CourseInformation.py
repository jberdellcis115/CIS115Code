
course_nums = ['CS101', 'CS102', 'CS103', 'NT110', 'CM241']
room_nums = [3004, 4501, 6755, 1244, 1411]
instructors = ['Haynes', 'Alvarado', 'Rich', 'Burke', 'Lee']
times = ['8:00 a.m.', '9:00 a.m.', '10:00 a.m.', '11:00 a.m.', '1:00 p.m.']

def main():
    num_dict = number_dictionary()
    inst_dict = instructor_dictionary()
    time_dict = time_dictionary()
    look_up = input('Enter course number for information: ')
    print()
    print('Room number: ', num_dict[look_up])
    print('Instructor: ', inst_dict[look_up])
    print('Meet time: ', time_dict[look_up])

def number_dictionary():
    num_dict = {}
    for i in range(len(course_nums)):
        num_dict[course_nums[i]] = room_nums[i]
    return num_dict

def instructor_dictionary():
    inst_dict = {}
    for i in range(len(course_nums)):
        inst_dict[course_nums[i]] = instructors[i]
    return inst_dict

def time_dictionary():
    time_dict = {}
    for i in range(len(course_nums)):
        time_dict[course_nums[i]] = times[i]
    return time_dict

main()