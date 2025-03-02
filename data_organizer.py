import json
import csv
import emoji
import csv_lists

def emoji_organizer(text_list):
    emoji_list = []
    
    for entry in text_list:
        emojis_found = [e['emoji'] for e in emoji.emoji_list(entry)] 
        emoji_list.extend(emojis_found) 

    # Save emojis to CSV
    with open('post_emojis.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(emoji_list) 

    return

def data_organizer(list,csv_name):
    text_list = []
    for file in list:
        with open(f"Raw Data\\{file}.json", 'r', encoding = 'utf-8') as file_json:
            data = json.load(file_json)
        
        with open(csv_name, 'a',newline='',encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile,quotechar='"',quoting=csv.QUOTE_ALL)
            for entry in data:
                text_list.append(entry['post_text'])
            clean_list = set(text_list)
            writer.writerow(clean_list)

    print(len(text_list))
    print(len(clean_list))
    print(f'{csv_name} has {len(text_list)-len(clean_list)} duplicates')
    emoji_organizer(clean_list)
    return 

# Turns data in to CSV files so they are easier to process
# 170 duplicate posts of 1218 posts scraped.
data_organizer(csv_lists.resume_list,'resume tips.csv')
data_organizer(csv_lists.interview_list,'interview tips.csv')
data_organizer(csv_lists.data_analysis_list,'data analysis tips.csv')
data_organizer(csv_lists.job_list,'job tips.csv')

print("data organized, emoji's organized")



