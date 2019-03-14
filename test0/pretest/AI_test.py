def main():
    f = open("fred.csv", 'r')

    lines = f.read().split('\n')

    for each in lines:
        elements = each.split(',')
        club_name = elements[0]
        people = elements[1:len(elements)].remove('')

        print(people)
        
main()
