if __name__ == '__main__':
    with open('zadanie2.csv', 'r') as file, open('result.csv', 'w', newline='') as output:
        reader = file.read()
        csv_file = reader.splitlines()

        # deleting rows without values
        for row in csv_file[1:]:
            splitted = row.split(',', 1)
            if splitted.count(''):
                csv_file.remove(row)
            else:
                row = splitted

        # creating lists in list
        lst = [csv_file[i].split(',', 1) for i in range(1, len(csv_file))]

        # Sorting_Algorithm ids
        for i in range(len(lst)):
            lst[i][0] = int(lst[i][0])
            lst[i][1] = lst[i][1].lower()
        lst.sort()

        # correcting numeration
        for i in range(len(lst)):
            for elem in lst[:i]:
                if elem[0] == lst[i][0]:
                    lst[i][0] = int(lst[i - 1][0]) + 1

        # subsection 6
        for row in lst:
            for i in range(1, len(row)):
                words = row[i].split(' ')
                for word in words:
                    try:
                        if abs(ord(word[0]) - ord(word[1])) == 1:
                            print('Removed word: "{}" from id: {}'.format(word, row[0]))
                            words.remove(word)
                    except IndexError:
                        pass

        # turning to string
        for elem in lst:
            elem[0] = str(elem[0])

        # saving to result.csv
        header = ['id', 'value']
        lst.insert(0, header)
        for line in lst:
            line = ','.join(line)
            output.write(line + '\n')

    # closing files
    output.close()
    file.close()
