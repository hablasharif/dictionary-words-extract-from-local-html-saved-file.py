# import re
# from bs4 import BeautifulSoup

# # Path to the HTML file
# file_path = r"C:\Users\style\Desktop\Movies Subtitles English\dictionary words storing\Dictionary Over 10000 english to bangla words.html"
# output_file = r"C:\Users\style\Desktop\Movies Subtitles English\dictionary words storing\english_to_bangla_words_filtereded.txt"

# try:
#     # Step 1: Read the content of the .html file
#     with open(file_path, "r", encoding="utf-8") as file:
#         html_content = file.read()

#     # Step 2: Parse HTML content using BeautifulSoup
#     soup = BeautifulSoup(html_content, 'html.parser')

#     # Step 3: Extract English words and their Bangla meanings (excluding errors)
#     english_to_bangla_pairs = []
#     table = soup.find('table')
#     if table:
#         rows = table.find_all('tr')
#         for row in rows:
#             columns = row.find_all('td')
#             if len(columns) == 3:
#                 english_word = columns[0].get_text(strip=True)
#                 bangla_meaning = columns[1].get_text(strip=True)

#                 # Check if the Bangla meaning is not an error message
#                 if "Sorry" not in bangla_meaning and "Timeout error" not in bangla_meaning:
#                     english_to_bangla_pairs.append((english_word, bangla_meaning))

#     # Step 4: Save English words and Bangla meanings to a .txt file
#     with open(output_file, "w", encoding="utf-8") as output:
#         for pair in english_to_bangla_pairs:
#             output.write(f"{pair[0]} = {pair[1]}\n")

#     print(f"Filtered English words and Bangla meanings saved to {output_file}")

# except FileNotFoundError:
#     print(f"File '{file_path}' not found.")
# except Exception as e:
#     print(f"An error occurred: {str(e)}")
