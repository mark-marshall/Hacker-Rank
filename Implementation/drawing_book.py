# https://www.hackerrank.com/challenges/drawing-book/problem
def pageCount(n, p):
    # initiate a book array with the first page set of None, 1
    book = [[None, 1]]
    # create the rest of the book array as sets of 2 pages
    for i in range(2, n + 1, 2):
        if (i + 1) <= n:
            book.append([i, i + 1])
        else:
            book.append([i, None])
    # initialize variables for page counts
    cur_page_forwards = 0
    pages_turned_forwards = 0
    cur_page_backwards = len(book) - 1
    pages_turned_backwards = 0
    # turn pages forwards and backwards simultaneously until the page is found
    while p not in book[cur_page_forwards] + book[cur_page_backwards]:
        cur_page_forwards += 1
        pages_turned_forwards += 1
        cur_page_backwards -= 1
        pages_turned_backwards += 1
    # return the smallest number of page turns
    return min(pages_turned_forwards, pages_turned_backwards)
