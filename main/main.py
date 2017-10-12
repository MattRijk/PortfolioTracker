from api.parser import TextParser

def main():
    path1 = '/Users/matthewrijk/PycharmProjects/PortfolioTracker/files/Baupost-3-31-17.txt'
    path2= '/Users/matthewrijk/PycharmProjects/PortfolioTracker/files/Baupost-06-30-17.txt'

    parser = TextParser()
    quarter_four, quarter_one = find_companies(parser, path1, path2)
    elements = parser.compare(quarter_one, quarter_four)
    print(elements)

def find_companies(parser, path1, path2):
    quarter_one = get_columns(parser, path1)
    quarter_four = get_columns(parser, path2)
    return quarter_four, quarter_one

def get_columns(parser, path2):
    b = parser.splitbylines(path2)
    quarter_four = parser.first_column(b)
    return quarter_four

if __name__ == '__main__':
    main()


