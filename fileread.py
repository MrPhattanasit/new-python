def main():
    infile = open('philosophees.txt', 'r')
    file_contents = infile.read()
    infile.close()
    print(file_contents)
main()