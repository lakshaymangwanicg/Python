option = int(input("Enter main option: "))

match option:
    case 1:
        engine_option = int(input("Enter engine option: "))
        match engine_option:
            case 1:
                print("Engine Started")
            case 2:
                print("Engine Stopped")
            case _:
                print("Invalid Option Selected")
    case 2:
        lights_option = int(input("Enter lights option: "))
        match lights_option:
            case 1:
                print("Headlights Selected")
            case 2:
                print("Indicators Selected")
            case 3:
                print("Hazard Lights Selected")
            case _:
                print("Invalid Option Selected")
    case 3:
        music_option = int(input("Enter music option: "))
        match music_option:
            case 1:
                print("Music Playing")
            case 2:
                print("Music Paused")
            case 3:
                print("Next Track Selected")
            case 4:
                print("Previous Track Selected")
            case _:
                print("Invalid Option Selected")
    case 4:
        nav_option = int(input("Enter navigation option: "))
        match nav_option:
            case 1:
                print("Navigation Started")
            case 2:
                print("Navigation Stopped")
            case _:
                print("Invalid Option Selected")
    case _:
        print("Invalid Main Option Selected")