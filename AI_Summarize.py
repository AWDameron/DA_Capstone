import json
import csv

resume_list = [
    'resumetips.json',
    'resume tips.json',
    'Resume Writing Tips.json',
]

data_analysis_list = [    
    'Data Analysis Interviews.json',
    'data analysis languages.json',
    'data skills.json',
    'data programming.json'
    ]

interview_job_list = [
    'jobsearch.json',
    'interviewtips.json'
    ]

def bs_html_cleaner(file):
    text_list = []
    
    with open(f"Raw Data\\{file}", 'r', encoding = 'utf-8') as file_json:
        data = json.load(file_json)
 

    for i in data:
        text_list.append(data[0]['post_text'])

    print(file)
    print(len(text_list))
    print(text_list[0])
    

    return

bs_html_cleaner('resumetips.json')

# for file in json_list:
#     bs_html_cleaner(f"Raw Data\\{file}")
