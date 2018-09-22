def csv_parser(s):
    """Parses the string s into lines, and then parses those lines by
    splitting on the comma and converting the numerical data to int.
    The output is a list of lists of subject data."""

    # Data is our output. It will be a list of lists.
    data = []

    lines = s.split('\n')# Split csv into lines and store them in a list called 'lines'.
    
    lines = lines[1:]# Remove the first element from lines, so that you have only the data lines left.
    
    for l in lines:
        row = l.strip().split(',')
        row[0] = int(row[0])
        row[1] = float(row[1])
        data.append(row)
    return data
print(csv_parser("""Subject,Height,Occupation
1,74.37000326528938,Psychologist
2,67.49686206937491,Psychologist
3,74.92356434760966,Psychologist
4,64.62372198999978,Psychologist
5,67.76787900026083,Linguist
6,61.50397707923559,Psychologist
7,62.73680961908566,Psychologist
8,68.60803984763902,Linguist
9,70.16090500135535,Psychologist
10,76.81144438287173,Linguist"""))
