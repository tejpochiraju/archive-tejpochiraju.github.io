#!/bin/python

import csv

data_file = "_data/projects.csv"
      

def add_to_set(input_list,output_set):
    for el in input_list:
                el = el.strip()
                if el:
                    output_set.add(el.strip())


def main():
    #Initialise the main dictionary
    data = {}
    tags = set()
    contributions = set()
    arenas = set()
    domains = set()
    statuses = set()
    clients = set()
    file_string = "---\nlayout: portfolio\npermalink: /tag/tag_url/\ntags: tag_name\n---"
    nav = "nav:\n"
    nav_section = "  - title: category_name\n    items:\n"
    nav_item = "      - page: item_name\n        url: /tag/item_url/\n"


    with open(data_file) as csvfile:
        #Read the csv file as a list of dictionaries
        reader = csv.DictReader(csvfile)
        for row in reader:
            row_tags = row["Tags"].split(",")
            row_contributions = row["Contribution"].split(",")
            row_arenas = row["Arena"].split(",")
            row_domains = row["Domains"].split(",")
            row_statuses = row["Status"].split(",")
            row_clients = row["Client"].split(",")

            add_to_set(row_tags,tags)
            add_to_set(row_contributions,contributions)
            add_to_set(row_arenas,arenas)
            add_to_set(row_domains,domains)
            add_to_set(row_statuses,statuses)
            add_to_set(row_clients,clients)
    
    nav += nav_section.replace("category_name","Contribution")
    for item in contributions:
        nav += nav_item.replace("item_name",item).replace("item_url",item.lower())

    nav += nav_section.replace("category_name","Domain")
    for item in domains:
        nav += nav_item.replace("item_name",item).replace("item_url",item.lower())

    nav += nav_section.replace("category_name","Status")
    for item in statuses:
        nav += nav_item.replace("item_name",item).replace("item_url",item.lower())

    nav += nav_section.replace("category_name","Arena")
    for item in arenas:
        nav += nav_item.replace("item_name",item).replace("item_url",item.lower())

    with open ("_data/navigation.yml", "w") as f:
        f.write(nav)

    for tag in tags:
        tag_file_string = file_string.replace("tag_url",tag.lower()).replace("tag_name",tag)
        with open ("_pages/tag/{}.md".format(tag.lower()), "w") as f:
            f.write(tag_file_string)





#Execute the main loop
if __name__ == "__main__":
    main()
