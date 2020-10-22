while True:
    words = input('Type some words! - ')
    print(f'You entered: {words}!')

    words = words.split(' ')

    for i in words:
        if len(i) >= 3:
            i = i + i[0]
            i = i[1:]

            print(i)

    print('\n')
