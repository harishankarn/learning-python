import time

def sum_of_vehicles(a,b,c,d):
    # lane1 situation
    if a > b and a > c and a > d:
        if a < 10:
            a=0
        else:
            a-=6

        b += 3
        c += 3
        d += 3

    # lane2 situation
    elif b > a and b > c and b > d:
        if b < 10:
            b = 0
        else:
            b -= 6

        a += 3
        c += 3
        d += 3

    # lane3 situation
    elif c > a and c > b and c > d:

        if c < 10:
            c = 0
        else:
            c -= 6

        b += 3
        d += 3
        a += 3

    # lane4 situation
    elif d > a and d > b and d > c:
        if d < 10:
            d = 0
        else:
            d -= 6

        b += 3
        c += 3
        a += 3

    # equality situation
    elif a==b or a==c or a==d or b==c or b==d or c==d:
        if a==b or a==c or a==d:
            if a < 10:
                a=0
            else:
                a-=6

            b += 3
            c += 5
            d += 7

        elif b==c or b==d:
            if b < 10:
                b = 0
            else:
                b -= 6

            a += 3
            c += 5
            d += 7

        elif c==d:
            if c < 10:
                c = 0
            else:
                c -= 6

            b += 3
            d += 5
            a += 7

    return a, b, c, d

def first_lane():
        print("[ Green : Red : Red : Red ]")
        print()

        time.sleep(3)

        print("[ Yellow : Red : Red : Red ]")
        print()

        time.sleep(1)

        print("[ Red : Red : Red : Red ]")
        print()
        print("[ Pedestrian : Green ]")
        print()

def second_lane():
        print("[ Red : Green : Red : Red ]")
        print()
        time.sleep(3)

        print("[ Red : Yellow : Red : Red ]")
        print()

        time.sleep(1)

        print("[ Red : Red : Red : Red ]")
        print()
        print("[ Pedestrian : Green ]")
        print()

def third_lane():
        print("[ Red : Red : Green : Red ]")
        print()

        time.sleep(3)

        print("[ Green : Red : Yellow : Red ]")
        print()

        time.sleep(1)

        print("[ Red : Red : Red : Red ]")
        print()
        print("[ Pedestrian : Green ]")
        print()

def fourth_lane():
        print("[ Red : Red : Red : Green ]")
        print()

        time.sleep(3)

        print("[ Red : Red : Red : Yellow ]")
        print()

        time.sleep(1)

        print("[ Red : Red : Red : Red ]")
        print()
        print("[ Pedestrian : Green ]")
        print()

def main():
    lane1 = int(input("Number of cars in first lane : "))
    lane2 = int(input("Number of cars in second lane : "))
    lane3 = int(input("Number of cars in third lane : "))
    lane4 = int(input("Number of cars in fourth lane : "))
    print()
    print("[ Pedestrian : Red ]")
    print()

    while True:
        if lane1 > lane2 and lane1 > lane3 and lane1 > lane4:
            first_lane()
            time.sleep(2)

        elif lane2 > lane1 and lane2 > lane3 and lane2 > lane4:
            second_lane()
            time.sleep(2)

        elif lane3 > lane2 and lane3 > lane1 and lane3 > lane4:
            third_lane()
            time.sleep(2)

        elif lane4 > lane2 and lane4 > lane3 and lane4 > lane1:
            fourth_lane()
            time.sleep(2)

        elif lane1 == lane2 or lane1 == lane3 or lane1 == lane2 or lane2 == lane3 or lane2 == lane4 or lane3 == lane4:
            if lane1 == lane2 or lane1 == lane2 or lane1 == lane3:
                first_lane()
                time.sleep(2)

            elif lane2 == lane3 or lane2 == lane4:
                second_lane()
                time.sleep(2)

            elif lane3 == lane4:
                third_lane()
                time.sleep(2)

            else:
                fourth_lane()
                time.sleep(2)

        lane1, lane2, lane3, lane4 = sum_of_vehicles(lane1, lane2, lane3, lane4)

        print("In lane1 : ", lane1)
        print("In lane2 : ", lane2)
        print("In lane3 : ", lane3)
        print("In lane4 : ", lane4)
        print()
        print("------------------------------")
        print()
        time.sleep(5)
        print("[ Pedestrian : Red ]")
        print()


if __name__ == '__main__':
    main()
