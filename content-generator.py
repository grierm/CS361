from future.moves import tkinter
# from tkinter import *
import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter
import csv
import sys

url = "https://en.wikipedia.org/wiki/"


# Function for the webcrawler
def web_scrape(site, prime, second):
    # Get user input
    # primary_kw = input("Enter primary keyword: ")
    # secondary_kw = input("Enter secondary keyword: ")
    site = url + prime
    primary_kw = prime.lower()
    secondary_kw = second.lower()

    # list for the paragraph on the site
    word_list = []
    source_code = requests.get(site).text

    # Ping the site for the data
    soup = BeautifulSoup(source_code, 'html.parser')

    print(primary_kw, " ", secondary_kw)
    #print(soup.get_text())
    # Search all <p> for the words
    for each_text in soup.findAll('p'):
        content = each_text.text
        #print(content)
        #print(content)
        # Split the sentence into words
        words = content.lower().split()

        if primary_kw in content and secondary_kw in content:
            for each_word in words:
                word_list.append(content)
                if each_word == "\n":
                    break
        #for each_word in words:
        #    if "puppy" in content:
        #        word_list.append(each_word)
        #print(word_list)


    with open('output.csv', 'w', newline='') as output_file:
        header_names = ['input_keywords', 'output_content']
        the_writer = csv.DictWriter(output_file, fieldnames=header_names)

        # Write headers
        the_writer.writeheader()
        # Write rows
        the_writer.writerow({'input_keywords' : primary_kw+";"+secondary_kw, 'output_content' : word_list[0]})

        #the_writer.writerow([primary_kw+";"+secondary_kw, word_list[0]])

    # with open('output.csv', mode='w', newline="") as output_file:
    # the_writer = csv.writer(open("output_file.csv", 'wb'))
    # #writer.writerow(["word_list[0]"])
    # print(the_writer)

# web_scrape(url)

#pk = 0
#sk = 0



#try:
if len(sys.argv) > 1:
    file_name = sys.argv[1]
    f = open(file_name, 'r')
    file = csv.reader(f)
    data = list(file)

    words = data[1]
    word = words[0].split(";")
    primary_kw = word[0]
    secondary_kw = word[1]

    url = url + primary_kw
    #for row in data:
     #   print(row)
else:
    top = tkinter.Tk()
    top.title("Content Generator")

    # this wil create a label widget
    p = tkinter.Label(top, text="Primary Keyword:")
    s = tkinter.Label(top, text="Secondary Keyword:")
    # code for project here

    # grid method to arrange labels in respective
    # rows and columns as specified
    p.grid(row=0, column=0, sticky=tkinter.W, pady=2)
    s.grid(row=1, column=0, sticky=tkinter.W, pady=2)

    # entry widgets, used to take entry from user
    e1 = tkinter.Entry(top)
    e2 = tkinter.Entry(top)

    def click_button():
        pk = e1.get().lower()
        sk = e2.get().lower()
        my_label = tkinter.Label(top, text="Output.csv created!")
        # my_label.pack()
        my_label.grid(row=3, column=1, pady=2)

        web_scrape(url, pk, sk)


    my_button = tkinter.Button(top, text="Export to CSV", command=click_button)

    # this will arrange entry widgets
    e1.grid(row=0, column=1, pady=2)
    e2.grid(row=1, column=1, pady=2)
    my_button.grid(row=2, column=1, pady=2)

    # entry = tkinter.Entry(top, width=50, bg="white", fg="gray", borderwidth=5)
    # entry.pack()
    # label = tkinter.Label(top, text="pk")
    # label.grid(row=0, column=0)

    # def click_button():
    #     pk = e1.get()
    #     my_label = tkinter.Label(top, text="The button was clicked", width=50)
    #     my_label.grid(row=3, column=1, pady=2)
    #     print(pk)

    # my_button = tkinter.Button(top, text="Export to CSV", command=click_button)
    # #my_button.grid(row=0, column=5)

    top.mainloop()

#except:
    #print("Error reading file: ")
    # Add tkinter functionality




