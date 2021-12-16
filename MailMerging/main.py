list = open('Input/Names/invited_names.txt')
list = [s.replace('\n', '') for s in list]
list.insert(0, '[name]')

letter = open('Input/Letters/starting_letter.txt', 'rt')
data = letter.read()
letter.close()
i = 0
for name in list[1:]:
    data = data.replace(list[i], name)
    with open(f'/home/cev/100-day-code/MailMerging/Output/ReadyToSend{name}.txt', 'wt') as newfile:
        newfile.write(data)
    i += 1
