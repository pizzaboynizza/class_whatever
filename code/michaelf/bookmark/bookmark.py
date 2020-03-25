import cv2 as cv
import pytesseract
import datetime
import numpy as np
from sys import argv
import matplotlib.pyplot as plt
import csv


script, logfile, filename = argv

def image_to_txt(filename):
    img = cv.imread(filename, cv.IMREAD_GRAYSCALE)
    # img = cv.resize(img, (1125, 1500))
    retval, thresh = cv.threshold(np.array(img), 160, 255, cv.THRESH_BINARY)
    
    # cv.imshow('thresh',thresh)
    # cv.waitKey(0)

    # kernel = np.ones((5,5),np.uint8)
    # erosion = cv.erode(thresh,kernel,iterations = 1)
    # # cv.imshow('erosion', erosion)
    # dilation = cv.dilate(erosion,kernel,iterations = 1)
    # # cv.imshow('dilation', dilation)
    
    text = pytesseract.image_to_string(thresh)
    print(text)
    return text

def clean_up(text):
    text = list(filter(lambda line:line == '' or line.isnumeric() == True or len(line) > 6 , text))
    return text

def has_number(line):
    return any(char.isdigit() for char in line)

def is_all_caps(line):
    if line.isupper()== True:
        return True

def has_no_text(line):
    if any(char.isalnum() for char in line):
        return False
    else:
        return True

def delete_empty(text):
    if has_no_text(text[0]) == True:
        text.pop(0)
    return text
   
def get_title_and_page(text):
    if text[0].isnumeric() == True:
        page_number = text.pop(0)
        text = delete_empty(text)
    if text[0].isupper()== True:
        if 'CHAPTER' in text[0]:
            book_title = ' N/A'
            page_number = text[0]
        else:
            book_title = text.pop(0).split()
            page_number = ' N / A'

        if book_title[0].isnumeric() == True:
            page_number = book_title.pop(0)

        for i in range(0,len(book_title)):
            if book_title[i].isnumeric() == True:
                page_number = book_title.pop(i)
            # else:
            #     page_number = ' N / A'

    else:
        book_title = ' N/A'
        page_number = ' N / A'
             
    return book_title, page_number
    
def get_bookmark(text):
    # if text[0]== '':
    #     text.pop(-1)
    bookmark_index = text.index('')
    if text[0] == '':
        bookmark = text[bookmark_index+1]
    elif text[0][0].isupper() == True:
        bookmark = text[0]
    elif text[0].istitle() == True:
        bookmark = text[0]
    else:
        bookmark = text[bookmark_index+1]

    return bookmark

def current_time():
    time_stamp = datetime.datetime.now()
    time_stamp = time_stamp.strftime("%Y-%m-%d %H:%M %p")
    return time_stamp

def log(time_stamp, book_title, page_number, bookmark, logfile):
    book_title = ' '.join(book_title)
    write_line = f"{time_stamp}\nTitle:{book_title}\nPage:{page_number}\nBookmark:'{bookmark}'"
    with open(logfile, 'a') as f:
        f.write(write_line + '\n')

def main():
    text = image_to_txt(filename)
    text = text.splitlines()
    text = clean_up(text)
    print(text)
    text = delete_empty(text)
    print(text)
    book_title, page_number = get_title_and_page(text)
    print(text)
    bookmark = get_bookmark(text)
    time_stamp = current_time()
    log(time_stamp, book_title, page_number, bookmark, logfile)

main()
















### write to csv instead of text
# def log(time_stamp, book_title, page_number, bookmark, logfile):
#     book_title = ' '.join(book_title)
#     with open(logfile, 'w') as f:
#         keys = ['title', 'page', 'bookmark']
#         writer = csv.DictWriter(f, fieldnames = keys)
#         writer.writeheader()
#         writer.writerow({f'title': {book_title}, 'page': {page_number}, 'bookmark': {bookmark}})
#         # f.write(write_line + '\n')
