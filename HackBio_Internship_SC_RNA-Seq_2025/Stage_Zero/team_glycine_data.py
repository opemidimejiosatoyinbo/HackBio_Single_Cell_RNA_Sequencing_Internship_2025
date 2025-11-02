"""
HackBio Internship - Stage 0 Python Task
Team: Glycine

# Task: Write a simple Python script for printing the names, slack username, country, 1 hobby, affiliations of people on your team and the DNA sequence of the genes they love most.
# Author: Opemidimeji Osatoyinbo
# GitHub: https://github.com/opemidimejiosatoyinbo
# LinkedIn: https://linkedin.com/in/opemidimejiosatoyinbo
"""

# Create data as a list of dictionaries
# Each dictionary represents one member
team_glycine_info = [
    {"Name": "NAME", "Slack": "SLACK ID", "Country": "COUNTRY", "Hobby": "HOBBY", "Affiliation": "AFFILIATION", "Favorite Gene": "GENE", "Sequence": "GENE SEQUENCE"}, # This will appear as the Header when the team info output is displayed
    {"Name": "Vishnushiri", "Slack": "vishnu shiri", "Country": "India", "Hobby": "Reading", "Affiliation": "Bioinformatician", "Favorite Gene": "SOD1", "Sequence": "ATGGCGACGAAGGCCGTGTG"},
    {"Name": "Joy", "Slack": "Abiodun Joy", "Country": "Nigeria", "Hobby": "Exploring", "Affiliation": "Statistician, ML Researcher", "Favorite Gene": "NIL", "Sequence": "NIL"},
    {"Name": "Victor", "Slack": "ONAH", "Country": "Nigeria", "Hobby": "Footballing", "Affiliation": "Bioinformatician", "Favorite Gene": "NIL", "Sequence": "NIL"},
    {"Name": "Aakash", "Slack": "Aakash Deva Thirukonda", "Country": "Sweden", "Hobby": "Cooking", "Affiliation": "Bioinformatician", "Favorite Gene": "TP53", "Sequence": "ATGGAGGAGCCGCAGTCAGAT"},
    {"Name": "Mary", "Slack": "Alo Yetunde Mary", "Country": "Nigeria", "Hobby": "Reading", "Affiliation": "Bioinformatician", "Favorite Gene": "DNMT3A", "Sequence": "ATGGAGCTGCCGCGCGGCGG"},
    {"Name": "Opemidimeji", "Slack": "Opemidimeji Osatoyinbo", "Country": "Nigeria", "Hobby": "Exploring", "Affiliation": "Researcher: Microbiologist; Molecular Biologist", "Favorite Gene": "mecA", "Sequence": "ATGGTCTGGACGTTGTCCAG"},
    {"Name": "Amin", "Slack": "Amin", "Country": "Malaysia", "Hobby": "Reading", "Affiliation": "Molecular Biologist", "Favorite Gene": "TERT", "Sequence": "ATGCCGCGCGCTCCCCGCGG"},
    {"Name": "Oluwaseun", "Slack": "Oluwaseun Awosise", "Country": "Nigeria", "Hobby": "Watching Sitcoms", "Affiliation": "Computational Biologist", "Favorite Gene": "BRCA1", "Sequence": "GCTGAGACTTCCTGGACGGG"},
    {"Name": "Ishita", "Slack": "Ishita Chopra", "Country": "India", "Hobby": "Reading, Hiking", "Affiliation": "Bioinformatician", "Favorite Gene": "BCL2", "Sequence": "ATGGCGCACGCTGGGAGAAC"},
    {"Name": "Opeoluwa", "Slack": "Eadencre8ives", "Country": "Nigeria", "Hobby": "Troubleshooting & Movies", "Affiliation": "Microbiology, Bioinformatics, Molecular Biology", "Favorite Gene": "BRCA1", "Sequence": "GCTGAGACTTCCTGGACGGG"},
    {"Name": "Olorunfemi", "Slack": "Femi", "Country": "Nigeria", "Hobby": "Watching Movies", "Affiliation": "Cell Biology and Genetics, Bioinformatics", "Favorite Gene": "SHH", "Sequence": "ATGCTGCTGCTGCTGCTGCT"}
]

# To print team information
print("\nHackBio Team Glycine Information:\n")

# Iterate through each team member and print their details
for member in team_glycine_info:
    print(f"{member['Name']:<15}{member['Slack']:<25}{member['Country']:<12}{member['Hobby']:<25}{member['Affiliation']:<60}{member['Favorite Gene']:<8}{member['Sequence']}")
    
print(f"\nTotal_team_members: {len(team_glycine_info)-1}") # This removes the first dictionary in team_Glycine_info serving as the header