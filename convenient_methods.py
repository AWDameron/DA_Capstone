import json
import csv
import emoji
import os
import convenient_lists

def emoji_organizer(text_list,file_name):
    emoji_list = []
    
    for entry in text_list:
        emojis_found = [e['emoji'] for e in emoji.emoji_list(entry)] 
        emoji_list.extend(emojis_found) 

    
    with open(f'Data_CSV/{file_name}.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(emoji_list) 
    print(f"{file_name}.csv has been created")

    return

def json_organizer(json_list, csv_name):
    text_list = []

    for file in json_list:
        with open(f"Raw_Data/{file}.json", 'r', encoding='utf-8') as file_json:
            data = json.load(file_json)
            for entry in data:
                post_text = entry.get('post_text', '').strip().replace("\n", " ")
                text_list.append(post_text)

    with open(f"Data_CSV/{csv_name}", 'a', newline='', encoding='utf-8') as csvfile:
         writer = csv.writer(csvfile, quotechar='"', quoting=csv.QUOTE_ALL)
         for text in text_list:
            writer.writerow([text])  

    print(f"Saved {len(text_list)} posts to {csv_name}")
    return

def CSV_duplicate_finder(csv_list,csv_name):
    text_list = []

    for file in csv_list:
        with open(f"Data_CSV/{file}.csv", 'r', encoding='utf-8') as file_csv:
            data = csv.reader(file_csv)    
            for entry in data:
                text_list.append(entry[0]) 
            
    clean_list = set(text_list)
    with open(f"Data_CSV/{csv_name}", 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, quotechar='"', quoting=csv.QUOTE_ALL)
        for item in clean_list:
            writer.writerow([item])
    print(f'{csv_name} has {len(text_list)-len(clean_list)} duplicates of {len(text_list)} posts')
    return clean_list

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