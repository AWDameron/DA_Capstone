import json
import csv
import emoji
import os
import convenient_lists
 
 # checks a list for emojis and puts them into a separate CSV file
 # For EACH list that this method reads, it will make a new row in a CSV file.
 # emoji_organizer is specifically designed to be built into the CSV_duplicate_finder method
 # can be nested inside of the duplicate finder method.
def emoji_organizer(text_list,file_name):
    create_folders()
    emoji_list = []
    
    for entry in text_list:
        emojis_found = [e['emoji'] for e in emoji.emoji_list(entry)] 
        emoji_list.extend(emojis_found) 

    
    with open(f'Data_CSV/{file_name}.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(emoji_list) 
    print(f"{file_name}.csv has been created")

    return

# json_organizer converts a list of json files into a csv.  Could effectively run a single 
# file if file is placed in square brackets, but ideally it is cleaning a list of scraped JSON files
# returns the csv_name of the newly created CSV file for faster method handling.
def json_organizer(json_list, csv_name):
    create_folders()
    text_list = []

    for file in json_list:
        with open(f"Raw_Data/{file}.json", 'r', encoding='utf-8') as file_json:
            data = json.load(file_json)
            for entry in data:
                post_text = entry.get('post_text', '').strip().replace("\n", " ")
                text_list.append(post_text)
        file_json.close()

    with open(f"Data_CSV/{csv_name}", 'a', newline='', encoding='utf-8') as csvfile:
         writer = csv.writer(csvfile, quotechar='"', quoting=csv.QUOTE_ALL)
         for text in text_list:
            writer.writerow([text])  
    csvfile.close()

    print(f"Saved {len(text_list)} posts to {csv_name}")
    return csv_name

# CSV_duplicate_finder opens a (dirty) CSV created by the json_organizer and then transfer it to a list
# that list is turned into a SET so that all duplicates are removed and that set is then placed into a new
# (clean) CSV file to avoid confusion. Double checks that you are not using a duplicate file name for the clean
# and dirty file.

def CSV_duplicate_finder(dirty_csv,clean_csv):
    create_folders()
    if dirty_csv == clean_csv:
        print("File names should be two separate names, check method call")
        return
    else:
        text_list = []

        with open(f"Data_CSV/{dirty_csv}.csv", 'r', encoding='utf-8') as file_csv:
            data = csv.reader(file_csv)    
            for entry in data:
                text_list.append(entry[0]) 
            file_csv.close()
                
        clean_list = set(text_list)
        with open(f"Data_CSV/{clean_csv}", 'a', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file, quotechar='"', quoting=csv.QUOTE_ALL)
            for item in clean_list:
                writer.writerow([item])
            csv_file.close()
        post_list = list(clean_list)
        print(f'{clean_csv} has {len(text_list)-len(clean_list)} duplicates of {len(text_list)} posts')
        return post_list


# Creates pre-equisite folders for various methods, added into the top of all methods to prevent errors when accessing or saving 
# CSV files.  Will not make new folders if there is already a folder in place, if it finds no folder it will create them as "Data_CSV" and "Raw_Data"  
def create_folders():
    os.makedirs(os.path.join("Data_CSV"), exist_ok=True)
    os.makedirs(os.path.join("Raw_Data"), exist_ok=True)
    return



if __name__ == "__main__":

    json_organizer(convenient_lists.resume_list,'resume tips.csv')
    json_organizer(convenient_lists.interview_list,'interview tips.csv')
    json_organizer(convenient_lists.data_analysis_list,'data analysis tips.csv')
    json_organizer(convenient_lists.job_list,'job tips.csv')
    print("data organized, emoji's organized")




'''
resume tips.csv has 89 duplicates
interview tips.csv has 17 duplicates
data analysis tips.csv has 43 duplicates
job tips.csv has 21 duplicates
'''

'''
Saved 302 posts to resume tips.csv
Saved 305 posts to interview tips.csv
Saved 307 posts to data analysis tips.csv
Saved 304 posts to job tips.csv
'''