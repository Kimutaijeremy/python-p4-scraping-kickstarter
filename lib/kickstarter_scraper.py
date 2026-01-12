from bs4 import BeautifulSoup

def create_project_dict():
    html = ''
    with open('./fixtures/kickstarter.html') as file:
        html = file.read()

    kickstarter = BeautifulSoup(html, 'html.parser')
    projects = {}
    
    # Iterate through the projects
    for project in kickstarter.select("li.project.grid_4"):
        title = project.select("h2.bbcard_name strong a")[0].text
        projects[title] = {
            'image_link': project.select("div.project-thumbnail a img")[0]['src'],
            'description': project.select("p.bbcard_blurb")[0].text,
            'location': project.select("ul.project-meta span.location-name")[0].text,
            'percent_funded': project.select("ul.project-stats li.first.funded strong")[0].text.replace("%", "")
        }
    
    return projects

# Test the function
if __name__ == "__main__":
    result = create_project_dict()
    print(f"Number of projects scraped: {len(result)}")
    for title, data in list(result.items())[:3]:  # Show first 3
        print(f"\nProject: {title}")
        print(f"Image: {data['image_link']}")
        print(f"Description: {data['description'][:50]}...")
        print(f"Location: {data['location']}")
        print(f"Percent Funded: {data['percent_funded']}%")