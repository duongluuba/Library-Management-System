def view_books():
    column_widths = [4, 16, 24, 15]
    column_names = ["Bid |", "| Title ", "| Author", "| Status"]
    for i, name in enumerate(column_names):
        print(name.ljust(column_widths[i]), end="\t")
    print()
    print("-" * (sum(column_widths) + 3 * (len(column_names) - 1)))
    with open("books.txt", "r") as file:
        for line in file:
            bid, title, author, status = line.strip().split('\t')
            print(bid.ljust(column_widths[0])+'|', end="\t")
            print('|',title.ljust(column_widths[1]), end="\t")
            print('|',author.ljust(column_widths[2]), end="\t")
            print('|',status)